import ssl
from .const import CONF_BUFFER_SIZE as CONF_BUFFER_SIZE, CONF_VALUE_ON as CONF_VALUE_ON
from .model import TcpSensorConfig as TcpSensorConfig
from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, CONF_PAYLOAD as CONF_PAYLOAD, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL, CONF_TIMEOUT as CONF_TIMEOUT, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import TemplateError as TemplateError
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Final

_LOGGER: Final[Incomplete]

class TcpEntity(Entity):
    _hass: Incomplete
    _config: TcpSensorConfig
    _ssl_context: ssl.SSLContext | None
    _state: str | None
    def __init__(self, hass: HomeAssistant, config: ConfigType) -> None: ...
    @property
    def name(self) -> str: ...
    def update(self) -> None: ...
