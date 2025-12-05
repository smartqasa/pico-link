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

        # Mark this button as pressed
        self._ctrl._pressed[button] = True

        # Start tap/hold lifecycle
        self._ctrl._tasks[button] = asyncio.create_task(
            self._press_lifecycle(button, token)
        )

    def handle_release(self, button: str) -> None:
        """
        DO NOT cancel lifecycle task here.
        That task needs to run so it can detect TAP vs HOLD.
        """
        if button not in ("on", "off"):
            return

        # Mark released
        self._ctrl._pressed[button] = False
        # Do NOT cancel the task!
        # A TAP occurs only when the lifecycle wakes up after hold_time
        # and sees "_pressed == False".

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
            # Wait for hold timeout
            await asyncio.sleep(self._ctrl._hold_time)

            # If a newer press occurred → exit silently
            if my_token != self._ctrl._press_tokens[button]:
                return

            # TAP: button was released before hold_time
            if not self._ctrl._pressed.get(button, False):
                if button == "on":
                    await self._ctrl._short_press_on()
                else:
                    await self._ctrl._short_press_off()
                return

            # HOLD behavior (light domain only)
            if self._ctrl.conf.domain == "light":
                direction = 1 if button == "on" else -1
                await self._ramp_paddle(direction, button)
            else:
                # Non-light devices → treat hold like tap
                if button == "on":
                    await self._ctrl._short_press_on()
                else:
                    await self._ctrl._short_press_off()

        except asyncio.CancelledError:
            pass

        finally:
            # Cleanup lifecycle
            self._ctrl._pressed[button] = False
            self._ctrl._tasks[button] = None

    # ------------------------------------------------------------------
    # LOCAL RAMP IMPLEMENTATION (PADDLE-ONLY)
    # ------------------------------------------------------------------
    async def _ramp_paddle(self, direction: int, button: str) -> None:
        step_pct = self._ctrl.conf.step_pct
        step = step_pct * direction

        try:
            while self._ctrl._pressed.get(button, False):

                await self._ctrl._call_entity_service(
                    "turn_on",
                    {"brightness_step_pct": step},
                    continue_on_error=True,
                )

                await asyncio.sleep(self._ctrl._step_time)

        except asyncio.CancelledError:
            pass
