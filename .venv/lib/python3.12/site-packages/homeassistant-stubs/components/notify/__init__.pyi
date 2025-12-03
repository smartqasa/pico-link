from .const import ATTR_DATA as ATTR_DATA, ATTR_MESSAGE as ATTR_MESSAGE, ATTR_RECIPIENTS as ATTR_RECIPIENTS, ATTR_TARGET as ATTR_TARGET, ATTR_TITLE as ATTR_TITLE, DOMAIN as DOMAIN, NOTIFY_SERVICE_SCHEMA as NOTIFY_SERVICE_SCHEMA, SERVICE_NOTIFY as SERVICE_NOTIFY, SERVICE_PERSISTENT_NOTIFICATION as SERVICE_PERSISTENT_NOTIFICATION, SERVICE_SEND_MESSAGE as SERVICE_SEND_MESSAGE
from .legacy import BaseNotificationService as BaseNotificationService, async_reload as async_reload, async_reset_platform as async_reset_platform, async_setup_legacy as async_setup_legacy
from .repairs import migrate_notify_issue as migrate_notify_issue
from _typeshed import Incomplete
from enum import IntFlag
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_PLATFORM as CONF_PLATFORM, STATE_UNAVAILABLE as STATE_UNAVAILABLE
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.hass_dict import HassKey as HassKey
from propcache import cached_property
from typing import Any, final, override

ATTR_TITLE_DEFAULT: str
DATA_COMPONENT: HassKey[EntityComponent[NotifyEntity]]
ENTITY_ID_FORMAT: Incomplete
MIN_TIME_BETWEEN_SCANS: Incomplete
_LOGGER: Incomplete
PLATFORM_SCHEMA: Incomplete

class NotifyEntityFeature(IntFlag):
    TITLE = 1

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class NotifyEntityDescription(EntityDescription, frozen_or_thawed=True): ...

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class NotifyEntity(RestoreEntity):
    entity_description: NotifyEntityDescription
    _attr_supported_features: NotifyEntityFeature
    _attr_should_poll: bool
    _attr_device_class: None
    _attr_state: None
    __last_notified_isoformat: str | None
    @cached_property
    @final
    @override
    def state(self) -> str | None: ...
    def __set_state(self, state: str | None) -> None: ...
    async def async_internal_added_to_hass(self) -> None: ...
    @final
    async def _async_send_message(self, **kwargs: Any) -> None: ...
    def send_message(self, message: str, title: str | None = None) -> None: ...
    async def async_send_message(self, message: str, title: str | None = None) -> None: ...
