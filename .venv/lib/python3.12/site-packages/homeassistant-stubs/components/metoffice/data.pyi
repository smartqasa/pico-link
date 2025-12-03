from dataclasses import dataclass
from datapoint.Forecast import Forecast as Forecast
from datapoint.Site import Site as Site
from datapoint.Timestep import Timestep as Timestep

@dataclass
class MetOfficeData:
    now: Forecast
    forecast: list[Timestep]
    site: Site
