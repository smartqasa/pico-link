"""Native Home Assistant setup and settings editor for Pico Link."""

from __future__ import annotations

from collections import Counter
from copy import deepcopy
from functools import partial

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers import selector

from .config import PICO_BUTTONS, override_button
from .const import DOMAIN, DOMAIN_ENTITY_FIELDS
from .ui_config import (
    DEVICE_SETTINGS,
    LOG_LEVELS,
    MODES,
    NUMBERS,
    TIMING,
    entry_config,
    import_document,
    remote_name,
    remote_type,
    validate_actions,
    validate_document,
)

GESTURES = ("tap", "hold", "double_tap")
BUTTON_ORDER = (
    "on",
    "raise",
    "stop",
    "lower",
    "button_1",
    "button_2",
    "button_3",
    "off",
)
ERRORS = (ValueError, TypeError, vol.Invalid, HomeAssistantError)


def select(options):
    labels = {
        "automatic": "Automatic",
        "P2B": "Paddle Pico (P2B)",
        "2B": "Two-button Pico (2B)",
        "3BRL": "Five-button Pico (3BRL)",
        "4B": "Four-button scene Pico (4B)",
        "normal": "Normal / inherited behavior",
        "custom": "Custom actions",
        "disabled": "Do nothing",
        "shared": "Use shared Stop action",
        "inherit": "Use default",
        "single": "Single — ignore while busy",
        "restart": "Restart — newest command takes over",
        "queued": "Queued — run in order",
        "parallel": "Parallel — run together",
        "stop": "Stop / middle",
        "cover": "Shades / covers",
        "light": "Lights",
        "fan": "Fans",
        "switch": "Switches",
        "media_player": "Media players",
    }
    return selector.SelectSelector(
        {
            "options": [
                {
                    "value": option,
                    "label": labels.get(option, option.replace("_", " ").capitalize()),
                }
                if isinstance(option, str)
                else option
                for option in options
            ],
            "mode": "dropdown",
        }
    )


def suggested(key, data):
    return vol.Optional(key, description={"suggested_value": data.get(key)})


class Editor:
    """Edit a private draft; only Save changes writes to HA storage."""

    def _init_editor(self, root=None):
        self._draft = deepcopy(root or {"defaults": {}, "devices": []})
        self._draft["defaults"] = self._draft.get("defaults") or {}
        self._remote = None
        self._index = None
        self._shared = False
        self._gesture = "stop_tap"
        self._error = ""
        self._pico_steps = []

    def _form(self, step, fields=None, errors=None, **placeholders):
        return self.async_show_form(
            step_id=step,
            data_schema=vol.Schema(fields or {}),
            errors=errors or {},
            description_placeholders={"detail": self._error, **placeholders},
        )

    def _menu(self, step, options, **placeholders):
        return self.async_show_menu(
            step_id=step,
            menu_options=options,
            description_placeholders=placeholders,
        )

    async def async_step_editor(self, user_input=None):
        # A labelled HA menu gives every remote its own clickable row. Register
        # handlers only for the current draft; the flow's schema validates the
        # selected row before dispatch. No configuration migration is needed.
        for step in self._pico_steps:
            delattr(self, f"async_step_{step}")
        self._pico_steps = []
        options = {
            "add": "Add Pico",
            "defaults": "Shared defaults",
            "save": "Save changes",
        }
        names = [remote_name(self.hass, raw) for raw in self._draft["devices"]]
        counts = Counter(names)
        for index in sorted(range(len(names)), key=lambda i: (names[i].casefold(), i)):
            step = f"pico_{index}"
            label = names[index]
            if counts[label] > 1:
                label = (
                    f"{label} ({names[: index + 1].count(label)} of {counts[label]})"
                )
            options[step] = label
            setattr(self, f"async_step_{step}", partial(self._async_open_pico, index))
            self._pico_steps.append(step)
        return self._menu("editor", options, count=str(len(names)))

    async def _async_open_pico(self, index, user_input=None):
        self._index = index
        self._remote = deepcopy(self._draft["devices"][index])
        return await self.async_step_remote()

    async def async_step_add(self, user_input=None):
        errors = {}
        if user_input is not None:
            raw = {"device_id": user_input["device_id"]}
            if user_input["type"] != "automatic":
                raw["type"] = user_input["type"]
            try:
                remote_type(self.hass, raw)
                if any(
                    d.get("device_id") == raw["device_id"]
                    for d in self._draft["devices"]
                ):
                    raise ValueError("This Pico is already configured.")
            except ERRORS as err:
                self._error = str(err)
                errors["base"] = "invalid_config"
            else:
                self._remote = raw
                self._index = None
                return await self.async_step_assignment()
        return self._form(
            "add",
            {
                vol.Required("device_id"): selector.DeviceSelector(
                    {"integration": "lutron_caseta"}
                ),
                vol.Required("type", default="automatic"): select(
                    ["automatic", "P2B", "2B", "3BRL", "4B"]
                ),
            },
            errors,
        )

    async def async_step_confirm_remove(self, user_input=None):
        if user_input is not None:
            self._draft["devices"].pop(self._index)
            self._index = None
            self._remote = None
            return await self.async_step_editor()
        return self._form(
            "confirm_remove",
            remote=remote_name(self.hass, self._draft["devices"][self._index]),
        )

    def _kind(self):
        return remote_type(self.hass, self._remote)

    def _domain(self):
        merged = {**self._draft["defaults"], **self._remote}
        return next(
            (
                domain
                for domain, field in DOMAIN_ENTITY_FIELDS.items()
                if merged.get(field)
            ),
            "light",
        )

    async def async_step_remote(self, user_input=None):
        self._shared = False
        try:
            kind = self._kind()
        except ERRORS:
            options = ["identity", "discard_remote"]
            if self._index is not None:
                options.append("confirm_remove")
            return self._menu(
                "remote",
                options,
                remote=remote_name(self.hass, self._remote),
                model="Unavailable or unrecognized — choose a remote and layout to repair",
            )
        options = ["identity", "button", "timing", "run"]
        if kind != "4B":
            options.insert(1, "assignment")
        if kind != "4B" and self._domain() != "switch":
            options.append("device_settings")
        options += ["done", "discard_remote"]
        if self._index is not None:
            options.append("confirm_remove")
        return self._menu(
            "remote",
            options,
            remote=remote_name(self.hass, self._remote),
            model=self._kind(),
        )

    async def async_step_identity(self, user_input=None):
        errors = {}
        if user_input is not None:
            candidate = deepcopy(self._remote)
            candidate["device_id"] = user_input["device_id"]
            candidate.pop("type", None)
            if user_input["type"] != "automatic":
                candidate["type"] = user_input["type"]
            try:
                kind = remote_type(self.hass, candidate)
                unsupported = [
                    key
                    for key in candidate
                    if (button := override_button(key)) is not None
                    and button not in PICO_BUTTONS[kind]
                ]
                if kind != "3BRL" and "middle_button" in candidate:
                    unsupported.append("middle_button")
                if kind != "4B" and candidate.get("buttons"):
                    unsupported.append("buttons")
                if unsupported:
                    raise ValueError(
                        "Remove actions for buttons absent from the new layout first: "
                        + ", ".join(unsupported)
                        + ". Alternatively, remove this Pico and add it again."
                    )
                if any(
                    i != self._index and raw.get("device_id") == candidate["device_id"]
                    for i, raw in enumerate(self._draft["devices"])
                ):
                    raise ValueError("This Pico is already configured.")
            except ERRORS as err:
                self._error = str(err)
                errors["base"] = "invalid_config"
            else:
                self._remote = candidate
                return await self.async_step_remote()
        return self._form(
            "identity",
            {
                vol.Required(
                    "device_id", default=self._remote.get("device_id", "")
                ): selector.DeviceSelector({"integration": "lutron_caseta"}),
                vol.Required(
                    "type", default=self._remote.get("type", "automatic")
                ): select(["automatic", "P2B", "2B", "3BRL", "4B"]),
            },
            errors,
        )

    async def async_step_assignment(self, user_input=None):
        if self._kind() == "4B":
            return await self.async_step_remote()
        if user_input is not None:
            self._selected_domain = user_input["domain"]
            return await self.async_step_entities()
        return self._form(
            "assignment",
            {
                vol.Required("domain", default=self._domain()): select(
                    DOMAIN_ENTITY_FIELDS
                ),
            },
        )

    async def async_step_entities(self, user_input=None):
        domain = self._selected_domain
        field = DOMAIN_ENTITY_FIELDS[domain]
        if user_input is not None:
            if not user_input.get("entities"):
                return self._form(
                    "entities",
                    {
                        vol.Required("entities"): selector.EntitySelector(
                            {"domain": domain, "multiple": True}
                        )
                    },
                    {"base": "entities_required"},
                )
            # Explicit empty lists mask any imported shared entity assignments.
            for key in DOMAIN_ENTITY_FIELDS.values():
                self._remote[key] = []
            self._remote[field] = user_input["entities"]
            return await self.async_step_remote()
        current = self._remote.get(field, self._draft["defaults"].get(field, []))
        if isinstance(current, str):
            current = [current]
        return self._form(
            "entities",
            {
                vol.Required("entities", default=current): selector.EntitySelector(
                    {"domain": domain, "multiple": True}
                ),
            },
        )

    async def async_step_button(self, user_input=None):
        if user_input is not None:
            self._gesture = f"{user_input['button']}_{user_input['gesture']}"
            return await self.async_step_behavior()
        return self._form(
            "button",
            {
                vol.Required("button"): select(
                    [b for b in BUTTON_ORDER if b in PICO_BUTTONS[self._kind()]]
                ),
                vol.Required("gesture", default="tap"): select(GESTURES),
            },
        )

    def _gesture_value(self):
        if self._gesture in self._remote:
            return self._remote[self._gesture]
        if self._gesture == "stop_tap":
            return self._remote.get("middle_button")
        if self._gesture.endswith("_tap") and not self._gesture.endswith("_double_tap"):
            return self._remote.get("buttons", {}).get(self._gesture[:-4])
        return None

    def _clear_gesture(self):
        self._remote.pop(self._gesture, None)
        if self._gesture == "stop_tap":
            self._remote.pop("middle_button", None)
        if self._gesture.endswith("_tap") and not self._gesture.endswith("_double_tap"):
            buttons = self._remote.get("buttons", {})
            buttons.pop(self._gesture[:-4], None)
            if not buttons:
                self._remote.pop("buttons", None)

    async def async_step_behavior(self, user_input=None):
        value = self._gesture_value()
        choices = ["normal", "custom", "disabled"]
        if self._gesture.startswith("stop_"):
            choices.append("shared")
        if user_input is not None:
            behavior = user_input["behavior"]
            if behavior == "custom":
                return await self.async_step_actions()
            self._clear_gesture()
            if behavior != "normal":
                self._remote[self._gesture] = "default" if behavior == "shared" else []
            return await self.async_step_remote()
        selected = (
            "normal"
            if value is None
            else "shared"
            if value == "default"
            else "custom"
            if value
            else "disabled"
        )
        return self._form(
            "behavior",
            {
                vol.Required("behavior", default=selected): select(choices),
            },
            gesture=self._gesture.replace("_", " "),
        )

    async def async_step_actions(self, user_input=None):
        errors = {}
        actions = (
            self._gesture_value()
            if not self._shared
            else self._draft["defaults"].get(
                self._gesture,
                self._draft["defaults"].get("middle_button", [])
                if self._gesture == "stop_tap"
                else [],
            )
        )
        if not isinstance(actions, list):
            actions = []
        if user_input is not None:
            actions = user_input.get("actions", [])
            try:
                await validate_actions(self.hass, actions)
            except ERRORS as err:
                self._error = str(err)
                errors["base"] = "invalid_config"
            else:
                if self._shared:
                    self._draft["defaults"][self._gesture] = deepcopy(actions)
                    return await self.async_step_defaults()
                self._clear_gesture()
                self._remote[self._gesture] = deepcopy(actions)
                return await self.async_step_remote()
        return self._form(
            "actions",
            {
                vol.Required("actions", default=actions): selector.ActionSelector(),
            },
            errors,
            gesture=self._gesture.replace("_", " "),
        )

    async def async_step_done(self, user_input=None):
        try:
            root = deepcopy(self._draft)
            if self._index is None:
                root["devices"].append(self._remote)
            else:
                root["devices"][self._index] = self._remote
            # Other remotes can be repaired in a later editor step. The final
            # Save validates the complete document, including duplicates.
            await validate_document(
                self.hass, {"defaults": root["defaults"], "devices": [self._remote]}
            )
        except ERRORS as err:
            self._error = str(err)
            if user_input is not None:
                return await self.async_step_remote()
            return self._form("done", errors={"base": "invalid_config"})
        self._draft = deepcopy(root)
        self._remote = None
        self._index = None
        return await self.async_step_editor()

    async def async_step_discard_remote(self, user_input=None):
        self._remote = None
        self._index = None
        return await self.async_step_editor()

    async def async_step_defaults(self, user_input=None):
        self._shared = True
        return self._menu(
            "defaults", ["timing", "shared_settings", "run", "shared_stop", "editor"]
        )

    async def async_step_shared_stop(self, user_input=None):
        if user_input is not None:
            self._gesture = f"stop_{user_input['gesture']}"
            return await self.async_step_actions()
        return self._form(
            "shared_stop", {vol.Required("gesture", default="tap"): select(GESTURES)}
        )

    def _settings_target(self):
        return self._draft["defaults"] if self._shared else self._remote

    async def _settings_back(self):
        return await (
            self.async_step_defaults() if self._shared else self.async_step_remote()
        )

    async def _numbers(self, step, keys, user_input, cover=False):
        target = self._settings_target()
        if user_input is not None:
            for key in keys:
                target.pop(key, None)
                if key in user_input:
                    target[key] = int(user_input[key])
            if cover:
                target.pop("cover_inverted", None)
                if user_input.get("cover_inverted", "inherit") != "inherit":
                    target["cover_inverted"] = user_input["cover_inverted"] == "yes"
            return await self._settings_back()
        fields = {}
        effective = []
        for key in keys:
            minimum, maximum, fallback, unit = NUMBERS[key]
            fields[suggested(key, target)] = selector.NumberSelector(
                {
                    "min": minimum,
                    "max": maximum,
                    "step": 1,
                    "mode": "box",
                    "unit_of_measurement": unit,
                }
            )
            inherited = (
                self._draft["defaults"].get(key, fallback)
                if not self._shared
                else fallback
            )
            effective.append(
                f"{key.replace('_', ' ').capitalize()}: {inherited} {unit}"
            )
        if cover:
            value = target.get("cover_inverted")
            fields[
                vol.Required(
                    "cover_inverted",
                    default="inherit" if value is None else "yes" if value else "no",
                )
            ] = select(["inherit", "yes", "no"])
        return self._form(step, fields, inherited="; ".join(effective))

    async def async_step_timing(self, user_input=None):
        return await self._numbers("timing", TIMING, user_input)

    async def async_step_device_settings(self, user_input=None):
        domain = self._domain()
        return await self._numbers(
            "device_settings",
            DEVICE_SETTINGS[domain],
            user_input,
            cover=domain == "cover",
        )

    async def async_step_shared_settings(self, user_input=None):
        return await self._numbers(
            "shared_settings",
            [k for k in NUMBERS if k not in TIMING],
            user_input,
            cover=True,
        )

    async def async_step_run(self, user_input=None):
        target = self._settings_target()
        errors = {}
        if user_input is not None:
            if "max" in user_input and (
                isinstance(user_input["max"], bool)
                or user_input["max"] < 1
                or int(user_input["max"]) != user_input["max"]
            ):
                errors["max"] = "positive_integer"
            else:
                for key in ("mode", "max", "max_exceeded"):
                    target.pop(key, None)
                    if key in user_input and user_input[key] != "inherit":
                        target[key] = (
                            int(user_input[key]) if key == "max" else user_input[key]
                        )
                return await self._settings_back()
        inherited = {} if self._shared else self._draft["defaults"]
        return self._form(
            "run",
            {
                vol.Required("mode", default=target.get("mode", "inherit")): select(
                    ["inherit", *MODES]
                ),
                suggested("max", target): selector.NumberSelector(
                    {"min": 1, "step": 1, "mode": "box"}
                ),
                vol.Required(
                    "max_exceeded",
                    default=target.get("max_exceeded", "inherit").lower(),
                ): select(["inherit", *LOG_LEVELS]),
            },
            errors,
            inherited=f"{inherited.get('mode', 'single')}; limit {inherited.get('max', 10)}; {inherited.get('max_exceeded', 'warning')}",
        )

    async def async_step_save(self, user_input=None):
        errors = {}
        self._error = ""
        try:
            await validate_document(self.hass, self._draft)
        except ERRORS as err:
            self._error = str(err)
            errors["base"] = "invalid_config"
        if user_input is not None:
            if errors:
                return await self.async_step_editor()
            self._draft["config_method"] = "ui"
            return self.async_create_entry(
                title="Pico Link", data=deepcopy(self._draft)
            )
        return self._form("save", errors=errors, count=str(len(self._draft["devices"])))


class PicoLinkConfigFlow(Editor, config_entries.ConfigFlow, domain=DOMAIN):
    """Opt-in native configuration; existing YAML remains active until import."""

    VERSION = 1

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return PicoLinkOptionsFlow(config_entry)

    async def async_step_user(self, user_input=None):
        await self.async_set_unique_id(DOMAIN)
        self._abort_if_unique_id_configured()
        self._init_editor()
        if self.hass.data.get(DOMAIN, {}).get("config_method") == "yaml":
            return self.async_abort(reason="yaml_selected")
        return await self.async_step_method(user_input)

    async def async_step_method(self, user_input=None):
        if user_input is None:
            return self._form(
                "method",
                {
                    vol.Required("config_method", default="ui"): select(
                        [
                            {
                                "value": "ui",
                                "label": "UI — configure in Home Assistant",
                            },
                            {"value": "yaml", "label": "YAML — configure in a file"},
                        ]
                    )
                },
            )
        if user_input["config_method"] == "yaml":
            return self.async_abort(reason="yaml_selected")
        yaml = self.hass.data.get(DOMAIN, {}).get("yaml_config")
        if isinstance(yaml, dict) and ("devices" in yaml or "defaults" in yaml):
            return await self.async_step_import_yaml()
        return await self.async_step_editor()

    async def async_step_import_yaml(self, user_input=None):
        errors = {}
        if user_input is not None:
            try:
                source = deepcopy(self.hass.data[DOMAIN]["yaml_config"])
                source.setdefault("devices", [])
                self._draft = await import_document(self.hass, source)
            except ERRORS as err:
                self._error = str(err)
                errors["base"] = "invalid_config"
            else:
                return await self.async_step_editor()
        return self._form("import_yaml", errors=errors)


class PicoLinkOptionsFlow(Editor, config_entries.OptionsFlow):
    """Manage a complete private copy, then reload on successful save."""

    def __init__(self, entry):
        self._entry = entry

    async def async_step_init(self, user_input=None):
        if self.hass.data.get(DOMAIN, {}).get("config_method") == "yaml":
            return self.async_abort(reason="yaml_selected")
        self._init_editor(entry_config(self._entry))
        return await self.async_step_editor()
