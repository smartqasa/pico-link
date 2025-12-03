from canary.model import Location as Location, Reading as Reading
from collections.abc import ValuesView
from typing import TypedDict

class CanaryData(TypedDict):
    locations: dict[str, Location]
    readings: dict[str, ValuesView[Reading]]
