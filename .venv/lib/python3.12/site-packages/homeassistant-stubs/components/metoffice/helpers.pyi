import datapoint
from .const import MODE_3HOURLY as MODE_3HOURLY
from .data import MetOfficeData as MetOfficeData
from _typeshed import Incomplete
from datapoint.Site import Site as Site
from homeassistant.helpers.update_coordinator import UpdateFailed as UpdateFailed
from homeassistant.util.dt import utcnow as utcnow

_LOGGER: Incomplete

def fetch_site(connection: datapoint.Manager, latitude: float, longitude: float) -> Site | None: ...
def fetch_data(connection: datapoint.Manager, site: Site, mode: str) -> MetOfficeData: ...
