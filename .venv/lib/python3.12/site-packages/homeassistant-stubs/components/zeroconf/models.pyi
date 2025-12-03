from _typeshed import Incomplete
from zeroconf import Zeroconf
from zeroconf.asyncio import AsyncZeroconf

class HaZeroconf(Zeroconf):
    def close(self) -> None: ...
    ha_close: Incomplete

class HaAsyncZeroconf(AsyncZeroconf):
    async def async_close(self) -> None: ...
    ha_async_close: Incomplete
