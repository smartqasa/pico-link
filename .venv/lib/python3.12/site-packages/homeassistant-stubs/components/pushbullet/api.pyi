from .const import DATA_UPDATED as DATA_UPDATED
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import dispatcher_send as dispatcher_send
from pushbullet import Listener, PushBullet as PushBullet
from typing import Any

class PushBulletNotificationProvider(Listener):
    hass: Incomplete
    pushbullet: Incomplete
    data: dict[str, Any]
    daemon: bool
    def __init__(self, hass: HomeAssistant, pushbullet: PushBullet) -> None: ...
    def update_data(self, data: dict[str, Any]) -> None: ...
