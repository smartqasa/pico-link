import asyncio
from .const import CONF_COMMAND_TIMEOUT as CONF_COMMAND_TIMEOUT, LOGGER as LOGGER, TRIGGER_ENTITY_OPTIONS as TRIGGER_ENTITY_OPTIONS
from .sensor import CommandSensorData as CommandSensorData
from _typeshed import Incomplete
from datetime import datetime, timedelta
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity
from homeassistant.const import CONF_COMMAND as CONF_COMMAND, CONF_NAME as CONF_NAME, CONF_PAYLOAD_OFF as CONF_PAYLOAD_OFF, CONF_PAYLOAD_ON as CONF_PAYLOAD_ON, CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from homeassistant.helpers.template import Template as Template
from homeassistant.helpers.trigger_template_entity import ManualTriggerEntity as ManualTriggerEntity
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType

DEFAULT_NAME: str
DEFAULT_PAYLOAD_ON: str
DEFAULT_PAYLOAD_OFF: str
SCAN_INTERVAL: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class CommandBinarySensor(ManualTriggerEntity, BinarySensorEntity):
    _attr_should_poll: bool
    data: Incomplete
    _attr_is_on: Incomplete
    _payload_on: Incomplete
    _payload_off: Incomplete
    _value_template: Incomplete
    _scan_interval: Incomplete
    _process_updates: asyncio.Lock | None
    def __init__(self, data: CommandSensorData, config: ConfigType, payload_on: str, payload_off: str, value_template: Template | None, scan_interval: timedelta) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def _update_entity_state(self, now: datetime | None = None) -> None: ...
    async def _async_update(self) -> None: ...
    async def async_update(self) -> None: ...
