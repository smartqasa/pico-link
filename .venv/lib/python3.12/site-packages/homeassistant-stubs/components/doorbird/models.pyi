from .device import ConfiguredDoorBird as ConfiguredDoorBird
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from typing import Any

type DoorBirdConfigEntry = ConfigEntry[DoorBirdData]
@dataclass
class DoorBirdData:
    door_station: ConfiguredDoorBird
    door_station_info: dict[str, Any]
    event_entity_ids: dict[str, str]
