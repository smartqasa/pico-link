"""Opt-in light palettes and restart-persistent positions, one per Pico."""

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
LEGACY_MAX_PALETTE_COLORS = 32
DEFAULT_PALETTE = [
    {"color_temp_kelvin": 2800},
    {"color_temp_kelvin": 4000},
    {"rgb_color": [255, 0, 0]},
    {"rgb_color": [255, 0, 255]},
    {"rgb_color": [0, 0, 255]},
    {"rgb_color": [0, 255, 255]},
    {"rgb_color": [0, 255, 0]},
]


def normalize_palette(
    value: Any, *, max_colors: int = MAX_PALETTE_COLORS
) -> list[dict[str, Any]]:
    """Accept an ordered list of RGB colors or white temperatures."""
    if not isinstance(value, list) or not 1 <= len(value) <= max_colors:
        raise ValueError(
            f"color_palette must contain between 1 and {max_colors} colors."
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


class ColorCycleStore:
    """Keep runtime positions out of settings and serialize only each Pico's calls."""

    def __init__(self, hass: HomeAssistant) -> None:
        self.hass = hass
        self.store = Store(hass, 1, STORAGE_KEY)
        self.positions: dict[str, dict[str, Any]] = {}
        self._load_lock = asyncio.Lock()
        self._loaded = False
        self._locks: dict[str, asyncio.Lock] = {}

    async def async_load(self) -> None:
        async with self._load_lock:
            if self._loaded:
                return
            saved = await self.store.async_load()
            if isinstance(saved, dict):
                for device_id, position in saved.items():
                    if not isinstance(position, dict):
                        continue
                    index = position.get("index")
                    try:
                        color = normalize_palette([position.get("color")])[0]
                    except ValueError:
                        continue
                    if isinstance(device_id, str) and type(index) is int and index >= 0:
                        self.positions[device_id] = {"index": index, "color": color}
            self._loaded = True

    def _save(self) -> None:
        # HA coalesces rapid presses and flushes pending data on clean shutdown.
        # Capture a snapshot because HA may serialize in a worker thread.
        snapshot = deepcopy(self.positions)
        self.store.async_delay_save(lambda: snapshot, 1)

    def reconcile(self, device_id: str, palette: list[dict[str, Any]]) -> None:
        """Preserve the last selected color across edits, or reset to the start."""
        previous = self.positions.get(device_id)
        if previous is None:
            return
        index, color = previous["index"], previous["color"]
        if index < len(palette) and palette[index] == color:
            return
        if color in palette:
            self.positions[device_id] = {"index": palette.index(color), "color": color}
        else:
            del self.positions[device_id]
        self._save()

    async def async_cycle(
        self, device_id: str, lights: list[str], palette: list[dict[str, Any]]
    ) -> None:
        """Choose from our own position, never from the lights' current state."""
        async with self._locks.setdefault(device_id, asyncio.Lock()):
            self.reconcile(device_id, palette)
            previous = self.positions.get(device_id)
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
            self.positions[device_id] = {"index": index, "color": deepcopy(color)}
            self._save()


def get_cycle_store(hass: HomeAssistant) -> ColorCycleStore:
    """Reuse storage and positions when UI saves replace the controllers."""
    runtime = hass.data.setdefault(DOMAIN, {})
    if "color_cycles" not in runtime:
        runtime["color_cycles"] = ColorCycleStore(hass)
    return runtime["color_cycles"]
