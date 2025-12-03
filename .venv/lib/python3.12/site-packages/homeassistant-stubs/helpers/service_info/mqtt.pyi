from dataclasses import dataclass
from homeassistant.data_entry_flow import BaseServiceInfo as BaseServiceInfo

type ReceivePayloadType = str | bytes | bytearray
@dataclass(slots=True)
class MqttServiceInfo(BaseServiceInfo):
    topic: str
    payload: ReceivePayloadType
    qos: int
    retain: bool
    subscribed_topic: str
    timestamp: float
