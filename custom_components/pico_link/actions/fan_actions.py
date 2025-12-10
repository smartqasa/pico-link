# fan_actions.py
from __future__ import annotations

import asyncio
import logging
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from ..controller import PicoController

_LOGGER = logging.getLogger(__name__)


class FanActions:
    """
    Fan behavior:

    TAP:
        on      → set percentage to fan_on_pct
        off     → turn_off
        raise   → increase to next discrete speed
        lower   → decrease to previous discrete speed
        stop    → middle_button actions OR reverse direction

    Special rule:
        If fan is OFF and raise is tapped → turn on to first step speed.

    NO HOLD LOGIC.
    """

    def __init__(self, ctrl: "PicoController") -> None:
        self.ctrl = ctrl

    # -------------------------------------------------------------
    # PUBLIC API (called by profiles)
    # -------------------------------------------------------------
    def press_on(self):
        asyncio.create_task(self._turn_on())

    def release_on(self):
        pass  # tap-only

    def press_off(self):
        asyncio.create_task(self._turn_off())

    def release_off(self):
        pass

    def press_stop(self):
        actions = self.ctrl.conf.middle_button

        if actions:
            for action in actions:
                asyncio.create_task(self.ctrl.utils.execute_button_action(action))
            return

        asyncio.create_task(self._reverse_direction())

    def release_stop(self):
        pass

    def press_raise(self):
        asyncio.create_task(self._step_up())

    def release_raise(self):
        pass

    def press_lower(self):
        asyncio.create_task(self._step_down())

    def release_lower(self):
        pass

    # -------------------------------------------------------------
    # FAN OPERATIONS
    # -------------------------------------------------------------
    async def _turn_on(self):
        pct = self.ctrl.conf.fan_on_pct
        await self.ctrl.utils.call_service(
            "set_percentage",
            {"percentage": pct},
            domain="fan",
        )

    async def _turn_off(self):
        await self.ctrl.utils.call_service(
            "turn_off",
            {},
            domain="fan",
        )

    async def _reverse_direction(self):
        state = self.ctrl.utils.get_entity_state()
        if not state:
            return

        cur = state.attributes.get("direction")
        if cur not in ("forward", "reverse"):
            return

        new_dir = "reverse" if cur == "forward" else "forward"

        await self.ctrl.utils.call_service(
            "set_direction",
            {"direction": new_dir},
            domain="fan",
        )

    # -------------------------------------------------------------
    # DISCRETE STEPPING
    # -------------------------------------------------------------
    def _build_speed_ladder(self, speeds: int) -> list[int]:
        """Return a list like [0, 25, 50, 75, 100] for speeds=5."""
        steps = speeds - 1
        return [round(i * 100 / steps) for i in range(speeds)]

    def _get_current_pct(self) -> Optional[float]:
        state = self.ctrl.utils.get_entity_state()
        if not state:
            return None

        pct = state.attributes.get("percentage")

        if pct is None:
            # off → treat as 0%
            return 0.0 if state.state == "off" else float(self.ctrl.conf.fan_on_pct)

        try:
            return float(pct)
        except Exception:
            return None

    async def _step_up(self):
        speeds = self.ctrl.conf.fan_speeds
        ladder = self._build_speed_ladder(speeds)

        current = self._get_current_pct()
        if current is None:
            return

        # If off → go to first step
        if current == 0:
            first_step = ladder[1] if len(ladder) > 1 else self.ctrl.conf.fan_on_pct
            await self.ctrl.utils.call_service(
                "set_percentage",
                {"percentage": first_step},
                domain="fan",
            )
            return

        idx = min(range(len(ladder)), key=lambda i: abs(ladder[i] - current))
        new_idx = min(len(ladder) - 1, idx + 1)

        if new_idx == idx:
            return  # already at max

        await self.ctrl.utils.call_service(
            "set_percentage",
            {"percentage": ladder[new_idx]},
            domain="fan",
        )

    async def _step_down(self):
        speeds = self.ctrl.conf.fan_speeds
        ladder = self._build_speed_ladder(speeds)

        current = self._get_current_pct()
        if current is None:
            return

        idx = min(range(len(ladder)), key=lambda i: abs(ladder[i] - current))
        new_idx = max(0, idx - 1)

        await self.ctrl.utils.call_service(
            "set_percentage",
            {"percentage": ladder[new_idx]},
            domain="fan",
        )
