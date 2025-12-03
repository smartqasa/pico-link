import asyncio
from .entity import AssistSatelliteEntity as AssistSatelliteEntity
from enum import IntFlag
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.util.hass_dict import HassKey as HassKey

DOMAIN: str
DATA_COMPONENT: HassKey[EntityComponent[AssistSatelliteEntity]]
CONNECTION_TEST_DATA: HassKey[dict[str, asyncio.Event]]

class AssistSatelliteEntityFeature(IntFlag):
    ANNOUNCE = 1
