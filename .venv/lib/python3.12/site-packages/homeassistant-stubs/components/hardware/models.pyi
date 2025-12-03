from dataclasses import dataclass
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Protocol

@dataclass(slots=True)
class BoardInfo:
    hassio_board_id: str | None
    manufacturer: str
    model: str | None
    revision: str | None

@dataclass(slots=True, frozen=True)
class USBInfo:
    vid: str
    pid: str
    serial_number: str | None
    manufacturer: str | None
    description: str | None

@dataclass(slots=True, frozen=True)
class HardwareInfo:
    name: str | None
    board: BoardInfo | None
    config_entries: list[str] | None
    dongle: USBInfo | None
    url: str | None

class HardwareProtocol(Protocol):
    @callback
    def async_info(self, hass: HomeAssistant) -> list[HardwareInfo]: ...
