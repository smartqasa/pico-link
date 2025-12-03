from homeassistant.helpers.template import Template as Template
from typing import TypedDict

class TcpSensorConfig(TypedDict):
    name: str
    host: str
    port: str
    timeout: int
    payload: str
    unit_of_measurement: str | None
    value_template: Template | None
    value_on: str | None
    buffer_size: int
    ssl: bool
    verify_ssl: bool
