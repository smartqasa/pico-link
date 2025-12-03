import uuid
from .const import CONF_P_GIVEN_F as CONF_P_GIVEN_F, CONF_P_GIVEN_T as CONF_P_GIVEN_T, CONF_TO_STATE as CONF_TO_STATE
from dataclasses import dataclass, field
from homeassistant.const import CONF_ABOVE as CONF_ABOVE, CONF_BELOW as CONF_BELOW, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_PLATFORM as CONF_PLATFORM, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE
from homeassistant.helpers.template import Template as Template

@dataclass
class Observation:
    entity_id: str | None
    platform: str
    prob_given_true: float
    prob_given_false: float
    to_state: str | None
    above: float | None
    below: float | None
    value_template: Template | None
    observed: bool | None = ...
    multi: bool = ...
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    def to_dict(self) -> dict[str, str | float | bool | None]: ...
    def is_mirror(self, other: Observation) -> bool: ...
    @property
    def template(self) -> str | None: ...
