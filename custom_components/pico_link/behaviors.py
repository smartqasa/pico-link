from __future__ import annotations

import asyncio
import logging
from typing import Any, Dict, Optional

from homeassistant.core import CALLBACK_TYPE, HomeAssistant

from .config import PicoConfig
from .const import SUPPORTED_BUTTONS

_LOGGER = logging.getLogger(__name__)


class SharedBehaviors:
    """Mixin providing shared behaviors for all PicoController profiles."""

    def __init__(self, hass: HomeAssistant, conf: PicoConfig) -> None:
        self.hass = hass
        self.conf = conf

        self._pressed: Dict[str, bool] = {btn: False for btn in SUPPORTED_BUTTONS}

        self._tasks: Dict[str, Optional[asyncio.Task]] = {
            btn: None for btn in SUPPORTED_BUTTONS
        }

        self._last_press_ts: Dict[str, float] = {btn: 0.0 for btn in SUPPORTED_BUTTONS}
        self._unsub_event: Optional[CALLBACK_TYPE] = None

        self._hold_time = conf.hold_time_ms / 1000.0
        self._step_time = conf.step_time_ms / 1000.0

    # ---------------------------------------------------------
    # Determine DOMAIN based on the device configuration
    # (alphabetized priority)
    # ---------------------------------------------------------
    def _entity_domain(self) -> Optional[str]:
        """Return domain based on which entity list is populated."""
        if self.conf.covers:
            return "cover"
        if self.conf.fans:
            return "fan"
        if self.conf.lights:
            return "light"
        if self.conf.media_players:
            return "media_player"
        if self.conf.switches:
            return "switch"
        return None

    # ---------------------------------------------------------
    # PRIMARY ENTITY (first entity in the correct list)
    # ---------------------------------------------------------
    def _primary_entity(self) -> Optional[str]:
        if self.conf.covers:
            return self.conf.covers[0]
        if self.conf.fans:
            return self.conf.fans[0]
        if self.conf.lights:
            return self.conf.lights[0]
        if self.conf.media_players:
            return self.conf.media_players[0]
        if self.conf.switches:
            return self.conf.switches[0]
        return None

    # ---------------------------------------------------------
    # CENTRALIZED ENTITY STATE ACCESSOR
    # ---------------------------------------------------------
    def get_entity_state(self):
        """Return HA state for the primary entity (or None if unavailable)."""
        entity_id = self._primary_entity()
        if not entity_id:
            return None
        return self.hass.states.get(entity_id)

    # ---------------------------------------------------------------------
    # ON BEHAVIOR (alphabetized case order)
    # ---------------------------------------------------------------------
    async def _short_press_on(self) -> None:
        domain = self._entity_domain()
        entity_id = self._primary_entity()

        match domain:

            case "cover":
                if entity_id and self._cover_is_moving(entity_id):
                    await self._call_entity_service("stop_cover", {})
                    return

                supports_position = False
                if entity_id:
                    state = self.hass.states.get(entity_id)
                    supports_position = (
                        state is not None and "current_position" in state.attributes
                    )

                if supports_position:
                    try:
                        await self._call_entity_service(
                            "set_cover_position",
                            {"position": self.conf.on_pct},
                        )
                        return
                    except Exception:
                        pass

                await self._call_entity_service("open_cover", {})
                return

            case "fan":
                await self._call_entity_service(
                    "set_percentage",
                    {"percentage": self.conf.on_pct},
                )
                return

            case "light":
                await self._call_entity_service(
                    "turn_on",
                    {"brightness_pct": self.conf.on_pct},
                )
                return

            case "media_player":
                await self._media_play_pause()
                return

            case "switch":
                await self._call_entity_service("turn_on", {})
                return

            case _:
                _LOGGER.warning(
                    "Device %s: unsupported domain '%s' in _short_press_on()",
                    self.conf.device_id,
                    domain,
                )
                return

    # ---------------------------------------------------------------------
    # OFF BEHAVIOR (alphabetized case order)
    # ---------------------------------------------------------------------
    async def _short_press_off(self) -> None:
        domain = self._entity_domain()
        entity_id = self._primary_entity()

        match domain:

            case "cover":
                if entity_id and self._cover_is_moving(entity_id):
                    await self._call_entity_service("stop_cover", {})
                    return
                await self._call_entity_service("close_cover", {})
                return

            case "fan":
                await self._call_entity_service("turn_off", {})
                return

            case "light":
                await self._call_entity_service("turn_off", {})
                return

            case "media_player":
                await self._media_next()
                return

            case "switch":
                await self._call_entity_service("turn_off", {})
                return

            case _:
                _LOGGER.warning(
                    "Device %s: unsupported domain '%s' in _short_press_off()",
                    self.conf.device_id,
                    domain,
                )
                return

    # ---------------------------------------------------------------------
    # COVER MOVEMENT CHECK
    # ---------------------------------------------------------------------
    def _cover_is_moving(self, entity_id: str) -> bool:
        state = self.hass.states.get(entity_id)
        if not state:
            return False
        return state.state in ("opening", "closing")

    # =====================================================================
    #  UNIFIED RAMP LOGIC
    # =====================================================================
    async def _ramp(self, button: str, direction: int):
        entity_id = self._primary_entity()
        if not entity_id:
            return

        step_pct = self.conf.step_pct
        low_pct = self.conf.low_pct

        step_value = round(255 * (step_pct / 100))
        min_brightness = max(1, round(255 * (low_pct / 100)))
        max_brightness = 255

        state = self.hass.states.get(entity_id)
        if not state:
            return

        brightness = state.attributes.get("brightness")
        current_brightness = int(brightness) if brightness is not None else 0

        MAX_STEPS = 100
        steps = 0

        try:
            while self._pressed.get(button, False):

                if steps >= MAX_STEPS:
                    _LOGGER.error(
                        "RAMP SAFETY: Max steps reached (%s) for button '%s' on device %s",
                        MAX_STEPS,
                        button,
                        self.conf.device_id
                    )
                    return

                steps += 1

                next_b = current_brightness + (step_value * direction)

                if direction < 0 and next_b <= min_brightness:
                    await self._call_entity_service("turn_on", {"brightness": min_brightness}, continue_on_error=True)
                    return

                if direction > 0 and next_b >= max_brightness:
                    await self._call_entity_service("turn_on", {"brightness": max_brightness}, continue_on_error=True)
                    return

                await self._call_entity_service(
                    "turn_on",
                    {"brightness": next_b},
                    continue_on_error=True,
                )

                current_brightness = next_b
                await asyncio.sleep(self._step_time)

        except asyncio.CancelledError:
            return

    # ---------------------------------------------------------------------
    # MEDIA PLAYER BEHAVIORS
    # ---------------------------------------------------------------------
    async def _media_play_pause(self) -> None:
        await self._call_entity_service("media_play_pause", {})

    async def _media_next(self) -> None:
        await self._call_entity_service("media_next_track", {})

    async def _media_volume_step(self, direction: int) -> None:
        service = "volume_up" if direction > 0 else "volume_down"
        await self._call_entity_service(service, {})

    # ---------------------------------------------------------------------
    # FAN SPEED HELPERS
    # ---------------------------------------------------------------------
    def _get_fan_speed_ladder(self) -> list[int]:
        speeds = getattr(self.conf, "fan_speeds", 6) or 6
        if speeds not in (4, 6):
            speeds = 6
        steps = speeds - 1
        return [round(i * 100 / steps) for i in range(speeds)]

    def _get_current_fan_percentage(self) -> Optional[float]:
        entity_id = self._primary_entity()
        if not entity_id:
            return None

        state = self.hass.states.get(entity_id)
        if not state:
            return None

        pct = state.attributes.get("percentage")
        if pct is None:
            return 0.0 if state.state == "off" else float(self.conf.on_pct)

        try:
            return float(pct)
        except Exception:
            return None

    async def _fan_step_discrete(self, direction: int) -> None:
        entity_id = self._primary_entity()
        if not entity_id:
            return

        ladder = self._get_fan_speed_ladder()
        current_pct = self._get_current_fan_percentage()
        if current_pct is None:
            return

        current_index = min(
            range(len(ladder)),
            key=lambda i: abs(ladder[i] - current_pct),
        )
        target_index = max(
            0, min(len(ladder) - 1, current_index + direction)
        )

        target_pct = ladder[target_index]
        if target_pct == current_pct:
            return

        await self._call_entity_service(
            "set_percentage",
            {"percentage": target_pct},
        )

    # ---------------------------------------------------------------------
    # SHARED SERVICE CALLER
    # ---------------------------------------------------------------------
    async def _call_entity_service(
        self,
        service: str,
        data: Dict[str, Any],
        continue_on_error: bool = False,
    ) -> None:

        domain = self._entity_domain()
        if not domain:
            _LOGGER.error(
                "Device %s: cannot determine domain for service '%s'",
                self.conf.device_id,
                service,
            )
            return

        service_data = {**data}

        # Choose the correct entity list based on the domain
        match domain:
            case "cover":
                entity_list = self.conf.covers
            case "fan":
                entity_list = self.conf.fans
            case "light":
                entity_list = self.conf.lights
            case "media_player":
                entity_list = self.conf.media_players
            case "switch":
                entity_list = self.conf.switches
            case _:
                entity_list = []

        if entity_list:
            service_data["entity_id"] = entity_list

        try:
            await self.hass.services.async_call(
                domain,
                service,
                service_data,
                blocking=False,
            )
        except Exception as err:
            msg = (
                f"Device {self.conf.device_id}: error calling "
                f"{domain}.{service}({service_data}): {err}"
            )
            if continue_on_error:
                _LOGGER.debug(msg)
            else:
                _LOGGER.error(msg)


    # ---------------------------------------------------------------------
    # FOUR-BUTTON ACTION EXECUTOR (unchanged except no entities use)
    # ---------------------------------------------------------------------
    async def _execute_button_action(self, action: Dict[str, Any] | list) -> None:
        if isinstance(action, list):
            for a in action:
                await self._execute_button_action(a)
            return

        if not isinstance(action, dict):
            _LOGGER.error(
                "Device %s: invalid action format (expected dict or list): %s",
                self.conf.device_id,
                action,
            )
            return

        try:
            domain, service = action["action"].split(".", 1)
        except Exception as err:
            _LOGGER.error(
                "Device %s (four_button): invalid action '%s': %s",
                self.conf.device_id,
                action,
                err,
            )
            return

        target = action.get("target")
        data = action.get("data", {})

        try:
            await self.hass.services.async_call(
                domain,
                service,
                data,
                blocking=False,
                target=target,
            )
        except Exception as err:
            _LOGGER.error(
                "Device %s (four_button): error calling %s.%s: %s",
                self.conf.device_id,
                domain,
                service,
                err,
            )
