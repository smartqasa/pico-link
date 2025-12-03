from .coordinator import AnovaCoordinator as AnovaCoordinator
from anova_wifi import AnovaApi as AnovaApi
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry

type AnovaConfigEntry = ConfigEntry[AnovaData]
@dataclass
class AnovaData:
    api_jwt: str
    coordinators: list[AnovaCoordinator]
    api: AnovaApi
