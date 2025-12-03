from .const import DOMAIN as DOMAIN
from .coordinator import EasyEnergyConfigEntry as EasyEnergyConfigEntry, EasyEnergyDataUpdateCoordinator as EasyEnergyDataUpdateCoordinator
from _typeshed import Incomplete
from datetime import date, datetime
from easyenergy import Electricity as Electricity, Gas as Gas
from enum import Enum
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers import selector as selector
from typing import Final

ATTR_CONFIG_ENTRY: Final[str]
ATTR_START: Final[str]
ATTR_END: Final[str]
ATTR_INCL_VAT: Final[str]
GAS_SERVICE_NAME: Final[str]
ENERGY_USAGE_SERVICE_NAME: Final[str]
ENERGY_RETURN_SERVICE_NAME: Final[str]
SERVICE_SCHEMA: Final[Incomplete]

class PriceType(str, Enum):
    ENERGY_USAGE = 'energy_usage'
    ENERGY_RETURN = 'energy_return'
    GAS = 'gas'

def __get_date(date_input: str | None) -> date | datetime: ...
def __serialize_prices(prices: list[dict[str, float | datetime]]) -> ServiceResponse: ...
def __get_coordinator(call: ServiceCall) -> EasyEnergyDataUpdateCoordinator: ...
async def __get_prices(call: ServiceCall, *, price_type: PriceType) -> ServiceResponse: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
