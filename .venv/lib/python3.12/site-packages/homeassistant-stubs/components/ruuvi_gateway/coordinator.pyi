import logging
from _typeshed import Incomplete
from aioruuvigateway.models import TagData
from datetime import timedelta
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

class RuuviGatewayUpdateCoordinator(DataUpdateCoordinator[list[TagData]]):
    host: Incomplete
    token: Incomplete
    last_tag_datas: dict[str, TagData]
    def __init__(self, hass: HomeAssistant, logger: logging.Logger, *, name: str, update_interval: timedelta | None = None, host: str, token: str) -> None: ...
    async def _async_update_data(self) -> list[TagData]: ...
