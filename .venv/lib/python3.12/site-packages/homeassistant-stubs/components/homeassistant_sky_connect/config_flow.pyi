from .const import DOCS_WEB_FLASHER_URL as DOCS_WEB_FLASHER_URL, DOMAIN as DOMAIN, HardwareVariant as HardwareVariant
from .util import get_hardware_variant as get_hardware_variant, get_usb_service_info as get_usb_service_info
from _typeshed import Incomplete
from homeassistant.components import usb as usb
from homeassistant.components.homeassistant_hardware import firmware_config_flow as firmware_config_flow, silabs_multiprotocol_addon as silabs_multiprotocol_addon
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryBaseFlow as ConfigEntryBaseFlow, ConfigFlowContext as ConfigFlowContext, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.core import callback as callback
from typing import Any, Protocol

_LOGGER: Incomplete

class TranslationPlaceholderProtocol(Protocol):
    def _get_translation_placeholders(self) -> dict[str, str]: ...

class SkyConnectTranslationMixin(ConfigEntryBaseFlow, TranslationPlaceholderProtocol):
    context: ConfigFlowContext
    def _get_translation_placeholders(self) -> dict[str, str]: ...

class HomeAssistantSkyConnectConfigFlow(SkyConnectTranslationMixin, firmware_config_flow.BaseFirmwareConfigFlow, domain=DOMAIN):
    VERSION: int
    MINOR_VERSION: int
    _usb_info: usb.UsbServiceInfo | None
    _hw_variant: HardwareVariant | None
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlow: ...
    _device: Incomplete
    _hardware_name: Incomplete
    async def async_step_usb(self, discovery_info: usb.UsbServiceInfo) -> ConfigFlowResult: ...
    def _async_flow_finished(self) -> ConfigFlowResult: ...

class HomeAssistantSkyConnectMultiPanOptionsFlowHandler(silabs_multiprotocol_addon.OptionsFlowHandler):
    async def _async_serial_port_settings(self) -> silabs_multiprotocol_addon.SerialPortSettings: ...
    async def _async_zha_physical_discovery(self) -> dict[str, Any]: ...
    @property
    def _hw_variant(self) -> HardwareVariant: ...
    def _zha_name(self) -> str: ...
    def _hardware_name(self) -> str: ...
    async def async_step_flashing_complete(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class HomeAssistantSkyConnectOptionsFlowHandler(SkyConnectTranslationMixin, firmware_config_flow.BaseFirmwareOptionsFlow):
    _usb_info: Incomplete
    _hw_variant: Incomplete
    _hardware_name: Incomplete
    _device: Incomplete
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def _async_flow_finished(self) -> ConfigFlowResult: ...
