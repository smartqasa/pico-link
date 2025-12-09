from __future__ import annotations

import asyncio
import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..controller import PicoController

_LOGGER = logging.getLogger(__name__)


class Pico3ButtonRaiseLower:
    """Pico3ButtonRaiseLower Pico:
    - on/off
    - stop (optional custom action)
    - raise/lower:
        * tap  = step (position +=/-= step_pct)
        * hold = open/close
        * release = stop
    """

    def __init__(self, controller: "PicoController") -> None:
        self._ctrl = controller
        self._press_timestamp: dict[str, float] = {}

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
            # record timestamp for tap-vs-hold detection
            self._press_timestamp[button] = asyncio.get_event_loop().time()
            self._ctrl._pressed[button] = True
            self._handle_raise_lower(button)

    def handle_release(self, button: str) -> None:
        domain = self._ctrl._entity_domain()

        if button in ("raise", "lower"):

            # COVER
            if domain == "cover":
                asyncio.create_task(self._cover_handle_release(button))
                return

            # LIGHT (existing behavior: cancel ramp)
            self._ctrl._pressed[button] = False
            task = self._ctrl._tasks.get(button)
            if task and not task.done():
                task.cancel()
            self._ctrl._tasks[button] = None

    # -------------------------------------------------------------
    # STOP BUTTON
    # -------------------------------------------------------------
    def _handle_stop(self):
        # Cancel raise/lower tasks
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

        # Default STOP behavior based on domain
        domain = self._ctrl._entity_domain()
        match domain:

            case "cover":
                asyncio.create_task(
                    self._ctrl._call_entity_service("stop_cover", {})
                )
                return

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

            case _:
                return

    # -------------------------------------------------------------
    # RAISE / LOWER PRESS DISPATCH
    # -------------------------------------------------------------
    def _handle_raise_lower(self, button: str) -> None:
        direction = 1 if button == "raise" else -1
        domain = self._ctrl._entity_domain()

        match domain:

            # ---------------------------------------------------------
            # COVER (new behavior)
            # ---------------------------------------------------------
            case "cover":
                asyncio.create_task(self._cover_handle_press(button))
                return

            # ---------------------------------------------------------
            # FAN
            # ---------------------------------------------------------
            case "fan":
                asyncio.create_task(
                    self._ctrl._fan_step_discrete(direction)
                )
                return

            # ---------------------------------------------------------
            # LIGHT
            # ---------------------------------------------------------
            case "light":
                self._ctrl._pressed[button] = True

                # Tap step immediately
                asyncio.create_task(
                    self._ctrl._call_entity_service(
                        "turn_on",
                        {"brightness_step_pct": self._ctrl.conf.step_pct * direction},
                    )
                )

                # Begin lifecycle for hold → ramp
                self._ctrl._tasks[button] = asyncio.create_task(
                    self._light_lifecycle(button, direction)
                )
                return

            # ---------------------------------------------------------
            # MEDIA PLAYER (unsupported)
            # ---------------------------------------------------------
            case "media_player":
                _LOGGER.debug(
                    "Device %s: raise/lower used with unsupported domain 'media_player'",
                    self._ctrl.conf.device_id,
                )
                return

            # ---------------------------------------------------------
            # SWITCH (unsupported)
            # ---------------------------------------------------------
            case "switch":
                _LOGGER.debug(
                    "Device %s: raise/lower used with unsupported domain 'switch'",
                    self._ctrl.conf.device_id,
                )
                return

            # ---------------------------------------------------------
            # Unsupported domain
            # ---------------------------------------------------------
            case _:
                _LOGGER.debug(
                    "Device %s: raise/lower pressed but domain '%s' unsupported",
                    self._ctrl.conf.device_id,
                    domain,
                )

    # -------------------------------------------------------------
    # COVER TAP/HOLD HANDLING
    # -------------------------------------------------------------
    async def _cover_handle_press(self, button: str):
        """
        Wait hold_time → if still pressed, start movement.
        Release handler handles tap.
        """
        await asyncio.sleep(self._ctrl._hold_time)

        # If released → tap, do nothing here
        if not self._ctrl._pressed.get(button, False):
            return

        # HOLD → start cover motion
        direction = "raise" if button == "raise" else "lower"
        await self._ctrl.cover_start_motion(direction)

    async def _cover_handle_release(self, button: str):
        """Tap = step movement; Always stop afterward."""
        self._ctrl._pressed[button] = False

        now = asyncio.get_event_loop().time()
        start = self._press_timestamp.get(button, now)
        elapsed = now - start

        pos = self._ctrl.cover_get_position()
        if pos is None:
            await self._ctrl.cover_stop()
            return

        step_pct = self._ctrl.conf.step_pct or 5
        hold_time = self._ctrl._hold_time

        # TAP → move by step_pct
        if elapsed < hold_time:
            await self._cover_step(button, pos, step_pct)

        # ALWAYS stop cover
        await self._ctrl.cover_stop()

    async def _cover_step(self, button: str, pos: int, step_pct: int):
        """Adjust by step_pct relative to current_position."""
        if button == "raise":
            new_pos = min(100, pos + step_pct)
        else:
            new_pos = max(0, pos - step_pct)

        await self._ctrl.cover_set_position(new_pos)

    # -------------------------------------------------------------
    # LIGHT TAP/HOLD LIFECYCLE (existing)
    # -------------------------------------------------------------
    async def _light_lifecycle(self, button: str, direction: int):
        try:
            await asyncio.sleep(self._ctrl._hold_time)

            if not self._ctrl._pressed.get(button, False):
                return

            await self._ctrl._ramp(button, direction)

        except asyncio.CancelledError:
            pass

        finally:
            self._ctrl._pressed[button] = False
            self._ctrl._tasks[button] = None
