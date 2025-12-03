from .const import CurrentTemperatureSelector as CurrentTemperatureSelector, DEFAULT_CURRENT_TEMP_SELECTOR as DEFAULT_CURRENT_TEMP_SELECTOR, DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DEFAULT_TARGET_TEMP_SELECTOR as DEFAULT_TARGET_TEMP_SELECTOR, TargetTemperatureSelector as TargetTemperatureSelector
from dataclasses import dataclass
from eq3btsmart.thermostat import Thermostat as Thermostat

@dataclass(slots=True)
class Eq3Config:
    mac_address: str
    current_temp_selector: CurrentTemperatureSelector = ...
    target_temp_selector: TargetTemperatureSelector = ...
    external_temp_sensor: str = ...
    scan_interval: int = ...

@dataclass(slots=True)
class Eq3ConfigEntryData:
    eq3_config: Eq3Config
    thermostat: Thermostat
