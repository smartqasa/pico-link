from .coordinator import SpotifyCoordinator as SpotifyCoordinator
from dataclasses import dataclass
from homeassistant.helpers.config_entry_oauth2_flow import OAuth2Session as OAuth2Session
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from spotifyaio import Device as Device

@dataclass
class SpotifyData:
    coordinator: SpotifyCoordinator
    session: OAuth2Session
    devices: DataUpdateCoordinator[list[Device]]
