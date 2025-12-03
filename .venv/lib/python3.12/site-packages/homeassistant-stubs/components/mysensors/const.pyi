from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from typing import Final, Literal, TypedDict

ATTR_DEVICES: Final[str]
ATTR_GATEWAY_ID: Final[str]
ATTR_NODE_ID: Final[str]
CONF_BAUD_RATE: Final[str]
CONF_PERSISTENCE_FILE: Final[str]
CONF_RETAIN: Final[str]
CONF_TCP_PORT: Final[str]
CONF_TOPIC_IN_PREFIX: Final[str]
CONF_TOPIC_OUT_PREFIX: Final[str]
CONF_VERSION: Final[str]
CONF_GATEWAY_TYPE: Final[str]
type ConfGatewayType = Literal['Serial', 'TCP', 'MQTT']
CONF_GATEWAY_TYPE_SERIAL: ConfGatewayType
CONF_GATEWAY_TYPE_TCP: ConfGatewayType
CONF_GATEWAY_TYPE_MQTT: ConfGatewayType
DOMAIN: Final[str]
MYSENSORS_GATEWAY_START_TASK: str
MYSENSORS_GATEWAYS: Final[str]
MYSENSORS_DISCOVERED_NODES: Final[str]
PLATFORM: Final[str]
SCHEMA: Final[str]
CHILD_CALLBACK: str
NODE_CALLBACK: str
MYSENSORS_DISCOVERY: str
MYSENSORS_NODE_DISCOVERY: str
MYSENSORS_ON_UNLOAD: str
TYPE: Final[str]
UPDATE_DELAY: float

class DiscoveryInfo(TypedDict):
    devices: list[DevId]
    gateway_id: GatewayId

class NodeDiscoveryInfo(TypedDict):
    gateway_id: GatewayId
    node_id: int

SERVICE_SEND_IR_CODE: Final[str]
type SensorType = str
type ValueType = str
type GatewayId = str
type DevId = tuple[GatewayId, int, int, int]
BINARY_SENSOR_TYPES: dict[SensorType, set[ValueType]]
CLIMATE_TYPES: dict[SensorType, set[ValueType]]
COVER_TYPES: dict[SensorType, set[ValueType]]
DEVICE_TRACKER_TYPES: dict[SensorType, set[ValueType]]
LIGHT_TYPES: dict[SensorType, set[ValueType]]
REMOTE_TYPES: dict[SensorType, set[ValueType]]
SENSOR_TYPES: dict[SensorType, set[ValueType]]
SWITCH_TYPES: dict[SensorType, set[ValueType]]
TEXT_TYPES: dict[SensorType, set[ValueType]]
PLATFORM_TYPES: dict[Platform, dict[SensorType, set[ValueType]]]
FLAT_PLATFORM_TYPES: dict[tuple[str, SensorType], set[ValueType]]
TYPE_TO_PLATFORMS: dict[SensorType, list[Platform]]
PLATFORMS: Incomplete
