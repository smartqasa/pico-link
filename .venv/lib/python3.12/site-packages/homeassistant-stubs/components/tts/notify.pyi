from . import ATTR_LANGUAGE as ATTR_LANGUAGE, ATTR_MEDIA_PLAYER_ENTITY_ID as ATTR_MEDIA_PLAYER_ENTITY_ID, ATTR_MESSAGE as ATTR_MESSAGE, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.notify import BaseNotificationService as BaseNotificationService
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, split_entity_id as split_entity_id
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

CONF_MEDIA_PLAYER: str
CONF_TTS_SERVICE: str
ENTITY_LEGACY_PROVIDER_GROUP: str
_LOGGER: Incomplete
PLATFORM_SCHEMA: Incomplete

async def async_get_service(hass: HomeAssistant, config: ConfigType, discovery_info: DiscoveryInfoType | None = None) -> TTSNotificationService: ...

class TTSNotificationService(BaseNotificationService):
    _target: str | None
    _tts_service: str | None
    _media_player: Incomplete
    _language: Incomplete
    def __init__(self, config: ConfigType) -> None: ...
    async def async_send_message(self, message: str = '', **kwargs: Any) -> None: ...
