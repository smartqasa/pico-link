"""Opt-in light palettes and persistent positions, one per Pico and gesture."""

from __future__ import annotations

import asyncio
from copy import deepcopy
from typing import Any

from homeassistant.core import Context, HomeAssistant
from homeassistant.helpers.storage import Store

from .const import DOMAIN

CYCLE_ACTION = "color_cycle"
STORAGE_KEY = f"{DOMAIN}.color_cycles"
MAX_PALETTE_COLORS = 25
PALETTE_GESTURES = ("stop_tap", "stop_hold", "stop_double_tap")
DEFAULT_PALETTE = [
    {"color_temp_kelvin": 2800},
    {"color_temp_kelvin": 4000},
    {"rgb_color": [255, 0, 0]},
    {"rgb_color": [255, 0, 255]},
    {"rgb_color": [128, 0, 255]},
    {"rgb_color": [0, 0, 255]},
    {"rgb_color": [0, 255, 255]},
    {"rgb_color": [0, 255, 0]},
    {"rgb_color": [255, 191, 0]},
]


def normalize_palette(value: Any) -> list[dict[str, Any]]:
    """Accept an ordered list of RGB colors or white temperatures."""
    if not isinstance(value, list) or not 1 <= len(value) <= MAX_PALETTE_COLORS:
        raise ValueError(
            f"color_palette must contain between 1 and {MAX_PALETTE_COLORS} colors."
        )
    for color in value:
        if not isinstance(color, dict):
            raise ValueError("Each color_palette entry must be a color mapping.")
        if set(color) == {"rgb_color"}:
            rgb = color["rgb_color"]
            valid = (
                isinstance(rgb, list)
                and len(rgb) == 3
                and all(type(v) is int and 0 <= v <= 255 for v in rgb)
            )
        elif set(color) == {"color_temp_kelvin"}:
            kelvin = color["color_temp_kelvin"]
            valid = type(kelvin) is int and 1000 <= kelvin <= 10000
        else:
            valid = False
        if not valid:
            raise ValueError(
                "Each color_palette entry needs only rgb_color (three integers "
                "from 0 to 255) or color_temp_kelvin (1000 to 10000)."
            )
    return deepcopy(value)


def palette_choices(raw: dict) -> dict[str, Any]:
    """Validate independent gesture choices, retaining early beta custom colors."""
    choices = raw.get("color_palettes", {})
    if not isinstance(choices, dict) or set(choices) - set(PALETTE_GESTURES):
        raise ValueError(
            "color_palettes must map Stop tap, hold, or double tap to palettes."
        )
    common = raw.get("color_palette", "default")
    if common != "default":
        common = normalize_palette(common)
    return {
        key: "default"
        if (value := choices.get(key, common)) == "default"
        else normalize_palette(value)
        for key in PALETTE_GESTURES
    }


def resolve_palettes(defaults: dict, raw: dict) -> dict[str, list[dict[str, Any]]]:
    """The gesture's behavior is the only choice of shared versus local colors."""
    shared = palette_choices(defaults)
    local = palette_choices(raw)
    return {
        key: deepcopy(
            local[key]
            if local[key] != "default"
            and raw.get(key, raw.get("middle_button") if key == "stop_tap" else None)
            != "default"
            else shared[key]
            if shared[key] != "default"
            else DEFAULT_PALETTE
        )
        for key in PALETTE_GESTURES
    }


def migrate_palette_document(root: Any) -> Any:
    """Retain old colors and freeze local cycles without editing saved data in place."""
    copied = deepcopy(root)
    if not isinstance(copied, dict):
        return copied
    devices = copied.get("devices", [])
    for raw in [
        copied.get("defaults"),
        *(devices if isinstance(devices, list) else []),
    ]:
        if not isinstance(raw, dict) or "color_palette" not in raw:
            continue
        common = raw["color_palette"]
        if not (isinstance(common, list) or common == "default"):
            continue  # Leave invalid values visible to normal validation.
        choices = raw.setdefault("color_palettes", {})
        if not isinstance(choices, dict):
            continue
        for key in PALETTE_GESTURES:
            choices.setdefault(key, deepcopy(common))
        del raw["color_palette"]
    defaults = copied.get("defaults") or {}
    if isinstance(devices, list) and isinstance(defaults, dict):
        shared = defaults.get("color_palettes", {})
        if not isinstance(shared, dict):
            return copied  # Normal validation reports malformed settings.
        for raw in devices:
            if not isinstance(raw, dict):
                continue
            for key in PALETTE_GESTURES:
                value = raw.get(
                    key, raw.get("middle_button") if key == "stop_tap" else None
                )
                if value != CYCLE_ACTION:
                    continue
                choices = raw.setdefault("color_palettes", {})
                if (
                    isinstance(choices, dict)
                    and choices.get(key, "default") == "default"
                ):
                    colors = shared.get(key, "default")
                    choices[key] = deepcopy(
                        DEFAULT_PALETTE if colors == "default" else colors
                    )
    return copied


class _PositionStore(Store):
    async def _async_migrate_func(self, old_major_version, old_minor_version, old_data):
        if old_major_version != 1:
            raise NotImplementedError
        if not isinstance(old_data, dict):
            return {}
        return {
            device_id: {key: deepcopy(position) for key in PALETTE_GESTURES}
            for device_id, position in old_data.items()
        }


class ColorCycleStore:
    """Keep runtime positions out of settings and serialize only each Pico's calls."""

    def __init__(self, hass: HomeAssistant) -> None:
        self.hass = hass
        self.store = _PositionStore(hass, 2, STORAGE_KEY)
        self.positions: dict[str, dict[str, dict[str, Any]]] = {}
        self._load_lock = asyncio.Lock()
        self._loaded = False
        self._locks: dict[str, asyncio.Lock] = {}

    async def async_load(self) -> None:
        async with self._load_lock:
            if self._loaded:
                return
            saved = await self.store.async_load()
            if isinstance(saved, dict):
                for device_id, gestures in saved.items():
                    if not isinstance(device_id, str) or not isinstance(gestures, dict):
                        continue
                    for key in PALETTE_GESTURES:
                        position = gestures.get(key)
                        if not isinstance(position, dict):
                            continue
                        index = position.get("index")
                        try:
                            color = normalize_palette([position.get("color")])[0]
                        except ValueError:
                            continue
                        if type(index) is int and index >= 0:
                            self.positions.setdefault(device_id, {})[key] = {
                                "index": index,
                                "color": color,
                            }
            self._loaded = True

    def _save(self) -> None:
        # HA coalesces rapid presses and flushes pending data on clean shutdown.
        # Capture a snapshot because HA may serialize in a worker thread.
        snapshot = deepcopy(self.positions)
        self.store.async_delay_save(lambda: snapshot, 1)

    def reconcile(
        self, device_id: str, gesture: str, palette: list[dict[str, Any]]
    ) -> None:
        """Preserve the last selected color across edits, or reset to the start."""
        previous = self.positions.get(device_id, {}).get(gesture)
        if previous is None:
            return
        index, color = previous["index"], previous["color"]
        if index < len(palette) and palette[index] == color:
            return
        if color in palette:
            self.positions[device_id][gesture] = {
                "index": palette.index(color),
                "color": color,
            }
        else:
            del self.positions[device_id][gesture]
            if not self.positions[device_id]:
                del self.positions[device_id]
        self._save()

    async def async_cycle(
        self,
        device_id: str,
        gesture: str,
        lights: list[str],
        palette: list[dict[str, Any]],
    ) -> None:
        """Choose from our own position, never from the lights' current state."""
        async with self._locks.setdefault(device_id, asyncio.Lock()):
            self.reconcile(device_id, gesture, palette)
            previous = self.positions.get(device_id, {}).get(gesture)
            index = (previous["index"] + 1) % len(palette) if previous else 0
            color = palette[index]
            await self.hass.services.async_call(
                "light",
                "turn_on",
                {**deepcopy(color), "entity_id": list(lights)},
                blocking=True,
                context=Context(),
            )
            # Failed or cancelled calls do not consume a color.
            self.positions.setdefault(device_id, {})[gesture] = {
                "index": index,
                "color": deepcopy(color),
            }
            self._save()


def get_cycle_store(hass: HomeAssistant) -> ColorCycleStore:
    """Reuse storage and positions when UI saves replace the controllers."""
    runtime = hass.data.setdefault(DOMAIN, {})
    if "color_cycles" not in runtime:
        runtime["color_cycles"] = ColorCycleStore(hass)
    return runtime["color_cycles"]
