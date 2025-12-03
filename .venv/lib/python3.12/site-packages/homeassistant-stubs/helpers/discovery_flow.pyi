import dataclasses
from _typeshed import Incomplete
from collections.abc import Coroutine
from homeassistant.config_entries import ConfigFlowContext as ConfigFlowContext, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import EVENT_HOMEASSISTANT_STARTED as EVENT_HOMEASSISTANT_STARTED
from homeassistant.core import CoreState as CoreState, Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util.async_ import gather_with_limited_concurrency as gather_with_limited_concurrency
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Any, NamedTuple, Self

FLOW_INIT_LIMIT: int
DISCOVERY_FLOW_DISPATCHER: HassKey[FlowDispatcher]

@dataclasses.dataclass(kw_only=True, slots=True)
class DiscoveryKey:
    domain: str
    key: str | tuple[str, ...]
    version: int
    @classmethod
    def from_json_dict(cls, json_dict: dict[str, Any]) -> Self: ...

@bind_hass
@callback
def async_create_flow(hass: HomeAssistant, domain: str, context: ConfigFlowContext, data: Any, *, discovery_key: DiscoveryKey | None = None) -> None: ...
@callback
def _async_init_flow(hass: HomeAssistant, domain: str, context: ConfigFlowContext, data: Any) -> Coroutine[None, None, ConfigFlowResult] | None: ...

class PendingFlowKey(NamedTuple):
    domain: str
    source: str

class PendingFlowValue(NamedTuple):
    context: ConfigFlowContext
    data: Any

class FlowDispatcher:
    hass: Incomplete
    started: bool
    pending_flows: dict[PendingFlowKey, list[PendingFlowValue]]
    def __init__(self, hass: HomeAssistant) -> None: ...
    @callback
    def async_setup(self) -> None: ...
    async def _async_start(self, event: Event) -> None: ...
    @callback
    def async_create(self, domain: str, context: ConfigFlowContext, data: Any) -> None: ...
