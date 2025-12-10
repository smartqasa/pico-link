from __future__ import annotations

import asyncio
import logging
import time
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from ..controller import PicoController

_LOGGER = logging.getLogger(__name__)


class CoverActions:
    """
    Cover behavior:

    - on    → open (respect cover_open_pos)
    - off   → close
    - stop  → stop or middle_button actions

    - raise/lower:
        * tap  = step position +/- cover_step_pct
        * hold = continuous open/close until release
    """

    MAX_STEPS = 50   # safety limit for ramp loops

    def __init__(self, ctrl: "PicoController") -> None:
        self.ctrl = ctrl

        # Local button-press tracking
        self._pressed: dict[str, bool] = {
            "raise": False,
            "lower": False,
        }

        self._press_ts: dict[str, float] = {}
        self._tasks: dict[str, Optional[asyncio.Task]] = {
            "raise": None,
            "lower": None,
        }

    # -------------------------------------------------------------
    # PUBLIC API
    # -------------------------------------------------------------
    def handle_press(self, button: str):
        match button:

            case "on":
                asyncio.create_task(self._open())

            case "off":
                asyncio.create_task(self._close())

            case "stop":
                actions = self.ctrl.conf.middle_button
                if actions:
                    for a in actions:
                        asyncio.create_task(self.ctrl.utils.execute_button_action(a))
                else:
                    asyncio.create_task(self._stop())

            case "raise" | "lower":
                self._pressed[button] = True
                self._press_ts[button] = time.time()

                task = asyncio.create_task(self._press_lifecycle(button))
                self._tasks[button] = task

            case _:
                _LOGGER.debug("CoverActions: unknown button %s", button)

    def handle_release(self, button: str):
        """Always stop motion on release, and step if it was a TAP."""

        if button not in ("raise", "lower"):
            return

        self._pressed[button] = False

        # Cancel hold/tap lifecycle
        task = self._tasks.get(button)
        if task and not task.done():
            task.cancel()
        self._tasks[button] = None

        asyncio.create_task(self._release_lifecycle(button))

    # -------------------------------------------------------------
    # TAP vs HOLD logic
    # -------------------------------------------------------------
    async def _press_lifecycle(self, button: str):
        await asyncio.sleep(self.ctrl.utils._hold_time)

        if not self._pressed.get(button):
            return  # TAP handled on release

        # HOLD → start continuous motion
        direction = "raise" if button == "raise" else "lower"
        await self._start_motion(direction)

    async def _release_lifecycle(self, button: str):
        now = time.time()
        start = self._press_ts.get(button, now)
        elapsed = now - start

        pos = self._get_position()

        # Short press → step
        if elapsed < self.ctrl.utils._hold_time and pos is not None:
            await self._step(button, pos)

        # Always stop after release
        await self._stop()

    # -------------------------------------------------------------
    # Position helpers
    # -------------------------------------------------------------
    def _get_position(self) -> Optional[int]:
        state = self.ctrl.utils.get_entity_state()
        if not state:
            return None
        return state.attributes.get("current_position")

    # -------------------------------------------------------------
    # Domain operations
    # -------------------------------------------------------------
    async def _start_motion(self, direction: str):
        svc = "open_cover" if direction == "raise" else "close_cover"

        await self.ctrl.utils.call_service(svc, {}, domain="cover")

    async def _open(self):
        pos = self.ctrl.conf.cover_open_pos
        if pos == 100:
            await self.ctrl.utils.call_service("open_cover", {}, domain="cover")
        else:
            await self.ctrl.utils.call_service(
                "set_cover_position", {"position": pos}, domain="cover"
            )

    async def _close(self):
        await self.ctrl.utils.call_service("close_cover", {}, domain="cover")

    async def _stop(self):
        await self.ctrl.utils.call_service("stop_cover", {}, domain="cover")

    async def _step(self, button: str, pos: int):
        step_pct = self.ctrl.conf.cover_step_pct

        new_pos = (
            min(100, pos + step_pct)
            if button == "raise"
            else max(0, pos - step_pct)
        )

        await self.ctrl.utils.call_service(
            "set_cover_position", {"position": new_pos}, domain="cover"
        )

    # -------------------------------------------------------------
    # RESET STATE (prevent runaway after reload)
    # -------------------------------------------------------------
    def reset_state(self):
        for t in self._tasks.values():
            if t and not t.done():
                t.cancel()

        for key in self._pressed:
            self._pressed[key] = False
            self._tasks[key] = None

        self._press_ts.clear()
