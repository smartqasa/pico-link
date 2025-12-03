from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.file_upload import process_uploaded_file as process_uploaded_file
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.storage import Store as Store
from typing import Final
from xknx import XKNX as XKNX
from xknx.dpt import DPTBase
from xknx.telegram.address import DeviceAddressableType as DeviceAddressableType, GroupAddressType
from xknxproject.models import DPTType as DPTType, Device as Device, GroupAddress as GroupAddressModel, KNXProject as KNXProjectModel, ProjectInfo as ProjectInfo

_LOGGER: Incomplete
STORAGE_VERSION: Final[int]
STORAGE_KEY: Final[Incomplete]

@dataclass
class GroupAddressInfo:
    address: str
    name: str
    description: str
    dpt_main: int | None
    dpt_sub: int | None
    transcoder: type[DPTBase] | None

def _create_group_address_info(ga_model: GroupAddressModel) -> GroupAddressInfo: ...

class KNXProject:
    loaded: bool
    devices: dict[str, Device]
    group_addresses: dict[str, GroupAddressInfo]
    info: ProjectInfo | None
    hass: Incomplete
    _store: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None: ...
    def initial_state(self) -> None: ...
    async def load_project(self, xknx: XKNX, data: KNXProjectModel | None = None) -> None: ...
    async def process_project_file(self, xknx: XKNX, file_id: str, password: str) -> None: ...
    async def remove_project_file(self) -> None: ...
    async def get_knxproject(self) -> KNXProjectModel | None: ...
    def get_address_format(self) -> GroupAddressType: ...
