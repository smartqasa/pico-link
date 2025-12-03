from .const import CONF_NETWORK as CONF_NETWORK, NODE_AUX_PROP_PLATFORMS as NODE_AUX_PROP_PLATFORMS, NODE_PLATFORMS as NODE_PLATFORMS, PROGRAM_PLATFORMS as PROGRAM_PLATFORMS, ROOT_NODE_PLATFORMS as ROOT_NODE_PLATFORMS, VARIABLE_PLATFORMS as VARIABLE_PLATFORMS
from dataclasses import dataclass
from homeassistant.const import Platform as Platform
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from pyisy import ISY as ISY
from pyisy.networking import NetworkCommand
from pyisy.nodes import Group as Group, Node as Node
from pyisy.programs import Program as Program
from pyisy.variables import Variable as Variable

@dataclass
class IsyData:
    root: ISY
    nodes: dict[Platform, list[Node | Group]]
    root_nodes: dict[Platform, list[Node]]
    variables: dict[Platform, list[Variable]]
    programs: dict[Platform, list[tuple[str, Program, Program]]]
    net_resources: list[NetworkCommand]
    devices: dict[str, DeviceInfo]
    aux_properties: dict[Platform, list[tuple[Node, str]]]
    def __init__(self) -> None: ...
    @property
    def uuid(self) -> str: ...
    def uid_base(self, node: Node | Group | Variable | Program | NetworkCommand) -> str: ...
    @property
    def unique_ids(self) -> set[tuple[Platform, str]]: ...
