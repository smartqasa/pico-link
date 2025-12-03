from _typeshed import Incomplete
from homeassistant.components.button import ButtonEntity as ButtonEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_BROADCAST_ADDRESS as CONF_BROADCAST_ADDRESS, CONF_BROADCAST_PORT as CONF_BROADCAST_PORT, CONF_MAC as CONF_MAC
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WolButton(ButtonEntity):
    _attr_name: Incomplete
    _mac_address: Incomplete
    _broadcast_address: Incomplete
    _broadcast_port: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, name: str, mac_address: str, broadcast_address: str | None, broadcast_port: int | None) -> None: ...
    async def async_press(self) -> None: ...
