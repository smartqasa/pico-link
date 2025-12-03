from _typeshed import Incomplete
from airtouch5py.airtouch5_client import Airtouch5ConnectionStateChange
from airtouch5py.airtouch5_simple_client import Airtouch5SimpleClient as Airtouch5SimpleClient
from homeassistant.core import callback as callback
from homeassistant.helpers.entity import Entity as Entity

class Airtouch5Entity(Entity):
    _attr_should_poll: bool
    _attr_has_entity_name: bool
    _client: Incomplete
    _attr_available: bool
    def __init__(self, client: Airtouch5SimpleClient) -> None: ...
    @callback
    def _receive_connection_callback(self, state: Airtouch5ConnectionStateChange) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
