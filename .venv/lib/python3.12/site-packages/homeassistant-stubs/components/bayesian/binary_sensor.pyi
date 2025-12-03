from . import DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .const import ATTR_OBSERVATIONS as ATTR_OBSERVATIONS, ATTR_OCCURRED_OBSERVATION_ENTITIES as ATTR_OCCURRED_OBSERVATION_ENTITIES, ATTR_PROBABILITY as ATTR_PROBABILITY, ATTR_PROBABILITY_THRESHOLD as ATTR_PROBABILITY_THRESHOLD, CONF_NUMERIC_STATE as CONF_NUMERIC_STATE, CONF_OBSERVATIONS as CONF_OBSERVATIONS, CONF_PRIOR as CONF_PRIOR, CONF_PROBABILITY_THRESHOLD as CONF_PROBABILITY_THRESHOLD, CONF_P_GIVEN_F as CONF_P_GIVEN_F, CONF_P_GIVEN_T as CONF_P_GIVEN_T, CONF_TEMPLATE as CONF_TEMPLATE, CONF_TO_STATE as CONF_TO_STATE, DEFAULT_NAME as DEFAULT_NAME, DEFAULT_PROBABILITY_THRESHOLD as DEFAULT_PROBABILITY_THRESHOLD
from .helpers import Observation as Observation
from .issues import raise_mirrored_entries as raise_mirrored_entries, raise_no_prob_given_false as raise_no_prob_given_false
from _typeshed import Incomplete
from collections import OrderedDict
from collections.abc import Callable as Callable
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.const import CONF_ABOVE as CONF_ABOVE, CONF_BELOW as CONF_BELOW, CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_NAME as CONF_NAME, CONF_PLATFORM as CONF_PLATFORM, CONF_STATE as CONF_STATE, CONF_UNIQUE_ID as CONF_UNIQUE_ID, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import Event as Event, EventStateChangedData as EventStateChangedData, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConditionError as ConditionError, TemplateError as TemplateError
from homeassistant.helpers import condition as condition
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import TrackTemplate as TrackTemplate, TrackTemplateResult as TrackTemplateResult, TrackTemplateResultInfo as TrackTemplateResultInfo, async_track_state_change_event as async_track_state_change_event, async_track_template_result as async_track_template_result
from homeassistant.helpers.reload import async_setup_reload_service as async_setup_reload_service
from homeassistant.helpers.template import Template as Template, result_as_boolean as result_as_boolean
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any
from uuid import UUID

_LOGGER: Incomplete

def _above_greater_than_below(config: dict[str, Any]) -> dict[str, Any]: ...

NUMERIC_STATE_SCHEMA: Incomplete

def _no_overlapping(configs: list[dict]) -> list[dict]: ...

STATE_SCHEMA: Incomplete
TEMPLATE_SCHEMA: Incomplete
PLATFORM_SCHEMA: Incomplete

def update_probability(prior: float, prob_given_true: float, prob_given_false: float) -> float: ...
async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class BayesianBinarySensor(BinarySensorEntity):
    _attr_should_poll: bool
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _observations: Incomplete
    _probability_threshold: Incomplete
    _attr_device_class: Incomplete
    _attr_is_on: bool
    _callbacks: list[TrackTemplateResultInfo]
    prior: Incomplete
    probability: Incomplete
    current_observations: OrderedDict[UUID, Observation]
    observations_by_entity: Incomplete
    observations_by_template: Incomplete
    observation_handlers: dict[str, Callable[[Observation, bool], bool | None]]
    def __init__(self, name: str, unique_id: str | None, prior: float, observations: list[ConfigType], probability_threshold: float, device_class: BinarySensorDeviceClass | None) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _recalculate_and_write_state(self) -> None: ...
    def _initialize_current_observations(self) -> OrderedDict[UUID, Observation]: ...
    def _record_entity_observations(self, entity: str) -> OrderedDict[UUID, Observation]: ...
    def _calculate_new_probability(self) -> float: ...
    def _build_observations_by_entity(self) -> dict[str, list[Observation]]: ...
    def _build_observations_by_template(self) -> dict[Template, list[Observation]]: ...
    def _process_numeric_state(self, entity_observation: Observation, multi: bool = False) -> bool | None: ...
    def _process_state(self, entity_observation: Observation, multi: bool = False) -> bool | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    async def async_update(self) -> None: ...
