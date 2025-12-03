from . import HomeworksData as HomeworksData
from .const import CONF_ADDR as CONF_ADDR, CONF_BUTTONS as CONF_BUTTONS, CONF_CONTROLLER_ID as CONF_CONTROLLER_ID, CONF_KEYPADS as CONF_KEYPADS, CONF_NUMBER as CONF_NUMBER, CONF_RELEASE_DELAY as CONF_RELEASE_DELAY, DOMAIN as DOMAIN
from .entity import HomeworksEntity as HomeworksEntity
from _typeshed import Incomplete
from homeassistant.components.button import ButtonEntity as ButtonEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyhomeworks.pyhomeworks import Homeworks as Homeworks

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HomeworksButton(HomeworksEntity, ButtonEntity):
    _attr_device_info: Incomplete
    _release_delay: Incomplete
    def __init__(self, controller: Homeworks, controller_id: str, addr: str, keypad_name: str, button_name: str, button_number: int, release_delay: float) -> None: ...
    async def async_press(self) -> None: ...
