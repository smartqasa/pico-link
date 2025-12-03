from .const import DOMAIN as DOMAIN
from .entity import TailscaleEntity as TailscaleEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from tailscale import Device as TailscaleDevice

@dataclass(frozen=True, kw_only=True)
class TailscaleSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[TailscaleDevice], datetime | str | None]

SENSORS: tuple[TailscaleSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TailscaleSensorEntity(TailscaleEntity, SensorEntity):
    entity_description: TailscaleSensorEntityDescription
    @property
    def native_value(self) -> datetime | str | None: ...
