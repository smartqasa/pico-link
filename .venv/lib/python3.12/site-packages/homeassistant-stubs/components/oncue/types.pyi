from aiooncue import OncueDevice
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

type OncueConfigEntry = ConfigEntry[DataUpdateCoordinator[dict[str, OncueDevice]]]
