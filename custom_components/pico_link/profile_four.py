from __future__ import annotations

import asyncio
import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .controller import PicoController

_LOGGER = logging.getLogger(__name__)

# Actual button types emitted by Lutron Pico4ButtonScene
FOUR_BUTTON_TYPES = {"button_1", "button_2", "button_3", "off"}


class FourButtonProfile:
    """Four-button profile: user-defined HA actions per button."""

    def __init__(self, controller: "PicoController") -> None:
        self._ctrl = controller

    # Public entrypoint used by PicoController
    def handle(self, button: str, action: str) -> None:
        # Only respond to press, ignore release
        if action != "press":
            return

        # Verify button is actually a four-button input
        if button not in FOUR_BUTTON_TYPES:
            _LOGGER.debug(
                "Device %s (four_button): unsupported button '%s' "
                "(expected one of %s)",
                self._ctrl.conf.device_id,
                button,
                FOUR_BUTTON_TYPES,
            )
            return

        # Lookup configured actions for this button
        action_list = self._ctrl.conf.buttons.get(button)
        if not action_list:
            _LOGGER.debug(
                "Device %s (four_button): no actions configured for '%s'",
                self._ctrl.conf.device_id,
                button,
            )
            return

        # Execute all actions assigned to this button
        for index, act in enumerate(action_list):
            try:
                asyncio.create_task(self._ctrl._execute_button_action(act))
            except Exception as err:
                _LOGGER.error(
                    "Device %s (four_button): error executing action #%s for '%s': %s",
                    self._ctrl.conf.device_id,
                    index,
                    button,
                    err,
                )
