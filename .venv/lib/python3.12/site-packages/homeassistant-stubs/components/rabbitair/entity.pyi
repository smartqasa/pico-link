from .const import DOMAIN as DOMAIN
from .coordinator import RabbitAirDataUpdateCoordinator as RabbitAirDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_MAC as CONF_MAC
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from rabbitair import Model
from typing import Any

_LOGGER: Incomplete
MODELS: Incomplete

class RabbitAirBaseEntity(CoordinatorEntity[RabbitAirDataUpdateCoordinator]):
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: RabbitAirDataUpdateCoordinator, entry: ConfigEntry) -> None: ...
    def _is_model(self, model: Model | list[Model]) -> bool: ...
    async def _set_state(self, **kwargs: Any) -> None: ...
