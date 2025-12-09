from __future__ import annotations

import asyncio
import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .controller import PicoController

_LOGGER = logging.getLogger(__name__)


class Pico3ButtonRaiseLower:
    """Pico3ButtonRaiseLower Pico:
    - on/off
    - stop (optional custom action)
    - raise/lower → tap = step, hold = ramp
    """

    def __init__(self, controller: "PicoController") -> None:
        self._ctrl = controller

    # -------------------------------------------------------------
    # ENTRY POINTS
    # -------------------------------------------------------------
    def handle_press(self, button: str) -> None:
        if button == "stop":
            self._handle_stop()
            return

        if button == "on":
            asyncio.create_task(self._ctrl._short_press_on())
            return

        if button == "off":
            asyncio.create_task(self._ctrl._short_press_off())
            return

        if button in ("raise", "lower"):
            self._handle_raise_lower(button)

    def handle_release(self, button: str) -> None:
        if button in ("raise", "lower"):
            self._ctrl._pressed[button] = False
            task = self._ctrl._tasks.get(button)
            if task and not task.done():
                task.cancel()
            self._ctrl._tasks[button] = None

    # -------------------------------------------------------------
    # STOP BUTTON
    # -------------------------------------------------------------
    def _handle_stop(self):
        # Cancel raise/lower first
        for b in ("raise", "lower"):
            self._ctrl._pressed[b] = False
            task = self._ctrl._tasks.get(b)
            if task and not task.done():
                task.cancel()
            self._ctrl._tasks[b] = None

        # Custom middle_button action?
        middle_action = getattr(self._ctrl.conf, "middle_button", None)
        if middle_action:
            asyncio.create_task(self._ctrl._execute_button_action(middle_action))
            return

        # Default STOP behavior based on entity domain
        domain = self._ctrl._entity_domain()
        match domain:

            # -----------------------------------------------------
            # FAN — reverse direction on STOP
            # -----------------------------------------------------
            case "fan":
                state = self._ctrl.get_entity_state()
                if not state:
                    return

                current_dir = state.attributes.get("direction")

                if current_dir in ("forward", "reverse"):
                    new_dir = (
                        "reverse" if current_dir == "forward" else "forward"
                    )

                    asyncio.create_task(
                        self._ctrl._call_entity_service(
                            "set_direction",
                            {"direction": new_dir},
                        )
                    )
                return

            # -----------------------------------------------------
            # COVER — normal STOP behavior
            # -----------------------------------------------------
            case "cover":
                asyncio.create_task(
                    self._ctrl._call_entity_service("stop_cover", {})
                )
                return

            # -----------------------------------------------------
            # ALL OTHER DOMAINS — do nothing
            # -----------------------------------------------------
            case _:
                return


    # -------------------------------------------------------------
    # RAISE / LOWER PRESS
    # -------------------------------------------------------------
    def _handle_raise_lower(self, button: str) -> None:
        direction = 1 if button == "raise" else -1
        domain = self._ctrl._entity_domain()

        # LIGHT
        if domain == "light":
            self._ctrl._pressed[button] = True

            # Tap step immediately
            asyncio.create_task(
                self._ctrl._call_entity_service(
                    "turn_on",
                    {"brightness_step_pct": self._ctrl.conf.step_pct * direction},
                )
            )

            # Begin lifecycle for hold/ramp
            self._ctrl._tasks[button] = asyncio.create_task(
                self._light_lifecycle(button, direction)
            )
            return

        # FAN
        if domain == "fan":
            asyncio.create_task(self._ctrl._fan_step_discrete(direction))
            return

        # COVER
        if domain == "cover":
            svc = "open_cover" if button == "raise" else "close_cover"
            asyncio.create_task(self._ctrl._call_entity_service(svc, {}))
            return

        # Unsupported domain
        _LOGGER.debug(
            "Device %s: raise/lower pressed but domain '%s' unsupported",
            self._ctrl.conf.device_id,
            domain,
        )

    # -------------------------------------------------------------
    # TAP/HOLD lifecycle (raise/lower)
    # -------------------------------------------------------------
    async def _light_lifecycle(self, button: str, direction: int):
        try:
            await asyncio.sleep(self._ctrl._hold_time)

            # Released → no hold behavior
            if not self._ctrl._pressed.get(button, False):
                return

            # HOLD → ramp
            await self._ctrl._ramp(button, direction)

        except asyncio.CancelledError:
            pass

        finally:
            self._ctrl._pressed[button] = False
            self._ctrl._tasks[button] = None
