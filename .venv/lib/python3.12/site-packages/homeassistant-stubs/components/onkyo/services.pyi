from .const import DOMAIN as DOMAIN
from .media_player import OnkyoMediaPlayer as OnkyoMediaPlayer
from _typeshed import Incomplete
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.util.hass_dict import HassKey as HassKey

DATA_MP_ENTITIES: HassKey[dict[str, dict[str, OnkyoMediaPlayer]]]
ATTR_HDMI_OUTPUT: str
ACCEPTED_VALUES: Incomplete
ONKYO_SELECT_OUTPUT_SCHEMA: Incomplete
SERVICE_SELECT_HDMI_OUTPUT: str

async def async_register_services(hass: HomeAssistant) -> None: ...
