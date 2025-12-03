import asyncio
from .adapter import MatterAdapter as MatterAdapter
from .const import DOMAIN as DOMAIN, ID_TYPE_DEVICE_ID as ID_TYPE_DEVICE_ID
from dataclasses import dataclass
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import device_registry as dr
from matter_server.client.models.node import MatterEndpoint as MatterEndpoint, MatterNode as MatterNode
from matter_server.common.models import ServerInfoMessage as ServerInfoMessage

class MissingNode(HomeAssistantError): ...

@dataclass
class MatterEntryData:
    adapter: MatterAdapter
    listen_task: asyncio.Task

@callback
def get_matter(hass: HomeAssistant) -> MatterAdapter: ...
def get_operational_instance_id(server_info: ServerInfoMessage, node: MatterNode) -> str: ...
def get_device_id(server_info: ServerInfoMessage, endpoint: MatterEndpoint) -> str: ...
@callback
def node_from_ha_device_id(hass: HomeAssistant, ha_device_id: str) -> MatterNode | None: ...
@callback
def get_node_from_device_entry(hass: HomeAssistant, device: dr.DeviceEntry) -> MatterNode | None: ...
