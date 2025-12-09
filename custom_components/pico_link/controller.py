from __future__ import annotations

import logging
from typing import Any, Dict, Mapping, Optional, Tuple

from homeassistant.core import Event, HomeAssistant, callback

from .config import PicoConfig
from .const import (
    SUPPORTED_BUTTONS,
    PICO_EVENT_TYPE,
    PICO_TYPE_MAP,
)
from .behaviors import SharedBehaviors

from .profile_base import PicoProfile
from .profile_p2b import PaddleSwitchPico
from .profile_3brl import Pico3ButtonRaiseLower
from .profile_2b import Pico2Button
from .profile_4b import Pico4ButtonScene

_LOGGER = logging.getLogger(__name__)


# --------------------------------------------------------------------
# CORRECTED: Map normalized device types → behavior classes
# Must match VALID_PICO_TYPES exactly: {"3BRL", "4B", "P2B", "2B"}
# --------------------------------------------------------------------
BEHAVIOR_CLASSES: Dict[str, type[PicoProfile]] = {
    "P2B": PaddleSwitchPico,        # Paddle Pico
    "2B": Pico2Button,              # 2-button Pico
    "3BRL": Pico3ButtonRaiseLower,  # 3-button raise/lower Pico
    "4B": Pico4ButtonScene,         # 4-button scene Pico
}

class PicoController(SharedBehaviors):
    """Main controller for a single Lutron Pico device."""

    def __init__(self, hass: HomeAssistant, conf: PicoConfig) -> None:
        super().__init__(hass, conf)

        # Behavior instance gets set after the first event
        self._behavior: Optional[PicoProfile] = None
        self._behavior_name: Optional[str] = None

    # ---------------------------------------------------------
    # START LISTENING
    # ---------------------------------------------------------
    async def async_start(self) -> None:

        @callback
        def _handle_event(event: Event) -> None:
            data = event.data

            # Must match this Pico device
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

            # -----------------------------------------------------
            # AUTO-DETECT DEVICE TYPE ONE TIME
            # -----------------------------------------------------
            if self._behavior is None:
                device_type_raw = data.get("type")

                if not device_type_raw:
                    _LOGGER.error(
                        "Device %s: event missing 'type' field; cannot determine behavior.",
                        self.conf.device_id,
                    )
                    return

                normalized = PICO_TYPE_MAP.get(device_type_raw)
                if not normalized:
                    _LOGGER.error(
                        "Device %s: unknown Pico type '%s'",
                        self.conf.device_id,
                        device_type_raw,
                    )
                    return

                # -------------------------------------------------
                # TYPE MISMATCH CHECK (YAML vs. hardware)
                # -------------------------------------------------
                configured_type = self.conf.type
                if normalized != configured_type:
                    _LOGGER.error(
                        (
                            "Device %s type mismatch: YAML defines type='%s' "
                            "but Lutron event reports type='%s' (raw='%s')."
                        ),
                        self.conf.device_id,
                        configured_type,
                        normalized,
                        device_type_raw,
                    )
                    # Continue anyway; runtime behavior uses normalized type

                behavior_cls = BEHAVIOR_CLASSES.get(normalized)
                if not behavior_cls:
                    _LOGGER.error(
                        "Device %s: no behavior implemented for type '%s'",
                        self.conf.device_id, normalized
                    )
                    return

                self._behavior = behavior_cls(self)
                self._behavior_name = normalized

                _LOGGER.warning(
                    "Device %s behavior set to '%s' (from type '%s')",
                    self.conf.device_id, normalized, device_type_raw
                )

            # -----------------------------------------------------
            # DISPATCH EVENT TO THE DEVICE'S BEHAVIOR
            # -----------------------------------------------------
            try:
                if action == "press":
                    self._behavior.handle_press(button)
                else:
                    self._behavior.handle_release(button)

            except Exception as err:
                _LOGGER.error(
                    "Device %s: behavior '%s' error handling %s/%s: %s",
                    self.conf.device_id,
                    self._behavior_name,
                    button,
                    action,
                    err,
                )

        self._unsub_event = self.hass.bus.async_listen(PICO_EVENT_TYPE, _handle_event)

    # ---------------------------------------------------------
    # STOP / CLEANUP
    # ---------------------------------------------------------
    def async_stop(self) -> None:
        if self._unsub_event:
            self._unsub_event()
            self._unsub_event = None

        # Cancel long-running tasks (e.g., ramping)
        for button in SUPPORTED_BUTTONS:
            task = self._tasks.get(button)
            if task and not task.done():
                task.cancel()
            self._tasks[button] = None

        self._pressed = {btn: False for btn in SUPPORTED_BUTTONS}

    # ---------------------------------------------------------
    # EVENT PAYLOAD → (button, action)
    # ---------------------------------------------------------
    def _map_event_payload(
        self, data: Mapping[str, Any]
    ) -> Tuple[Optional[str], Optional[str]]:
        button = data.get("button_type")
        action = data.get("action")

        if not button or not action:
            return None, None

        button = str(button).lower()
        action = str(action).lower()

        if action not in ("press", "release"):
            return None, None

        return button, action
