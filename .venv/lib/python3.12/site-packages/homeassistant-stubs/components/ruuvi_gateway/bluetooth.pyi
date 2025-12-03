from .coordinator import RuuviGatewayUpdateCoordinator as RuuviGatewayUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.bluetooth import BaseHaRemoteScanner as BaseHaRemoteScanner, FALLBACK_MAXIMUM_STALE_ADVERTISEMENT_SECONDS as FALLBACK_MAXIMUM_STALE_ADVERTISEMENT_SECONDS, MONOTONIC_TIME as MONOTONIC_TIME, async_register_scanner as async_register_scanner
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback

_LOGGER: Incomplete

class RuuviGatewayScanner(BaseHaRemoteScanner):
    coordinator: Incomplete
    def __init__(self, scanner_id: str, name: str, *, coordinator: RuuviGatewayUpdateCoordinator) -> None: ...
    @callback
    def _async_handle_new_data(self) -> None: ...
    @callback
    def start_polling(self) -> CALLBACK_TYPE: ...

def async_connect_scanner(hass: HomeAssistant, entry: ConfigEntry, coordinator: RuuviGatewayUpdateCoordinator) -> tuple[RuuviGatewayScanner, CALLBACK_TYPE]: ...
