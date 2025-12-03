from . import HomeworksData as HomeworksData, HomeworksKeypad as HomeworksKeypad
from .const import CONF_ADDR as CONF_ADDR, CONF_BUTTONS as CONF_BUTTONS, CONF_CONTROLLER_ID as CONF_CONTROLLER_ID, CONF_KEYPADS as CONF_KEYPADS, CONF_LED as CONF_LED, CONF_NUMBER as CONF_NUMBER, DOMAIN as DOMAIN
from .entity import HomeworksEntity as HomeworksEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyhomeworks.pyhomeworks import Homeworks as Homeworks
from typing import Any

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HomeworksBinarySensor(HomeworksEntity, BinarySensorEntity):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    _keypad: Incomplete
    def __init__(self, controller: Homeworks, keypad: HomeworksKeypad, controller_id: str, addr: str, keypad_name: str, button_name: str, led_number: int) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_is_on: Incomplete
    @callback
    def _update_callback(self, msg_type: str, values: list[Any]) -> None: ...
