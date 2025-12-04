from __future__ import annotations

import asyncio
import logging
from typing import Any, Dict, Mapping, Optional, Tuple

from homeassistant.core import CALLBACK_TYPE, Event, HomeAssistant, callback

from .config import PicoConfig
from .const import (
    PROFILE_FIVE_BUTTON,
    PROFILE_FOUR_BUTTON,
    PROFILE_PADDLE,
    PROFILE_TWO_BUTTON,
    SUPPORTED_BUTTONS,
    PICO_EVENT_TYPE,
)

_LOGGER = logging.getLogger(__name__)


class PicoController:
    """Implements press/hold/ramp behavior for a single Pico remote."""

    def __init__(self, hass: HomeAssistant, conf: PicoConfig) -> None:
        self.hass = hass
        self.conf = conf

        # Press state per logical button
        self._pressed: Dict[str, bool] = {btn: False for btn in SUPPORTED_BUTTONS}

        # Task per button to implement lifecycle / ramp
        self._tasks: Dict[str, Optional[asyncio.Task]] = {
            btn: None for btn in SUPPORTED_BUTTONS
        }

        # For future features
        self._last_press_ts: Dict[str, float] = {btn: 0.0 for btn in SUPPORTED_BUTTONS}

        # Unsubscribe callback from hass.bus.async_listen
        self._unsub_event: Optional[CALLBACK_TYPE] = None

        # Convert ms → seconds
        self._hold_time = conf.hold_time_ms / 1000.0
        self._step_time = conf.step_time_ms / 1000.0

    async def async_start(self) -> None:
        """Start listening for Pico button events."""

        @callback
        def _handle_event(event: Event) -> None:
            data = event.data

            if data.get("device_id") != self.conf.device_id:
                return

            button, action = self._map_event_payload(data)
            if button is None or action is None:
                return

            if button not in SUPPORTED_BUTTONS:
                _LOGGER.debug(
                    "Device %s: ignoring unsupported button '%s'",
                    self.conf.device_id,
                    button,
                )
                return

            # Route to profile handlers
            if self.conf.profile == PROFILE_PADDLE:
                self._handle_paddle_event(button, action)

            elif self.conf.profile == PROFILE_FIVE_BUTTON:
                self._handle_five_button_event(button, action)

            elif self.conf.profile == PROFILE_TWO_BUTTON:
                self._handle_two_button_event(button, action)

            elif self.conf.profile == PROFILE_FOUR_BUTTON:
                self._handle_four_button_event(button, action)

        self._unsub_event = self.hass.bus.async_listen(PICO_EVENT_TYPE, _handle_event)

        _LOGGER.info(
            "PicoController started for device %s (profile=%s, domain=%s)",
            self.conf.device_id,
            self.conf.profile,
            getattr(self.conf, "domain", None),
        )

    def async_stop(self) -> None:
        """Stop listening and cancel tasks."""
        if self._unsub_event:
            self._unsub_event()
            self._unsub_event = None

        for button in SUPPORTED_BUTTONS:
            task = self._tasks.get(button)
            if task and not task.done():
                task.cancel()
            self._tasks[button] = None

        self._pressed = {btn: False for btn in SUPPORTED_BUTTONS}

    # ---------------------------------------------------------------------
    # Event payload mapping
    # ---------------------------------------------------------------------

    def _map_event_payload(
        self,
        data: Mapping[str, Any],
    ) -> Tuple[Optional[str], Optional[str]]:
        """Translate lutron_caseta event payload into (button, action)."""
        button = data.get("button_type")
        action = data.get("action")

        if not button or not action:
            return None, None

        button = str(button).lower()
        action = str(action).lower()

        if action not in ("press", "release"):
            return None, None

        return button, action

    # ---------------------------------------------------------------------
    # Paddle profile
    # ---------------------------------------------------------------------

    def _handle_paddle_event(self, button: str, action: str) -> None:
        if button not in ("on", "off"):
            return

        if action == "press":
            self._handle_press_paddle(button)
        elif action == "release":
            self._handle_release_paddle(button)

    def _handle_press_paddle(self, button: str) -> None:
        old_task = self._tasks.get(button)
        if old_task and not old_task.done():
            old_task.cancel()

        self._pressed[button] = True
        self._tasks[button] = asyncio.create_task(
            self._press_lifecycle_paddle(button)
        )

    def _handle_release_paddle(self, button: str) -> None:
        self._pressed[button] = False

    async def _press_lifecycle_paddle(self, button: str) -> None:
        """Hold = ramp (lights only). Tap = on/off."""
        try:
            await asyncio.sleep(self._hold_time)

            # Short press
            if not self._pressed.get(button, False):
                if button == "on":
                    await self._short_press_on()
                else:
                    await self._short_press_off()
                return

            # Long press (light domain only)
            if self.conf.domain == "light":
                direction = 1 if button == "on" else -1
                await self._ramp_loop(direction, active_button=button)
            else:
                # Non-light domains: act immediately, no hold behavior
                if button == "on":
                    await self._short_press_on()
                else:
                    await self._short_press_off()

        except asyncio.CancelledError:
            pass
        finally:
            self._pressed[button] = False
            self._tasks[button] = None

    # ---------------------------------------------------------------------
    # Five-button profile
    # ---------------------------------------------------------------------

    def _handle_five_button_event(self, button: str, action: str) -> None:
        if action == "press":
            self._handle_press_five(button)
        elif action == "release":
            self._handle_release_five(button)

    def _handle_press_five(self, button: str) -> None:

        # Domain-specific STOP
        if button == "stop":
            if self.conf.domain == "cover":
                asyncio.create_task(
                    self._call_entity_service("stop_cover", {})
                )
            # Cancel raise/lower ramp
            for b in ("raise", "lower"):
                self._pressed[b] = False
                task = self._tasks.get(b)
                if task and not task.done():
                    task.cancel()
                    self._tasks[b] = None
            return

        # Standard ON/OFF
        if button == "on":
            asyncio.create_task(self._short_press_on())
            return

        if button == "off":
            asyncio.create_task(self._short_press_off())
            return

        # Raise/Lower mapping for COVER
        if button in ("raise", "lower"):
            if self.conf.domain == "cover":
                svc = "open_cover" if button == "raise" else "close_cover"
                asyncio.create_task(self._call_entity_service(svc, {}))
                return

            # Raise/Lower for FAN
            if self.conf.domain == "fan":
                step = self.conf.step_pct * (1 if button == "raise" else -1)
                asyncio.create_task(
                    self._call_entity_service(
                        "set_percentage",
                        {"percentage_step": step},
                    )
                )
                return

            # LIGHT (ramp)
            direction = 1 if button == "raise" else -1

            # Cancel opposite task
            for b in ("raise", "lower"):
                task = self._tasks.get(b)
                if task and not task.done():
                    task.cancel()
                self._pressed[b] = False

            self._pressed[button] = True
            self._tasks[button] = asyncio.create_task(
                self._ramp_loop(direction, button)
            )

    def _handle_release_five(self, button: str) -> None:
        if button in ("raise", "lower"):
            self._pressed[button] = False
            task = self._tasks.get(button)
            if task and not task.done():
                task.cancel()
                self._tasks[button] = None

    # ---------------------------------------------------------------------
    # Four-button profile (user-defined actions)
    # ---------------------------------------------------------------------

    def _handle_four_button_event(self, button: str, action: str) -> None:
        if action != "press":
            return

        action_list = self.conf.buttons.get(button)
        if not action_list:
            _LOGGER.debug(
                "Device %s (four_button): no actions for button '%s'",
                self.conf.device_id,
                button,
            )
            return

        for act in action_list:
            asyncio.create_task(self._execute_button_action(act))

    # ---------------------------------------------------------------------
    # Two-button profile
    # ---------------------------------------------------------------------

    def _handle_two_button_event(self, button: str, action: str) -> None:
        if action != "press":
            return

        if button == "on":
            asyncio.create_task(self._short_press_on())
        elif button == "off":
            asyncio.create_task(self._short_press_off())

    # ---------------------------------------------------------------------
    # Shared ON/OFF behaviors (domain-aware)
    # ---------------------------------------------------------------------

    async def _short_press_on(self) -> None:
        domain = self.conf.domain

        if domain == "light":
            await self._call_entity_service(
                "turn_on",
                {"brightness_pct": self.conf.on_pct},
            )

        elif domain == "fan":
            await self._call_entity_service(
                "set_percentage",
                {"percentage": self.conf.on_pct},
            )

        elif domain == "cover":
            await self._call_entity_service("open_cover", {})

    async def _short_press_off(self) -> None:
        domain = self.conf.domain

        if domain == "light":
            await self._call_entity_service("turn_off", {})

        elif domain == "fan":
            await self._call_entity_service("turn_off", {})

        elif domain == "cover":
            await self._call_entity_service("close_cover", {})

    # ---------------------------------------------------------------------
    # Ramping (LIGHT domain only)
    # ---------------------------------------------------------------------

    async def _ramp_loop(self, direction: int, active_button: str) -> None:
        """Repeatedly brightness_step_pct while held (LIGHT ONLY)."""

        if self.conf.domain != "light":
            return  # non-light domains do not support ramping

        step = self.conf.step_pct * direction

        try:
            while self._pressed.get(active_button, False):
                await self._call_entity_service(
                    "turn_on",
                    {"brightness_step_pct": step},
                    continue_on_error=True,
                )

                if not await self._brightness_in_range(direction):
                    break

                await asyncio.sleep(self._step_time)

        except asyncio.CancelledError:
            pass

    async def _brightness_in_range(self, direction: int) -> bool:
        """Check if brightness is still within limits."""

        if not self.conf.entities:
            return False

        state = self.hass.states.get(self.conf.entities[0])
        if not state:
            return False

        brightness = state.attributes.get("brightness")
        if brightness is None:
            return True

        if direction > 0 and brightness >= 254:
            return False
        if direction < 0 and brightness <= 1:
            return False

        return True

    # ---------------------------------------------------------------------
    # Generic domain-based service caller
    # ---------------------------------------------------------------------

    async def _call_entity_service(
        self,
        service: str,
        data: Dict[str, Any],
        continue_on_error: bool = False,
    ) -> None:

        domain = self.conf.domain  # light, fan, cover

        service_data = {**data}
        if self.conf.entities:
            service_data["entity_id"] = self.conf.entities

        try:
            await self.hass.services.async_call(
                domain, service, service_data, blocking=False
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
    # Four-button action executor
    # ---------------------------------------------------------------------

    async def _execute_button_action(self, action: Dict[str, Any]) -> None:
        """
        Executes a mapping such as:
        {
            "action": "light.turn_on",
            "target": {"entity_id": "..."},
            "data": {...}
        }
        """
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

        service_data = {**data}
        if target:
            eid = target.get("entity_id")
            if eid:
                service_data["entity_id"] = eid

        try:
            await self.hass.services.async_call(
                domain, service, service_data, blocking=False
            )
        except Exception as err:
            _LOGGER.error(
                "Device %s (four_button): error calling %s.%s: %s",
                self.conf.device_id,
                domain,
                service,
                err,
            )
