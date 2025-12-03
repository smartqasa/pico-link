from _typeshed import Incomplete
from homeassistant.components.repairs import RepairsFlow as RepairsFlow
from homeassistant.data_entry_flow import FlowResult as FlowResult

REQUIRED_KEYS: Incomplete

class AssistInProgressDeprecatedRepairFlow(RepairsFlow):
    _data: Incomplete
    def __init__(self, data: dict[str, str | int | float | None] | None) -> None: ...
    async def async_step_init(self, _: None = None) -> FlowResult: ...
    async def async_step_confirm_disable_entity(self, user_input: dict[str, str] | None = None) -> FlowResult: ...
