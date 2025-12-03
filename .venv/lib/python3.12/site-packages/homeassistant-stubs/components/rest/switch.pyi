import httpx
from _typeshed import Incomplete
from homeassistant.components.switch import DEVICE_CLASSES_SCHEMA as DEVICE_CLASSES_SCHEMA, SwitchEntity as SwitchEntity
from homeassistant.const import CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_HEADERS as CONF_HEADERS, CONF_ICON as CONF_ICON, CONF_METHOD as CONF_METHOD, CONF_NAME as CONF_NAME, CONF_PARAMS as CONF_PARAMS, CONF_PASSWORD as CONF_PASSWORD, CONF_RESOURCE as CONF_RESOURCE, CONF_TIMEOUT as CONF_TIMEOUT, CONF_UNIQUE_ID as CONF_UNIQUE_ID, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import PlatformNotReady as PlatformNotReady
from homeassistant.helpers import template as template
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from homeassistant.helpers.trigger_template_entity import CONF_AVAILABILITY as CONF_AVAILABILITY, CONF_PICTURE as CONF_PICTURE, ManualTriggerEntity as ManualTriggerEntity, TEMPLATE_ENTITY_BASE_SCHEMA as TEMPLATE_ENTITY_BASE_SCHEMA
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Incomplete
CONF_BODY_OFF: str
CONF_BODY_ON: str
CONF_IS_ON_TEMPLATE: str
CONF_STATE_RESOURCE: str
TRIGGER_ENTITY_OPTIONS: Incomplete
DEFAULT_METHOD: str
DEFAULT_BODY_OFF: str
DEFAULT_BODY_ON: str
DEFAULT_NAME: str
DEFAULT_TIMEOUT: int
DEFAULT_VERIFY_SSL: bool
SUPPORT_REST_METHODS: Incomplete
PLATFORM_SCHEMA: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class RestSwitch(ManualTriggerEntity, SwitchEntity):
    _resource: str
    _state_resource: str
    _method: str
    _headers: dict[str, template.Template] | None
    _params: dict[str, template.Template] | None
    _auth: Incomplete
    _body_on: template.Template
    _body_off: template.Template
    _is_on_template: template.Template | None
    _timeout: int
    _verify_ssl: bool
    def __init__(self, hass: HomeAssistant, config: ConfigType, trigger_entity_config: ConfigType) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_is_on: bool
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def set_device_state(self, body: Any) -> httpx.Response: ...
    async def async_update(self) -> None: ...
    async def get_device_state(self, hass: HomeAssistant) -> httpx.Response: ...
