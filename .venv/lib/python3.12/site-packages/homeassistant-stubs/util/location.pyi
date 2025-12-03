import aiohttp
from _typeshed import Incomplete
from functools import lru_cache
from typing import Any, NamedTuple

WHOAMI_URL: str
WHOAMI_URL_DEV: str
AXIS_A: int
FLATTENING: Incomplete
AXIS_B: float
MILES_PER_KILOMETER: float
MAX_ITERATIONS: int
CONVERGENCE_THRESHOLD: float

class LocationInfo(NamedTuple):
    ip: str
    country_code: str
    currency: str
    region_code: str
    region_name: str
    city: str
    zip_code: str
    time_zone: str
    latitude: float
    longitude: float
    use_metric: bool

async def async_detect_location_info(session: aiohttp.ClientSession) -> LocationInfo | None: ...
@lru_cache
def distance(lat1: float | None, lon1: float | None, lat2: float, lon2: float) -> float | None: ...
def vincenty(point1: tuple[float, float], point2: tuple[float, float], miles: bool = False) -> float | None: ...
async def _get_whoami(session: aiohttp.ClientSession) -> dict[str, Any] | None: ...
