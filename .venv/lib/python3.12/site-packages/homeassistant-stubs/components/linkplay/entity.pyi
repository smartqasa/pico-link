from . import DOMAIN as DOMAIN, LinkPlayRequestException as LinkPlayRequestException
from .utils import MANUFACTURER_GENERIC as MANUFACTURER_GENERIC, get_info_from_project as get_info_from_project
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity import Entity as Entity
from linkplay.bridge import LinkPlayBridge as LinkPlayBridge
from typing import Any, Concatenate

def exception_wrap[_LinkPlayEntityT: LinkPlayBaseEntity, **_P, _R](func: Callable[Concatenate[_LinkPlayEntityT, _P], Coroutine[Any, Any, _R]]) -> Callable[Concatenate[_LinkPlayEntityT, _P], Coroutine[Any, Any, _R]]: ...

class LinkPlayBaseEntity(Entity):
    _attr_has_entity_name: bool
    _bridge: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, bridge: LinkPlayBridge) -> None: ...
