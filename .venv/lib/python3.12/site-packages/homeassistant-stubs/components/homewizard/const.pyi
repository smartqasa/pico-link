from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.const import Platform as Platform
from homewizard_energy.v1.models import Data as Data, Device as Device, State as State, System as System

DOMAIN: str
PLATFORMS: Incomplete
LOGGER: Incomplete
CONF_API_ENABLED: str
CONF_DATA: str
CONF_PRODUCT_NAME: str
CONF_PRODUCT_TYPE: str
CONF_SERIAL: str
UPDATE_INTERVAL: Incomplete

@dataclass
class DeviceResponseEntry:
    device: Device
    data: Data
    state: State | None = ...
    system: System | None = ...
