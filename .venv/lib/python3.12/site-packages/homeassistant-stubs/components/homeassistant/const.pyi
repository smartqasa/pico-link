from .exposed_entities import ExposedEntities as ExposedEntities
from _typeshed import Incomplete
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Final

DOMAIN: Incomplete
DATA_EXPOSED_ENTITIES: HassKey[ExposedEntities]
DATA_STOP_HANDLER: Incomplete
SERVICE_HOMEASSISTANT_STOP: Final[str]
SERVICE_HOMEASSISTANT_RESTART: Final[str]
