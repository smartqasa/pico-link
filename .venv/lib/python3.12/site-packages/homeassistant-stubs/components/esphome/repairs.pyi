from homeassistant.components.assist_pipeline.repair_flows import AssistInProgressDeprecatedRepairFlow as AssistInProgressDeprecatedRepairFlow
from homeassistant.components.repairs import RepairsFlow as RepairsFlow
from homeassistant.core import HomeAssistant as HomeAssistant

async def async_create_fix_flow(hass: HomeAssistant, issue_id: str, data: dict[str, str | int | float | None] | None) -> RepairsFlow: ...
