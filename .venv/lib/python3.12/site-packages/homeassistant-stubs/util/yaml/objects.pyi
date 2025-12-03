import voluptuous as vol
import yaml
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Any

class NodeListClass(list):
    __slots__: Incomplete
    __config_file__: str
    __line__: int | str

class NodeStrClass(str):
    __slots__: Incomplete
    __config_file__: str
    __line__: int | str
    def __voluptuous_compile__(self, schema: vol.Schema) -> Any: ...

class NodeDictClass(dict):
    __slots__: Incomplete
    __config_file__: str
    __line__: int | str

@dataclass(slots=True, frozen=True)
class Input:
    name: str
    @classmethod
    def from_node(cls, loader: yaml.Loader, node: yaml.nodes.Node) -> Input: ...
