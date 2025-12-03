from .const import CONF_ALERT_MESSAGE as CONF_ALERT_MESSAGE, CONF_CAN_ACK as CONF_CAN_ACK, CONF_DATA as CONF_DATA, CONF_DONE_MESSAGE as CONF_DONE_MESSAGE, CONF_NOTIFIERS as CONF_NOTIFIERS, CONF_SKIP_FIRST as CONF_SKIP_FIRST, CONF_TITLE as CONF_TITLE, DEFAULT_CAN_ACK as DEFAULT_CAN_ACK, DEFAULT_SKIP_FIRST as DEFAULT_SKIP_FIRST, DOMAIN as DOMAIN, LOGGER as LOGGER
from .entity import AlertEntity as AlertEntity
from _typeshed import Incomplete
from homeassistant.const import CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_NAME as CONF_NAME, CONF_REPEAT as CONF_REPEAT, CONF_STATE as CONF_STATE, SERVICE_TOGGLE as SERVICE_TOGGLE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType

ALERT_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
