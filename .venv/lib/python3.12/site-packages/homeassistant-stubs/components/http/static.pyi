from _typeshed import Incomplete
from aiohttp.web import Request as Request, StreamResponse as StreamResponse
from aiohttp.web_urldispatcher import StaticResource
from collections.abc import Mapping
from lru import LRU
from pathlib import Path
from typing import Final

CACHE_TIME: Final[Incomplete]
CACHE_HEADER: Incomplete
CACHE_HEADERS: Mapping[str, str]
RESPONSE_CACHE: LRU[tuple[str, Path], tuple[Path, str]]
_GUESSER: Incomplete

class CachingStaticResource(StaticResource):
    async def _handle(self, request: Request) -> StreamResponse: ...
