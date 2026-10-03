from __future__ import annotations

import logging
import re
from collections.abc import Mapping
from copy import deepcopy
from dataclasses import dataclass, field
from typing import Any

import voluptuous as vol
from homeassistant.core import HomeAssistant, valid_entity_id
from homeassistant.helpers import device_registry as dr

from .color_cycle import CYCLE_ACTION, DEFAULT_PALETTE, normalize_palette
from .const import PICO_TYPE_MAP, VALID_PICO_TYPES
from .placeholder import placeholder_entity_id
from .script_runner import has_template, script_schema

_LOGGER = logging.getLogger(__name__)

_VALID_4B_BUTTONS = frozenset(
    {
        "button_1",
        "button_2",
        "button_3",
        "off",
    }
)

ActionConfig = dict[str, Any]

PICO_BUTTONS = {
    "P2B": frozenset({"on", "off"}),
    "2B": frozenset({"on", "off"}),
    "2BRL": frozenset({"on", "off", "raise", "lower"}),
    "3BRL": frozenset({"on", "off", "raise", "lower", "stop"}),
    "4B": _VALID_4B_BUTTONS,
}

STOP_GESTURES = frozenset({"stop_tap", "stop_double_tap", "stop_hold"})


def override_button(key: str) -> str | None:
    """Extract a button using the longest gesture suffix first."""
    for gesture in ("double_tap", "tap", "hold"):
        suffix = f"_{gesture}"
        if key.endswith(suffix):
            return key[: -len(suffix)]
    return None


@dataclass
class PicoConfig:
    """Normalized configuration for one Pico remote."""

    device_id: str
    type: str

    # Exactly one domain must be assigned for non-4B Picos.
    covers: list[str] = field(default_factory=list)
    fans: list[str] = field(default_factory=list)
    lights: list[str] = field(default_factory=list)
    media_players: list[str] = field(default_factory=list)
    switches: list[str] = field(default_factory=list)

    # Normalized action parameters in milliseconds.
    hold_time_ms: int = 400
    double_tap_time_ms: int = 300
    step_time_ms: int = 650

    # Custom sequences share one execution policy per physical remote.
    mode: str = "single"
    max: int = 10
    max_exceeded: str = "warning"

    # Cover configuration.
    cover_open_pos: int = 100
    cover_step_pct: int = 10
    cover_inverted: bool = False

    # Fan configuration.
    fan_on_pct: int = 100

    # Light configuration.
    light_on_pct: int = 100
    light_low_pct: int = 5
    light_step_pct: int = 10
    light_transition_on: int = 0
    light_transition_off: int = 0

    # Media-player configuration.
    media_player_vol_step: int = 10

    # 3BRL only.
    middle_button: list[ActionConfig] = field(default_factory=list)

    # 4B only.
    buttons: dict[str, list[ActionConfig]] = field(default_factory=dict)

    # Explicit gesture overrides; absence and an empty list are distinct.
    overrides: dict[str, list[ActionConfig]] = field(default_factory=dict)

    # Native cycles share gesture recognition, but are not script sequences.
    color_cycle_gestures: set[str] = field(default_factory=set)
    color_palette: list[dict[str, Any]] = field(default_factory=list)

    def validate(self) -> None:
        """Validate the normalized Pico configuration."""
        if self.type not in VALID_PICO_TYPES:
            valid_types = ", ".join(sorted(VALID_PICO_TYPES))

            raise ValueError(
                f"Invalid Pico type {self.type!r}. Must be one of: {valid_types}"
            )

        domain_lists = {
            "covers": self.covers,
            "fans": self.fans,
            "lights": self.lights,
            "media_players": self.media_players,
            "switches": self.switches,
        }

        active_domains = [name for name, entities in domain_lists.items() if entities]

        if self.type == "4B":
            if active_domains:
                raise ValueError(
                    f"Pico {self.device_id} (4B) cannot define "
                    f"entity domains: {', '.join(active_domains)}. "
                    "Use button actions instead."
                )

            if not self.buttons and not self.overrides:
                raise ValueError(
                    f"Pico {self.device_id} (4B) must define "
                    "a non-empty 'buttons' mapping or button gesture overrides."
                )

            if self.middle_button:
                raise ValueError(
                    f"Pico {self.device_id} (4B) cannot define 'middle_button'."
                )

            return

        if len(active_domains) != 1:
            if not active_domains:
                raise ValueError(
                    f"Pico {self.device_id} must define exactly "
                    "one of: covers, fans, lights, media_players, "
                    "switches."
                )

            raise ValueError(
                f"Pico {self.device_id} defines multiple entity "
                f"domains: {', '.join(active_domains)}. "
                "Only one is allowed."
            )

        if self.buttons:
            raise ValueError(
                f"Pico {self.device_id} ({self.type}) cannot "
                "define 'buttons'. 'buttons' is only valid for "
                "4B Picos."
            )


# ================================================================
# DEVICE LOOKUP
# ================================================================


def lookup_device_id(
    hass: HomeAssistant,
    name: str,
) -> str | None:
    """Resolve a unique device by user-assigned or registry name."""
    device_registry = dr.async_get(hass)
    devices = device_registry.devices
    # New HA registries iterate entries directly; older releases expose a mapping.
    # Check the container type without accessing deprecated lookup methods.
    entries = tuple(devices.values() if isinstance(devices, Mapping) else devices)

    # Prefer the user-assigned name over the integration-provided name.
    for attribute in (
        "name_by_user",
        "name",
    ):
        matches = [
            device
            for device in entries
            if getattr(device, attribute) == name
        ]

        if len(matches) > 1:
            raise ValueError(
                f"Multiple devices are named {name!r}. "
                "Configure this Pico using device_id."
            )

        if matches:
            return matches[0].id

    return None


def _detect_pico_type(hass: HomeAssistant, device_id: str) -> str:
    """Read a supported Lutron type from the local registry during setup only."""
    device = dr.async_get(hass).async_get(device_id)
    hint = "Specify 'type' explicitly on this device, then restart Home Assistant."

    if device is None:
        raise ValueError(
            f"Cannot detect Pico type for {device_id}: no device registry entry. {hint}"
        )

    lutron_entries = {
        entry.entry_id for entry in hass.config_entries.async_entries("lutron_caseta")
    }
    if not device.config_entries.intersection(lutron_entries):
        raise ValueError(
            f"Cannot detect Pico type for {device_id}: device is not registered "
            f"with the Lutron Caseta integration. {hint}"
        )

    # HA records models as "<model number> (<Lutron type>)". Accept the raw
    # Lutron type too, but never infer a layout from a name or partial match.
    model = device.model.strip() if isinstance(device.model, str) else ""
    match = re.fullmatch(r"[^()]*\(([^()]+)\)", model)
    raw_type = match.group(1).strip() if match else model
    pico_type = PICO_TYPE_MAP.get(raw_type)
    if pico_type is None:
        raise ValueError(
            f"Cannot detect Pico type for {device_id}: unrecognized or missing "
            f"Lutron model {device.model!r}. {hint}"
        )

    _LOGGER.debug("Detected Pico type %s for device %s", pico_type, device_id)
    return pico_type


def _resolve_device_id(
    hass: HomeAssistant,
    merged: dict[str, Any],
) -> str:
    """Resolve the configured Pico device ID."""
    raw_device_id = merged.get("device_id")

    if raw_device_id is not None:
        if not isinstance(raw_device_id, str) or not raw_device_id.strip():
            raise ValueError("'device_id' must be a non-empty string.")

        # The Lutron event supplies the Home Assistant device ID.
        # Do not require a particular registry identifier format.
        return raw_device_id.strip()

    raw_name = merged.get("name")

    if not isinstance(raw_name, str) or not raw_name.strip():
        raise ValueError("Device must define a non-empty 'device_id' or 'name'.")

    name = raw_name.strip()

    device_id = lookup_device_id(
        hass,
        name,
    )

    if device_id is None:
        raise ValueError(f"No device was found with name {name!r}.")

    _LOGGER.debug(
        "Resolved device name %r to device_id %s",
        name,
        device_id,
    )

    return device_id


# ================================================================
# VALUE NORMALIZATION
# ================================================================


def _normalize_int(
    raw_val: Any,
    default: int,
    min_val: int,
    max_val: int,
) -> int:
    """
    Convert a value to int and clamp it to the allowed range.

    Invalid values and zero use the supplied default.
    """
    if isinstance(raw_val, bool):
        return default

    try:
        value = int(raw_val)
    except (TypeError, ValueError):
        value = default

    if value == 0:
        return default

    return max(
        min_val,
        min(max_val, value),
    )


def _normalize_bool(
    raw_val: Any,
    default: bool = False,
) -> bool:
    """Normalize a strict Boolean configuration value."""
    if raw_val is None:
        return default

    if isinstance(raw_val, bool):
        return raw_val

    if isinstance(raw_val, str):
        value = raw_val.strip().lower()

        if value in {
            "true",
            "yes",
            "on",
            "1",
        }:
            return True

        if value in {
            "false",
            "no",
            "off",
            "0",
        }:
            return False

    raise ValueError(f"Expected a Boolean value, got {raw_val!r}.")


def _normalize_entities(
    value: Any,
    *,
    key: str,
    domain: str,
) -> list[str]:
    """Normalize and validate an entity ID or entity-ID list."""
    if value is None:
        return []

    if isinstance(value, str):
        raw_entities = [value]
    elif isinstance(value, list):
        raw_entities = value
    else:
        raise ValueError(f"'{key}' must be an entity ID or a list of entity IDs.")

    entities: list[str] = []

    for index, item in enumerate(
        raw_entities,
        start=1,
    ):
        if not isinstance(item, str):
            raise ValueError(
                f"'{key}' entry {index} must be a string, got {type(item).__name__}."
            )

        entity_id = item.strip()

        if not valid_entity_id(entity_id):
            raise ValueError(
                f"'{key}' entry {index} contains invalid entity ID {entity_id!r}."
            )

        entity_domain = entity_id.split(
            ".",
            1,
        )[0]

        if entity_domain != domain:
            raise ValueError(
                f"'{key}' entry {index} must use the "
                f"{domain!r} domain, got {entity_id!r}."
            )

        # Preserve order while removing duplicates.
        if entity_id not in entities:
            entities.append(entity_id)

    return entities


# ================================================================
# ACTION VALIDATION
# ================================================================


def _normalize_action(
    value: Any,
    *,
    context: str,
) -> ActionConfig:
    """Validate and copy one Home Assistant action mapping."""
    if not isinstance(value, dict):
        raise ValueError(f"{context} must be a mapping, got {type(value).__name__}.")

    action = deepcopy(value)
    # Preserve diagnostics for the original flat format. Structured actions
    # use HA validation after assigned-entity placeholders are expanded.
    if (
        "action" not in action
        or has_template(action)
        or not action.keys() <= {"action", "target", "data"}
    ):
        return action
    action_name = action.get("action")

    if not isinstance(action_name, str):
        raise ValueError(f"{context} must define an 'action' string.")

    domain, separator, service = action_name.partition(".")

    if not separator or not domain or not service:
        raise ValueError(
            f"{context} contains invalid action "
            f"{action_name!r}. Expected 'domain.service'."
        )

    data = action.get(
        "data",
        {},
    )

    if not isinstance(data, dict):
        raise ValueError(f"{context} data must be a mapping.")

    target = action.get("target")

    if target is not None and not isinstance(target, dict):
        raise ValueError(f"{context} target must be a mapping.")

    return action


def _normalize_action_list(
    value: Any,
    *,
    context: str,
) -> list[ActionConfig]:
    """Validate and copy an ordered action list."""
    if value is None:
        return []

    if not isinstance(value, list):
        raise ValueError(f"{context} must be a list of actions.")

    return [
        _normalize_action(
            action,
            context=f"{context} action {index}",
        )
        for index, action in enumerate(
            value,
            start=1,
        )
    ]


def _normalize_buttons(
    value: Any,
) -> dict[str, list[ActionConfig]]:
    """Validate a 4B button-to-action mapping."""
    if value is None:
        return {}

    if not isinstance(value, dict):
        raise ValueError("'buttons' must be a mapping of button names to action lists.")

    buttons: dict[str, list[ActionConfig]] = {}

    for raw_button, raw_actions in value.items():
        if not isinstance(raw_button, str):
            raise ValueError("Each 'buttons' key must be a string.")

        button = raw_button.strip()

        if button not in _VALID_4B_BUTTONS:
            valid_buttons = ", ".join(sorted(_VALID_4B_BUTTONS))

            raise ValueError(
                f"Unsupported 4B button {button!r}. Valid buttons are: {valid_buttons}."
            )

        actions = _normalize_action_list(
            raw_actions,
            context=f"buttons.{button}",
        )

        if not actions:
            raise ValueError(f"'buttons.{button}' must contain at least one action.")

        buttons[button] = actions

    return buttons


# ================================================================
# PLACEHOLDER EXPANSION
# ================================================================


def _expand_action_placeholders(
    actions: list[ActionConfig],
    placeholders: dict[str, list[str]],
    context: str = "middle_button",
) -> list[ActionConfig]:
    """
    Expand entity placeholders while preserving other target fields.

    Other target selectors remain unchanged.
    """
    rewritten: list[ActionConfig] = []

    for action_index, action in enumerate(
        actions,
        start=1,
    ):
        if not isinstance(action, dict):
            raise ValueError(f"{context} action {action_index} must be a mapping.")
        new_action = deepcopy(action)
        # Recurse only through script action containers. Service data,
        # templates and variable payloads may contain identical key names.
        for sequence_key in ("then", "else", "default", "sequence", "parallel"):
            if isinstance(new_action.get(sequence_key), (list, dict)):
                child = new_action[sequence_key]
                new_action[sequence_key] = _expand_action_placeholders(
                    child if isinstance(child, list) else [child], placeholders, context
                )
        if isinstance(new_action.get("repeat"), dict):
            repeat = new_action["repeat"]
            if isinstance(repeat.get("sequence"), (list, dict)):
                child = repeat["sequence"]
                repeat["sequence"] = _expand_action_placeholders(
                    child if isinstance(child, list) else [child], placeholders, context
                )
        if isinstance(new_action.get("choose"), list):
            for choice in new_action["choose"]:
                if isinstance(choice, dict) and isinstance(
                    choice.get("sequence"), (list, dict)
                ):
                    child = choice["sequence"]
                    choice["sequence"] = _expand_action_placeholders(
                        child if isinstance(child, list) else [child],
                        placeholders,
                        context,
                    )
        target = new_action.get("target")

        if not isinstance(target, dict):
            rewritten.append(new_action)
            continue

        entity_ids = target.get("entity_id")

        if entity_ids is None:
            rewritten.append(new_action)
            continue

        # An unassigned placeholder must not become a silent, empty target.
        for candidate in entity_ids if isinstance(entity_ids, list) else [entity_ids]:
            if (
                isinstance(candidate, str)
                and candidate in placeholders
                and not placeholders[candidate]
            ):
                raise ValueError(
                    f"{context} action {action_index}: placeholder {candidate!r} "
                    "has no assigned entities for this Pico. Use specific targets "
                    "or assign the matching group in Remote & targets."
                )

        if isinstance(entity_ids, str):
            expanded_entity_ids: str | list[str]

            if entity_ids in placeholders:
                expanded_entity_ids = list(placeholders[entity_ids])
            else:
                expanded_entity_ids = entity_ids

        elif isinstance(entity_ids, list):
            expanded: list[str] = []

            for entity_index, entity_id in enumerate(
                entity_ids,
                start=1,
            ):
                if not isinstance(entity_id, str):
                    raise ValueError(
                        f"{context} action {action_index} "
                        "target entity_id entry "
                        f"{entity_index} must be a string."
                    )

                if entity_id in placeholders:
                    expanded.extend(placeholders[entity_id])
                else:
                    expanded.append(entity_id)

            expanded_entity_ids = expanded

        else:
            raise ValueError(
                f"{context} action {action_index} target "
                "entity_id must be a string or list of strings."
            )

        new_target = dict(target)
        new_target["entity_id"] = expanded_entity_ids
        new_action["target"] = new_target

        rewritten.append(new_action)

    return rewritten


# ================================================================
# CONFIGURATION PARSER
# ================================================================


def parse_pico_config(
    hass: HomeAssistant,
    defaults: dict[str, Any],
    device_raw: dict[str, Any],
    *,
    from_ui: bool = False,
) -> PicoConfig:
    """Normalize and validate one Pico Link device configuration."""
    if not from_ui and any(
        "color_palette" in source
        or any(
            source.get(key) == CYCLE_ACTION
            for key in (*STOP_GESTURES, "middle_button")
        )
        for source in (defaults, device_raw)
    ):
        raise ValueError(
            "Configure native color cycling and palettes in the Pico Link UI. "
            "Existing YAML action sequences remain supported."
        )
    # An explicit type keeps its existing authority and validation. Only an
    # omitted key enables detection; an empty or invalid value is still an error.
    device_type = None
    if "type" in device_raw:
        raw_type = device_raw["type"]
        if not isinstance(raw_type, str) or not raw_type.strip():
            raise ValueError("'type' must be a non-empty string.")
        device_type = raw_type.strip().upper()

    # Stop gesture defaults, including the legacy tap name, require an opt-in.
    # Device-level keys still go through model and action validation below.
    merged = {
        key: value
        for key, value in defaults.items()
        if key != "middle_button" and key not in STOP_GESTURES
    }
    merged.update(device_raw)

    device_id = _resolve_device_id(
        hass,
        merged,
    )

    if device_type is None:
        device_type = _detect_pico_type(hass, device_id)

    mode = merged.get("mode", "single")
    if mode not in ("single", "restart", "queued", "parallel"):
        raise ValueError("mode must be single, restart, queued, or parallel.")
    max_runs = merged.get("max", 10)
    if isinstance(max_runs, bool) or not isinstance(max_runs, int) or max_runs < 1:
        raise ValueError("max must be a positive integer.")
    max_exceeded = merged.get("max_exceeded", "warning")
    if not isinstance(max_exceeded, str) or max_exceeded.lower() not in (
        "silent",
        "debug",
        "info",
        "warning",
        "error",
        "critical",
    ):
        raise ValueError("max_exceeded must be silent or a standard log level.")
    if "continue_on_error" in merged:
        raise ValueError(
            "continue_on_error belongs on an action, not defaults or a device."
        )

    # ------------------------------------------------------------
    # ENTITY LISTS
    # ------------------------------------------------------------

    covers = _normalize_entities(
        merged.get("covers"),
        key="covers",
        domain="cover",
    )

    fans = _normalize_entities(
        merged.get("fans"),
        key="fans",
        domain="fan",
    )

    lights = _normalize_entities(
        merged.get("lights"),
        key="lights",
        domain="light",
    )

    media_players = _normalize_entities(
        merged.get("media_players"),
        key="media_players",
        domain="media_player",
    )

    switches = _normalize_entities(
        merged.get("switches"),
        key="switches",
        domain="switch",
    )

    # ------------------------------------------------------------
    # TIMING AND DOMAIN OPTIONS
    # ------------------------------------------------------------

    hold_time_ms = _normalize_int(
        merged.get(
            "hold_time_ms",
            400,
        ),
        default=400,
        min_val=100,
        max_val=2000,
    )

    step_time_ms = _normalize_int(
        merged.get(
            "step_time_ms",
            650,
        ),
        default=650,
        min_val=100,
        max_val=2000,
    )

    double_tap_time_ms = _normalize_int(
        merged.get("double_tap_time_ms", 300),
        default=300,
        min_val=100,
        max_val=2000,
    )

    cover_open_pos = _normalize_int(
        merged.get(
            "cover_open_pos",
            100,
        ),
        default=100,
        min_val=1,
        max_val=100,
    )

    cover_step_pct = _normalize_int(
        merged.get(
            "cover_step_pct",
            10,
        ),
        default=10,
        min_val=1,
        max_val=25,
    )

    cover_inverted = _normalize_bool(
        merged.get(
            "cover_inverted",
            False,
        ),
        default=False,
    )

    fan_on_pct = _normalize_int(
        merged.get(
            "fan_on_pct",
            100,
        ),
        default=100,
        min_val=1,
        max_val=100,
    )

    light_on_pct = _normalize_int(
        merged.get(
            "light_on_pct",
            100,
        ),
        default=100,
        min_val=1,
        max_val=100,
    )

    light_low_pct = _normalize_int(
        merged.get(
            "light_low_pct",
            5,
        ),
        default=5,
        min_val=1,
        max_val=99,
    )

    light_step_pct = _normalize_int(
        merged.get(
            "light_step_pct",
            10,
        ),
        default=10,
        min_val=1,
        max_val=25,
    )

    light_transition_on = _normalize_int(
        merged.get(
            "light_transition_on",
            0,
        ),
        default=0,
        min_val=0,
        max_val=300,
    )

    light_transition_off = _normalize_int(
        merged.get(
            "light_transition_off",
            0,
        ),
        default=0,
        min_val=0,
        max_val=300,
    )

    media_player_vol_step = _normalize_int(
        merged.get(
            "media_player_vol_step",
            10,
        ),
        default=10,
        min_val=1,
        max_val=20,
    )

    # ------------------------------------------------------------
    # MIDDLE BUTTON
    # ------------------------------------------------------------

    raw_middle_button = device_raw.get("middle_button")
    cycle_gestures: set[str] = set()
    shared_palette = normalize_palette(defaults.get("color_palette", DEFAULT_PALETTE))
    raw_palette = device_raw.get("color_palette", "default")
    palette = (
        shared_palette if raw_palette == "default" else normalize_palette(raw_palette)
    )
    # Resolve the legacy alias to the same opt-in as stop_tap. Explicit stop_tap
    # still wins, including when it disables or replaces legacy cycling.
    middle_value = raw_middle_button
    if middle_value == "default":
        middle_value = defaults.get("stop_tap", defaults.get("middle_button", []))
    if middle_value == CYCLE_ACTION:
        raw_middle_button = None
        if "stop_tap" not in device_raw:
            merged["stop_tap"] = CYCLE_ACTION

    if device_type == "3BRL":
        if raw_middle_button == "default":
            tap_default_key = "stop_tap" if "stop_tap" in defaults else "middle_button"
            middle_button = _normalize_action_list(
                defaults.get(
                    tap_default_key,
                    [],
                ),
                context=f"defaults.{tap_default_key}",
            )
        elif raw_middle_button is None:
            middle_button = []
        else:
            middle_button = _normalize_action_list(
                raw_middle_button,
                context="middle_button",
            )
    else:
        if raw_middle_button not in (
            None,
            [],
        ):
            raise ValueError("'middle_button' is only valid for 3BRL Picos.")

        middle_button = []

    # ------------------------------------------------------------
    # 4B BUTTONS
    # ------------------------------------------------------------

    buttons = _normalize_buttons(
        merged.get("buttons"),
    )

    # The legacy tap name must also honor an explicitly selected empty shared
    # action instead of falling back to native shade, fan or media controls.
    overrides = (
        {"stop_tap": []} if raw_middle_button == "default" and not middle_button else {}
    )
    valid_buttons = PICO_BUTTONS.get(device_type, frozenset())
    for key, value in merged.items():
        if not isinstance(key, str):
            continue
        button = override_button(key)
        if button is None:
            continue
        if button not in valid_buttons:
            raise ValueError(
                f"'{key}' is not a supported button override for {device_type}."
            )
        if key in STOP_GESTURES and value == "default":
            default_key = key
            if key == "stop_tap" and key not in defaults:
                default_key = "middle_button"
            # An unspecified shared gesture means "Do nothing". This still
            # requires per-device opt-in; unconfigured Picos keep native behavior.
            value = defaults.get(default_key, [])
        if value == CYCLE_ACTION:
            if key not in STOP_GESTURES or device_type != "3BRL" or not lights:
                raise ValueError(
                    "color_cycle requires a 3BRL Stop gesture with assigned lights."
                )
            cycle_gestures.add(key)
            overrides[key] = []
            continue
        if not isinstance(value, list):
            raise ValueError(
                f"'{key}' must be a list of actions; use [] to disable it."
            )
        overrides[key] = _normalize_action_list(value, context=key)

    # ------------------------------------------------------------
    # BUILD CONFIGURATION
    # ------------------------------------------------------------

    pico_config = PicoConfig(
        device_id=device_id,
        type=device_type,
        mode=mode,
        max=max_runs,
        max_exceeded=max_exceeded.lower(),
        covers=covers,
        fans=fans,
        lights=lights,
        media_players=media_players,
        switches=switches,
        hold_time_ms=hold_time_ms,
        double_tap_time_ms=double_tap_time_ms,
        step_time_ms=step_time_ms,
        cover_open_pos=cover_open_pos,
        cover_step_pct=cover_step_pct,
        cover_inverted=cover_inverted,
        fan_on_pct=fan_on_pct,
        light_on_pct=light_on_pct,
        light_low_pct=light_low_pct,
        light_step_pct=light_step_pct,
        light_transition_on=light_transition_on,
        light_transition_off=light_transition_off,
        media_player_vol_step=media_player_vol_step,
        middle_button=middle_button,
        buttons=buttons,
        overrides=overrides,
        color_cycle_gestures=cycle_gestures,
        color_palette=palette,
    )

    placeholders = {
        "covers": pico_config.covers,
        "fans": pico_config.fans,
        "lights": pico_config.lights,
        "media_players": pico_config.media_players,
        "switches": pico_config.switches,
    }
    if light_placeholder := placeholder_entity_id(hass):
        if light_placeholder in pico_config.lights:
            raise ValueError(
                "Assign real lights in Remote & targets. "
                "Pico Link placeholder belongs only in action targets."
            )
        placeholders[light_placeholder] = pico_config.lights

    pico_config.middle_button = _expand_action_placeholders(
        pico_config.middle_button,
        placeholders,
    )

    pico_config.overrides = {
        key: _expand_action_placeholders(actions, placeholders, context=key)
        for key, actions in overrides.items()
    }

    pico_config.buttons = {
        key: _expand_action_placeholders(actions, placeholders, context=key)
        for key, actions in buttons.items()
    }
    for key, actions in {
        "middle_button": pico_config.middle_button,
        **pico_config.buttons,
        **pico_config.overrides,
    }.items():
        try:
            script_schema(actions)
        except (vol.Invalid, TypeError, ValueError) as err:
            raise ValueError(f"Invalid {key} script: {err}") from err

    pico_config.validate()

    return pico_config
