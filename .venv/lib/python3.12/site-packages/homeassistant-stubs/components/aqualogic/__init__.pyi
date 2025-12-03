import threading
from _typeshed import Incomplete
from aqualogic.core import AquaLogic
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, EVENT_HOMEASSISTANT_START as EVENT_HOMEASSISTANT_START, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import dispatcher_send as dispatcher_send
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete
DOMAIN: str
UPDATE_TOPIC: Incomplete
CONF_UNIT: str
RECONNECT_INTERVAL: Incomplete
CONFIG_SCHEMA: Incomplete

def setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class AquaLogicProcessor(threading.Thread):
    _hass: Incomplete
    _host: Incomplete
    _port: Incomplete
    _shutdown: bool
    _panel: Incomplete
    def __init__(self, hass: HomeAssistant, host: str, port: int) -> None: ...
    def start_listen(self, event: Event) -> None: ...
    def shutdown(self, event: Event) -> None: ...
    def data_changed(self, panel: AquaLogic) -> None: ...
    def run(self) -> None: ...
    @property
    def panel(self) -> AquaLogic | None: ...
