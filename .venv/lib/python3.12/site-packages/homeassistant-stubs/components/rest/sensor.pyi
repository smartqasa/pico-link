from . import async_get_config_and_coordinator as async_get_config_and_coordinator, create_rest_data_from_config as create_rest_data_from_config
from .const import CONF_JSON_ATTRS as CONF_JSON_ATTRS, CONF_JSON_ATTRS_PATH as CONF_JSON_ATTRS_PATH, DEFAULT_SENSOR_NAME as DEFAULT_SENSOR_NAME
from .data import RestData as RestData
from .entity import RestEntity as RestEntity
from .schema import RESOURCE_SCHEMA as RESOURCE_SCHEMA, SENSOR_SCHEMA as SENSOR_SCHEMA
from .util import parse_json_attributes as parse_json_attributes
from _typeshed import Incomplete
from homeassistant.components.sensor import CONF_STATE_CLASS as CONF_STATE_CLASS, SensorDeviceClass as SensorDeviceClass
from homeassistant.components.sensor.helpers import async_parse_date_datetime as async_parse_date_datetime
from homeassistant.const import CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_FORCE_UPDATE as CONF_FORCE_UPDATE, CONF_ICON as CONF_ICON, CONF_NAME as CONF_NAME, CONF_RESOURCE as CONF_RESOURCE, CONF_RESOURCE_TEMPLATE as CONF_RESOURCE_TEMPLATE, CONF_UNIQUE_ID as CONF_UNIQUE_ID, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import PlatformNotReady as PlatformNotReady
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.template import Template as Template
from homeassistant.helpers.trigger_template_entity import CONF_AVAILABILITY as CONF_AVAILABILITY, CONF_PICTURE as CONF_PICTURE, ManualTriggerSensorEntity as ManualTriggerSensorEntity
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

_LOGGER: Incomplete
PLATFORM_SCHEMA: Incomplete
TRIGGER_ENTITY_OPTIONS: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class RestSensor(ManualTriggerSensorEntity, RestEntity):
    _value_template: Incomplete
    _json_attrs: Incomplete
    _json_attrs_path: Incomplete
    _attr_extra_state_attributes: Incomplete
    def __init__(self, hass: HomeAssistant, coordinator: DataUpdateCoordinator[None] | None, rest: RestData, config: ConfigType, trigger_entity_config: ConfigType) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    _attr_native_value: Incomplete
    def _update_from_rest_data(self) -> None: ...
