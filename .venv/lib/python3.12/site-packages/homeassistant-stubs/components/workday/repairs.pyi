from .config_flow import validate_custom_dates as validate_custom_dates
from .const import CONF_PROVINCE as CONF_PROVINCE, CONF_REMOVE_HOLIDAYS as CONF_REMOVE_HOLIDAYS
from _typeshed import Incomplete
from homeassistant import data_entry_flow as data_entry_flow
from homeassistant.components.repairs import ConfirmRepairFlow as ConfirmRepairFlow, RepairsFlow as RepairsFlow
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_COUNTRY as CONF_COUNTRY
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.selector import SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode
from typing import Any

class CountryFixFlow(RepairsFlow):
    entry: Incomplete
    country: str | None
    def __init__(self, entry: ConfigEntry, country: str | None) -> None: ...
    async def async_step_init(self, user_input: dict[str, str] | None = None) -> data_entry_flow.FlowResult: ...
    async def async_step_country(self, user_input: dict[str, Any] | None = None) -> data_entry_flow.FlowResult: ...
    async def async_step_province(self, user_input: dict[str, Any] | None = None) -> data_entry_flow.FlowResult: ...

class HolidayFixFlow(RepairsFlow):
    entry: Incomplete
    country: str | None
    named_holiday: str
    def __init__(self, entry: ConfigEntry, country: str | None, named_holiday: str) -> None: ...
    async def async_step_init(self, user_input: dict[str, str] | None = None) -> data_entry_flow.FlowResult: ...
    async def async_step_fix_remove_holiday(self, user_input: dict[str, Any] | None = None) -> data_entry_flow.FlowResult: ...

async def async_create_fix_flow(hass: HomeAssistant, issue_id: str, data: dict[str, Any] | None) -> RepairsFlow: ...
