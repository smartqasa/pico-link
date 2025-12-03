from .const import CONF_APP_ID as CONF_APP_ID, DOMAIN as DOMAIN
from .entity import TTNEntity as TTNEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from ttn_client import TTNSensorValue

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TtnDataSensor(TTNEntity, SensorEntity):
    _ttn_value: TTNSensorValue
    @property
    def native_value(self) -> StateType: ...
