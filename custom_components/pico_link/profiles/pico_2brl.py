# profiles/pico_2brl.py
from __future__ import annotations

import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..controller import PicoController

_LOGGER = logging.getLogger(__name__)


class Pico2ButtonRaiseLower:
    """
    PJ2-2BRL: On, Raise, Lower, Off. A 3BRL without the Stop button.

    On and Off behave exactly as they do on a 3BRL, and Raise/Lower step
    and ramp the same way. There is no Stop button, so `middle_button`
    and the stop_* gestures are not accepted for this type (see
    config.py).
    """

    def __init__(self, controller: "PicoController") -> None:
        self._ctrl = controller

    def _actions(self):
        domain = self._ctrl.utils.entity_domain()
        if not domain:
            _LOGGER.debug("2BRL: no domain configured")
            return None

        actions = self._ctrl.actions.get(domain)
        if not actions:
            _LOGGER.debug("2BRL: no action handler for domain %s", domain)
            return None

        return actions

    # -------------------------------------------------------------
    # PRESS
    # -------------------------------------------------------------
    def handle_press(self, button: str) -> None:
        actions = self._actions()
        if not actions:
            return

        match button:
            case "on":
                actions.press_on()
            case "off":
                actions.press_off()
            case "raise":
                actions.press_raise()
            case "lower":
                actions.press_lower()
            case _:
                _LOGGER.debug("2BRL: unknown press button '%s'", button)

    # -------------------------------------------------------------
    # RELEASE
    # -------------------------------------------------------------
    def handle_release(self, button: str) -> None:
        actions = self._actions()
        if not actions:
            return

        match button:
            case "raise":
                actions.release_raise()
            case "lower":
                actions.release_lower()
            case _:
                pass
