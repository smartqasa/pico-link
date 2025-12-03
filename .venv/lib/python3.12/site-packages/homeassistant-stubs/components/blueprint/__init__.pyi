from . import websocket_api as websocket_api
from .const import CONF_USE_BLUEPRINT as CONF_USE_BLUEPRINT, DOMAIN as DOMAIN
from .errors import BlueprintException as BlueprintException, BlueprintInUse as BlueprintInUse, BlueprintWithNameException as BlueprintWithNameException, FailedToLoad as FailedToLoad, InvalidBlueprint as InvalidBlueprint, InvalidBlueprintInputs as InvalidBlueprintInputs, MissingInput as MissingInput
from .models import Blueprint as Blueprint, BlueprintInputs as BlueprintInputs, DomainBlueprints as DomainBlueprints
from .schemas import BLUEPRINT_INSTANCE_FIELDS as BLUEPRINT_INSTANCE_FIELDS, BLUEPRINT_SCHEMA as BLUEPRINT_SCHEMA, is_blueprint_instance_config as is_blueprint_instance_config
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType

CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
