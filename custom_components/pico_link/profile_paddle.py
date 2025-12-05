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
        """
        Called by PicoController for every button press.
        `token` uniquely identifies THIS press and rejects stale tasks.
        """
        if button not in ("on", "off"):
            return

        # Cancel any previous task for this button
        existing = self._ctrl._tasks.get(button)
        if existing and not existing.done():
            existing.cancel()

        # Mark pressed
        self._ctrl._pressed[button] = True

        # Launch the tap/hold lifecycle
        self._ctrl._tasks[button] = asyncio.create_task(
            self._press_lifecycle(button, token)
        )

    def handle_release(self, button: str) -> None:
        """Called by PicoController on release."""
        if button not in ("on", "off"):
            return

        self._ctrl._pressed[button] = False
        task = self._ctrl._tasks.get(button)
        if task and not task.done():
            task.cancel()

        self._ctrl._tasks[button] = None

    # ------------------------------------------------------------------
    # TAP / HOLD LIFECYCLE (TOKEN-SAFE)
    # ------------------------------------------------------------------
    async def _press_lifecycle(self, button: str, my_token: int) -> None:
        """
        - A quick release → TAP
        - A continued hold → HOLD and ramp
        """
        try:
            # Wait for hold timeout
            await asyncio.sleep(self._ctrl._hold_time)

            # If a newer press has occurred → this is stale, exit
            if my_token != self._ctrl._press_tokens[button]:
                return

            # If button was released → TAP
            if not self._ctrl._pressed.get(button, False):
                if button == "on":
                    await self._ctrl._short_press_on()
                else:
                    await self._ctrl._short_press_off()
                return

            # HOLD → ramp (lights only)
            if self._ctrl.conf.domain == "light":
                direction = 1 if button == "on" else -1
                await self._ramp_paddle(direction, button)
            else:
                # Non-light devices: treat hold as tap
                if button == "on":
                    await self._ctrl._short_press_on()
                else:
                    await self._ctrl._short_press_off()

        except asyncio.CancelledError:
            pass

        finally:
            # Cleanup
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
