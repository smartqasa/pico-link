import logging
from _typeshed import Incomplete
from homeassistant.const import CONCENTRATION_PARTS_PER_BILLION as CONCENTRATION_PARTS_PER_BILLION, CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, DEGREE as DEGREE, LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, Platform as Platform, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfIrradiance as UnitOfIrradiance, UnitOfLength as UnitOfLength, UnitOfPower as UnitOfPower, UnitOfPressure as UnitOfPressure, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime, UnitOfVolume as UnitOfVolume, UnitOfVolumeFlowRate as UnitOfVolumeFlowRate
from pyoverkiz.enums import UIClass, UIWidget
from typing import Final

DOMAIN: Final[str]
LOGGER: logging.Logger
CONF_API_TYPE: Final[str]
CONF_HUB: Final[str]
DEFAULT_SERVER: Final[Incomplete]
DEFAULT_HOST: Final[str]
UPDATE_INTERVAL: Final[Incomplete]
UPDATE_INTERVAL_ALL_ASSUMED_STATE: Final[Incomplete]
PLATFORMS: list[Platform]
IGNORED_OVERKIZ_DEVICES: list[UIClass | UIWidget]
OVERKIZ_DEVICE_TO_PLATFORM: dict[UIClass | UIWidget, Platform | None]
OVERKIZ_STATE_TO_TRANSLATION: dict[str, str]
OVERKIZ_UNIT_TO_HA: dict[str, str]
