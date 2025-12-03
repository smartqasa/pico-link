from .const import DOMAIN as DOMAIN
from .entity import HuaweiLteBaseEntityWithDevice as HuaweiLteBaseEntityWithDevice
from _typeshed import Incomplete
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import entity_platform as entity_platform

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: entity_platform.AddEntitiesCallback) -> None: ...

class BaseButton(HuaweiLteBaseEntityWithDevice, ButtonEntity):
    @property
    def _device_unique_id(self) -> str: ...
    async def async_update(self) -> None: ...
    def press(self) -> None: ...
    def _press(self) -> str: ...

BUTTON_KEY_CLEAR_TRAFFIC_STATISTICS: str

class ClearTrafficStatisticsButton(BaseButton):
    entity_description: Incomplete
    def _press(self) -> str: ...

BUTTON_KEY_RESTART: str

class RestartButton(BaseButton):
    entity_description: Incomplete
    def _press(self) -> str: ...
