from .const import CONF_COLUMN_NAME as CONF_COLUMN_NAME, CONF_QUERY as CONF_QUERY, DOMAIN as DOMAIN
from .models import SQLData as SQLData
from .util import redact_credentials as redact_credentials, resolve_db_url as resolve_db_url
from _typeshed import Incomplete
from homeassistant.components.recorder import CONF_DB_URL as CONF_DB_URL, SupportedDialect as SupportedDialect, get_instance as get_instance
from homeassistant.components.sensor import CONF_STATE_CLASS as CONF_STATE_CLASS
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_ICON as CONF_ICON, CONF_NAME as CONF_NAME, CONF_UNIQUE_ID as CONF_UNIQUE_ID, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, MATCH_ALL as MATCH_ALL
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import TemplateError as TemplateError
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.template import Template as Template
from homeassistant.helpers.trigger_template_entity import CONF_AVAILABILITY as CONF_AVAILABILITY, CONF_PICTURE as CONF_PICTURE, ManualTriggerSensorEntity as ManualTriggerSensorEntity
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from sqlalchemy.engine import Result as Result
from sqlalchemy.orm import Session as Session, scoped_session
from sqlalchemy.sql.lambdas import StatementLambdaElement as StatementLambdaElement
from sqlalchemy.util import LRUCache
from typing import Any

_LOGGER: Incomplete
_SQL_LAMBDA_CACHE: LRUCache
TRIGGER_ENTITY_OPTIONS: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
@callback
def _async_get_or_init_domain_data(hass: HomeAssistant) -> SQLData: ...
async def async_setup_sensor(hass: HomeAssistant, trigger_entity_config: ConfigType, query_str: str, column_name: str, value_template: Template | None, unique_id: str | None, db_url: str, yaml: bool, async_add_entities: AddEntitiesCallback) -> None: ...
def _validate_and_get_session_maker_for_db_url(db_url: str) -> scoped_session | None: ...
def _generate_lambda_stmt(query: str) -> StatementLambdaElement: ...

class SQLSensor(ManualTriggerSensorEntity):
    _unrecorded_attributes: Incomplete
    _query: Incomplete
    _template: Incomplete
    _column_name: Incomplete
    sessionmaker: Incomplete
    _attr_extra_state_attributes: Incomplete
    _use_database_executor: Incomplete
    _lambda_stmt: Incomplete
    _attr_name: Incomplete
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, trigger_entity_config: ConfigType, sessmaker: scoped_session, query: str, column: str, value_template: Template | None, yaml: bool, use_database_executor: bool) -> None: ...
    @property
    def name(self) -> str | None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any] | None: ...
    async def async_update(self) -> None: ...
    _attr_native_value: Incomplete
    def _update(self) -> Any: ...
