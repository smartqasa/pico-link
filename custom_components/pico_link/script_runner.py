"""Home Assistant scripts with one execution policy per physical Pico."""

from __future__ import annotations

import asyncio
import logging
from collections.abc import Awaitable, Callable
from copy import deepcopy
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

from homeassistant.core import Context
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.script import (
    DATA_SCRIPTS,
    Script,
    async_validate_actions_config,
)

from .color_cycle import get_cycle_store
from .const import DOMAIN

if TYPE_CHECKING:
    from .controller import PicoController

_LOGGER = logging.getLogger(__name__)
LEGACY_KEYS = {"action", "target", "data"}


def has_template(value: Any) -> bool:
    if isinstance(value, str):
        return "{{" in value or "{%" in value
    if isinstance(value, dict):
        return any(has_template(item) for item in value.values())
    if isinstance(value, list):
        return any(has_template(item) for item in value)
    return False


def is_legacy_sequence(actions: list[dict[str, Any]]) -> bool:
    """Only the original, flat service-call format gets legacy error handling."""
    return not has_template(actions) and all(
        "action" in action and action.keys() <= LEGACY_KEYS for action in actions
    )


def script_schema(actions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Use HA validation, including its pre-2024 service spelling."""

    def convert(value: Any) -> Any:
        # Recurse through action sequences only, never service data or variables.
        if isinstance(value, dict):
            value = [value]
        if not isinstance(value, list):
            return value
        result = []
        for original in value:
            action = deepcopy(original)
            if not isinstance(action, dict):
                result.append(action)
                continue
            if "action" in action and "service" not in action:
                action["service"] = action.pop("action")
            for key in ("then", "else", "default", "sequence"):
                if key in action:
                    action[key] = convert(action[key])
            if isinstance(action.get("repeat"), dict):
                repeat = action["repeat"]
                if "sequence" in repeat:
                    repeat["sequence"] = convert(repeat["sequence"])
            if isinstance(action.get("choose"), list):
                for choice in action["choose"]:
                    if isinstance(choice, dict) and "sequence" in choice:
                        choice["sequence"] = convert(choice["sequence"])
            if isinstance(action.get("parallel"), list):
                action["parallel"] = convert(action["parallel"])
            result.append(action)
        return result

    return cv.SCRIPT_SCHEMA(convert(actions))


@dataclass
class PreparedSequence:
    scripts: list[Script]
    legacy: bool
    actions: list[dict[str, Any]]
    name: str


class PicoScriptRunner:
    """Share admission/cancellation across different button script objects.

    HA executes every action. A small per-Pico coordinator is necessary because
    HA's own modes apply to one Script object, not to different button sequences.
    Script objects are prepared once and explicitly released during shutdown.
    """

    def __init__(self, ctrl: PicoController) -> None:
        self.ctrl = ctrl
        self.sequences: dict[int, PreparedSequence] = {}
        self._runs: set[asyncio.Task] = set()
        self._queue = asyncio.Lock()
        self._stopping = False
        self._interrupted: set[asyncio.Task] = set()
        self._cancel_requested: set[asyncio.Task] = set()

    async def async_prepare(self) -> None:
        conf = self.ctrl.conf
        sequences = {
            "middle_button": conf.middle_button,
            **conf.buttons,
            **conf.overrides,
        }
        for name, actions in sequences.items():
            if not actions or id(actions) in self.sequences:
                continue
            legacy = is_legacy_sequence(actions)
            prepared = PreparedSequence([], legacy, actions, name)
            self.sequences[id(actions)] = prepared
            # Legacy lists have no shared script variables or control flow. Run
            # their service steps through HA individually so *all* old service
            # failures still log and continue, including missing services.
            parts = [[action] for action in actions] if legacy else [actions]
            for index, part in enumerate(parts, start=1):
                if legacy:
                    # The old service API merged target into data without
                    # coercing scalar selectors into lists. Preserve that
                    # service payload while still executing through HA Script.
                    part = deepcopy(part)
                    if target := part[0].pop("target", None):
                        part[0]["data"] = {**part[0].get("data", {}), **target}
                sequence = await async_validate_actions_config(
                    self.ctrl.hass, script_schema(part)
                )
                prepared.scripts.append(
                    Script(
                        self.ctrl.hass,
                        sequence,
                        f"Pico {conf.device_id} {name} {index}",
                        DOMAIN,
                        script_mode="parallel",
                        max_runs=conf.max,
                        max_exceeded=conf.max_exceeded.upper(),
                        logger=_LOGGER,
                        log_exceptions=not legacy,
                    )
                )

    def _reject(self, message: str) -> None:
        level = self.ctrl.conf.max_exceeded
        if level != "silent":
            _LOGGER.log(
                getattr(logging, level.upper()),
                "Pico %s: %s; new custom sequence ignored",
                self.ctrl.conf.device_id,
                message,
            )

    def interrupt(self) -> None:
        """A recognized native command supersedes custom work in restart mode."""
        if self.ctrl.conf.mode != "restart":
            return
        for task in tuple(self._runs):
            if not task.done():
                # Cancel only once: a second cancellation can interrupt the
                # script engine while it is cleaning up its first cancellation.
                self.cancel_task(task)
                self._interrupted.add(task)

    def cancel_task(self, task: asyncio.Task) -> None:
        """Cancel once, including on older Python without Task.cancelling()."""
        if task.done() or task in self._cancel_requested:
            return
        self._cancel_requested.add(task)
        task.add_done_callback(self._cancel_requested.discard)
        task.cancel()

    async def async_wait_interrupted(self) -> None:
        pending = tuple(self._interrupted)
        if pending:
            await asyncio.gather(
                *(asyncio.shield(task) for task in pending), return_exceptions=True
            )
            self._interrupted.difference_update(pending)

    async def async_run(self, actions: list[dict[str, Any]]) -> None:
        if self._stopping or not actions:
            return
        prepared = self.sequences[id(actions)]
        await self._async_run(lambda: self._execute(prepared))

    async def async_run_color_cycle(self, gesture: str) -> None:
        """Apply the same per-Pico run policy to the opt-in native gesture."""
        conf = self.ctrl.conf

        async def execute() -> None:
            try:
                await get_cycle_store(self.ctrl.hass).async_cycle(
                    conf.device_id, gesture, conf.lights, conf.color_palettes[gesture]
                )
            except Exception:
                _LOGGER.exception(
                    "Pico %s (%s): color cycle failed", conf.device_id, gesture
                )

        await self._async_run(execute)

    async def _async_run(self, execute: Callable[[], Awaitable[None]]) -> None:
        if self._stopping:
            return
        mode = self.ctrl.conf.mode
        self._runs = {task for task in self._runs if not task.done()}
        if mode == "single" and self._runs:
            self._reject("Already running")
            return
        if mode in {"queued", "parallel"} and len(self._runs) >= self.ctrl.conf.max:
            self._reject("Maximum number of runs exceeded")
            return
        if mode == "restart":
            self.interrupt()
        task = asyncio.current_task()
        assert task is not None
        self._runs.add(task)
        try:
            await self.async_wait_interrupted()
            if mode == "queued":
                async with self._queue:
                    await execute()
            else:
                await execute()
        finally:
            self._runs.discard(task)

    async def _execute(self, prepared: PreparedSequence) -> None:
        context = Context()
        for index, script in enumerate(prepared.scripts):
            if self._stopping:
                return
            try:
                await script.async_run(context=context)
            except Exception:
                if prepared.legacy:
                    _LOGGER.exception(
                        "Pico %s: error calling %s",
                        self.ctrl.conf.device_id,
                        prepared.actions[index]["action"],
                    )
                else:
                    _LOGGER.exception(
                        "Pico %s: custom sequence %s failed",
                        self.ctrl.conf.device_id,
                        prepared.name,
                    )
                    return

    def stop_accepting(self) -> None:
        self._stopping = True

    async def async_close(self) -> None:
        self.stop_accepting()
        pending = tuple(self._runs | self._interrupted)
        for task in pending:
            self.cancel_task(task)
        if pending:
            await asyncio.gather(*pending, return_exceptions=True)
        for prepared in self.sequences.values():
            for script in prepared.scripts:
                unload = getattr(script, "async_unload", None)
                if unload is not None:
                    await unload()
                else:
                    # Older supported HA releases have no unload API. Stop the
                    # object and remove only its own global shutdown registration.
                    await script.async_stop()
                    registry = self.ctrl.hass.data.get(DATA_SCRIPTS)
                    if isinstance(registry, list):
                        registry[:] = [
                            item for item in registry if item["instance"] is not script
                        ]
                    elif isinstance(registry, dict):
                        registry.pop(id(script), None)
        self.sequences.clear()
        self._runs.clear()
        self._interrupted.clear()
        self._cancel_requested.clear()
