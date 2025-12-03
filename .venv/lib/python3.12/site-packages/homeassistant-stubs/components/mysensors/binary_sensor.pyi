from . import setup_mysensors_platform as setup_mysensors_platform
from .const import DiscoveryInfo as DiscoveryInfo, MYSENSORS_DISCOVERY as MYSENSORS_DISCOVERY
from .entity import MySensorsChildEntity as MySensorsChildEntity
from .helpers import on_unload as on_unload
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

@dataclass(frozen=True)
class MySensorsBinarySensorDescription(BinarySensorEntityDescription):
    is_on: Callable[[int, dict[int, str]], bool] = ...

SENSORS: dict[str, MySensorsBinarySensorDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MySensorsBinarySensor(MySensorsChildEntity, BinarySensorEntity):
    entity_description: MySensorsBinarySensorDescription
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @property
    def is_on(self) -> bool: ...
