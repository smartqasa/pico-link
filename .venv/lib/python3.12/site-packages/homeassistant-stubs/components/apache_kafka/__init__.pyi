import json
from _typeshed import Incomplete
from homeassistant.const import CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_USERNAME as CONF_USERNAME, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, EVENT_STATE_CHANGED as EVENT_STATE_CHANGED
from homeassistant.core import Event as Event, EventStateChangedData as EventStateChangedData, HomeAssistant as HomeAssistant
from homeassistant.helpers.entityfilter import EntityFilter as EntityFilter, FILTER_SCHEMA as FILTER_SCHEMA
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any, Literal

DOMAIN: str
CONF_FILTER: str
CONF_TOPIC: str
CONF_SECURITY_PROTOCOL: str
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class DateTimeJSONEncoder(json.JSONEncoder):
    def default(self, o: Any) -> str: ...

class KafkaManager:
    _encoder: Incomplete
    _entities_filter: Incomplete
    _hass: Incomplete
    _producer: Incomplete
    _topic: Incomplete
    def __init__(self, hass: HomeAssistant, ip_address: str, port: int, topic: str, entities_filter: EntityFilter, security_protocol: Literal['PLAINTEXT', 'SSL', 'SASL_SSL'], username: str | None, password: str | None) -> None: ...
    def _encode_event(self, event: Event[EventStateChangedData]) -> bytes | None: ...
    async def start(self) -> None: ...
    async def shutdown(self, _: Event) -> None: ...
    async def write(self, event: Event[EventStateChangedData]) -> None: ...
