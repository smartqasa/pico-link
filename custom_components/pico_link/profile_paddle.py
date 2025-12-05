from __future__ import annotations

import asyncio
import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .controller import PicoController

_LOGGER = logging.getLogger(__name__)


class PaddleProfile:
    """Paddle profile: tap = on/off, hold = ramp (lights only)."""

    def __init__(self, controller: "PicoController") -> None:
        self._ctrl = controller

    # ------------------------------------------------------------------
    # ENTRY POINTS CALLED BY PicoController
    # ------------------------------------------------------------------
    def handle_press(self, button: str, token: int) -> None:
        """Called for every press. Token ensures lifecycle validity."""
        if button not in ("on", "off"):
            return

        # Cancel any previous lifecycle on this button
        existing = self._ctrl._tasks.get(button)
        if existing and not existing.done():
            existing.cancel()

        # Mark pressed
        self._ctrl._pressed[button] = True

        # Start lifecycle
        self._ctrl._tasks[button] = asyncio.create_task(
            self._press_lifecycle(button, token)
        )

    def handle_release(self, button: str) -> None:
        """
        DO NOT cancel lifecycle task here.
        That task determines TAP vs HOLD.
        """
        if button not in ("on", "off"):
            return

        self._ctrl._pressed[button] = False

    # ------------------------------------------------------------------
    # TAP / HOLD LIFECYCLE (TOKEN-SAFE)
    # ------------------------------------------------------------------
    async def _press_lifecycle(self, button: str, my_token: int) -> None:
        """
        After hold_time:
        - If released → TAP
        - If still pressed → HOLD (ramp)
        Token ensures stale tasks never fire.
        """
        try:
            # Wait hold timeout
            await asyncio.sleep(self._ctrl._hold_time)

            # Stale?
            if my_token != self._ctrl._press_tokens[button]:
                return

            # TAP?
            if not self._ctrl._pressed.get(button, False):
                if button == "on":
                    await self._ctrl._short_press_on()
                else:
                    await self._ctrl._short_press_off()
                return

            # HOLD (only lights)
            if self._ctrl.conf.domain == "light":
                direction = 1 if button == "on" else -1
                await self._ramp(button, direction, my_token)
            else:
                # Non-light: treat hold like tap
                if button == "on":
                    await self._ctrl._short_press_on()
                else:
                    await self._ctrl._short_press_off()

        except asyncio.CancelledError:
            pass

        finally:
            self._ctrl._pressed[button] = False
            self._ctrl._tasks[button] = None

    # ------------------------------------------------------------------
    # RAMP
    # ------------------------------------------------------------------
    async def _ramp(self, button: str, direction: int, token: int):
        step_pct = self._ctrl.conf.step_pct
        low_pct = self._ctrl.conf.low_pct

        step_value = round(255 * (step_pct / 100))
        min_brightness = max(1, round(255 * (low_pct / 100)))
        max_brightness = 255

        try:
            while True:

                # Abort if a newer press occurred
                if token != self._ctrl._press_tokens[button]:
                    return

                # Abort if button was released
                if not self._ctrl._pressed.get(button, False):
                    return

                # Current brightness
                entity_id = self._ctrl.conf.entities[0]
                state = self._ctrl.hass.states.get(entity_id)
                if not state:
                    return

                brightness = state.attributes.get("brightness")
                if brightness is None:
                    return

                #
                # Predict next brightness BEFORE applying step
                #
                if direction < 0:  # dimming
                    next_b = brightness - step_value

                    if next_b <= min_brightness:
                        # Set EXACTLY to low_pct stop value
                        await self._ctrl._call_entity_service(
                            "turn_on",
                            {"brightness": min_brightness},
                            continue_on_error=True,
                        )
                        return

                else:  # brightening
                    next_b = brightness + step_value

                    if next_b >= max_brightness:
                        # Hit the real top: 255
                        await self._ctrl._call_entity_service(
                            "turn_on",
                            {"brightness": max_brightness},
                            continue_on_error=True,
                        )
                        return

                #
                # Apply incremental change
                #
                await self._ctrl._call_entity_service(
                    "turn_on",
                    {"brightness_step_pct": step_pct * direction},
                    continue_on_error=True,
                )

                await asyncio.sleep(self._ctrl._step_time)

        except asyncio.CancelledError:
            return


