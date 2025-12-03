from .const import ATTR_APPLY_FILTER as ATTR_APPLY_FILTER, ATTR_KEEP_DAYS as ATTR_KEEP_DAYS, ATTR_REPACK as ATTR_REPACK, DOMAIN as DOMAIN
from .core import Recorder as Recorder
from .tasks import PurgeEntitiesTask as PurgeEntitiesTask, PurgeTask as PurgeTask
from _typeshed import Incomplete
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers.entityfilter import generate_filter as generate_filter
from homeassistant.helpers.service import async_extract_entity_ids as async_extract_entity_ids, async_register_admin_service as async_register_admin_service

SERVICE_PURGE: str
SERVICE_PURGE_ENTITIES: str
SERVICE_ENABLE: str
SERVICE_DISABLE: str
SERVICE_PURGE_SCHEMA: Incomplete
ATTR_DOMAINS: str
ATTR_ENTITY_GLOBS: str
SERVICE_PURGE_ENTITIES_SCHEMA: Incomplete
SERVICE_ENABLE_SCHEMA: Incomplete
SERVICE_DISABLE_SCHEMA: Incomplete

@callback
def _async_register_purge_service(hass: HomeAssistant, instance: Recorder) -> None: ...
@callback
def _async_register_purge_entities_service(hass: HomeAssistant, instance: Recorder) -> None: ...
@callback
def _async_register_enable_service(hass: HomeAssistant, instance: Recorder) -> None: ...
@callback
def _async_register_disable_service(hass: HomeAssistant, instance: Recorder) -> None: ...
@callback
def async_register_services(hass: HomeAssistant, instance: Recorder) -> None: ...
