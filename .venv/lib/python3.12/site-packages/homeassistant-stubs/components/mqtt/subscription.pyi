from . import debug_info as debug_info
from .client import async_subscribe_internal as async_subscribe_internal
from .const import DEFAULT_QOS as DEFAULT_QOS
from .models import MessageCallbackType as MessageCallbackType
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.core import HassJobType as HassJobType, HomeAssistant as HomeAssistant, callback as callback
from typing import Any

@dataclass(slots=True, kw_only=True)
class EntitySubscription:
    hass: HomeAssistant
    topic: str | None
    message_callback: MessageCallbackType
    should_subscribe: bool | None
    unsubscribe_callback: Callable[[], None] | None
    qos: int = ...
    encoding: str = ...
    entity_id: str | None
    job_type: HassJobType | None
    def resubscribe_if_necessary(self, hass: HomeAssistant, other: EntitySubscription | None) -> None: ...
    @callback
    def subscribe(self) -> None: ...
    def _should_resubscribe(self, other: EntitySubscription | None) -> bool: ...

@callback
def async_prepare_subscribe_topics(hass: HomeAssistant, sub_state: dict[str, EntitySubscription] | None, topics: dict[str, dict[str, Any]]) -> dict[str, EntitySubscription]: ...
async def async_subscribe_topics(hass: HomeAssistant, sub_state: dict[str, EntitySubscription]) -> None: ...
@callback
def async_subscribe_topics_internal(hass: HomeAssistant, sub_state: dict[str, EntitySubscription]) -> None: ...
def async_unsubscribe_topics(hass: HomeAssistant, sub_state: dict[str, EntitySubscription] | None) -> dict[str, EntitySubscription]: ...

async_unsubscribe_topics: Incomplete
