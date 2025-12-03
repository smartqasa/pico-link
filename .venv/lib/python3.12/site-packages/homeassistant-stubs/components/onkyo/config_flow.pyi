from .const import CONF_RECEIVER_MAX_VOLUME as CONF_RECEIVER_MAX_VOLUME, CONF_SOURCES as CONF_SOURCES, DOMAIN as DOMAIN, InputSource as InputSource, OPTION_INPUT_SOURCES as OPTION_INPUT_SOURCES, OPTION_MAX_VOLUME as OPTION_MAX_VOLUME, OPTION_MAX_VOLUME_DEFAULT as OPTION_MAX_VOLUME_DEFAULT, OPTION_VOLUME_RESOLUTION as OPTION_VOLUME_RESOLUTION, OPTION_VOLUME_RESOLUTION_DEFAULT as OPTION_VOLUME_RESOLUTION_DEFAULT, VOLUME_RESOLUTION_ALLOWED as VOLUME_RESOLUTION_ALLOWED
from .receiver import ReceiverInfo as ReceiverInfo, async_discover as async_discover, async_interview as async_interview
from _typeshed import Incomplete
from homeassistant.components import ssdp as ssdp
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow, SOURCE_RECONFIGURE as SOURCE_RECONFIGURE
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME
from homeassistant.core import callback as callback
from homeassistant.helpers.selector import NumberSelector as NumberSelector, NumberSelectorConfig as NumberSelectorConfig, NumberSelectorMode as NumberSelectorMode, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode, Selector as Selector, TextSelector as TextSelector
from typing import Any

_LOGGER: Incomplete
CONF_DEVICE: str
INPUT_SOURCES_ALL_MEANINGS: Incomplete
STEP_MANUAL_SCHEMA: Incomplete
STEP_CONFIGURE_SCHEMA: Incomplete

class OnkyoConfigFlow(ConfigFlow, domain=DOMAIN):
    _receiver_info: ReceiverInfo
    _discovered_infos: dict[str, ReceiverInfo]
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_manual(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_eiscp_discovery(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_ssdp(self, discovery_info: ssdp.SsdpServiceInfo) -> ConfigFlowResult: ...
    async def async_step_configure_receiver(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_import(self, user_input: dict[str, Any]) -> ConfigFlowResult: ...
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlow: ...

class OnkyoOptionsFlowHandler(OptionsFlow):
    _input_sources: Incomplete
    def __init__(self, config_entry: ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
