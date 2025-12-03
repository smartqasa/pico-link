import asyncio
from .const import DATA_CLOUD as DATA_CLOUD, DOMAIN as DOMAIN
from .subscription import async_migrate_paypal_agreement as async_migrate_paypal_agreement, async_subscription_info as async_subscription_info
from homeassistant.components.repairs import ConfirmRepairFlow as ConfirmRepairFlow, RepairsFlow as RepairsFlow, repairs_flow_manager as repairs_flow_manager
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

BACKOFF_TIME: int
MAX_RETRIES: int

@callback
def async_manage_legacy_subscription_issue(hass: HomeAssistant, subscription_info: dict[str, Any]) -> None: ...

class LegacySubscriptionRepairFlow(RepairsFlow):
    wait_task: asyncio.Task | None
    _data: dict[str, Any] | None
    async def async_step_init(self, _: None = None) -> FlowResult: ...
    async def async_step_confirm_change_plan(self, user_input: dict[str, str] | None = None) -> FlowResult: ...
    async def async_step_change_plan(self, _: None = None) -> FlowResult: ...
    async def async_step_complete(self, _: None = None) -> FlowResult: ...
    async def async_step_timeout(self, _: None = None) -> FlowResult: ...

async def async_create_fix_flow(hass: HomeAssistant, issue_id: str, data: dict[str, str | int | float | None] | None) -> RepairsFlow: ...
