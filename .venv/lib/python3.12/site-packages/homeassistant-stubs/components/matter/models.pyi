from chip.clusters import Objects as clusters
from chip.clusters.Objects import Cluster as Cluster, ClusterAttributeDescriptor as ClusterAttributeDescriptor
from dataclasses import dataclass
from homeassistant.const import Platform as Platform
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from matter_server.client.models.device_types import DeviceType as DeviceType
from matter_server.client.models.node import MatterEndpoint as MatterEndpoint
from typing import Any, TypedDict

type SensorValueTypes = type[clusters.uint | int | clusters.Nullable | clusters.float32 | float]
class MatterDeviceInfo(TypedDict):
    unique_id: str
    vendor_id: str
    product_id: str

@dataclass
class MatterEntityInfo:
    endpoint: MatterEndpoint
    platform: Platform
    attributes_to_watch: list[type[ClusterAttributeDescriptor]]
    entity_description: EntityDescription
    entity_class: type
    discovery_schema: MatterDiscoverySchema
    @property
    def primary_attribute(self) -> type[ClusterAttributeDescriptor]: ...

@dataclass
class MatterDiscoverySchema:
    platform: Platform
    entity_description: EntityDescription
    entity_class: type
    required_attributes: tuple[type[ClusterAttributeDescriptor], ...]
    device_type: tuple[type[DeviceType] | DeviceType, ...] | None = ...
    not_device_type: tuple[type[DeviceType] | DeviceType, ...] | None = ...
    vendor_id: tuple[int, ...] | None = ...
    product_name: tuple[str, ...] | None = ...
    endpoint_id: tuple[int, ...] | None = ...
    absent_attributes: tuple[type[ClusterAttributeDescriptor], ...] | None = ...
    absent_clusters: tuple[type[Cluster], ...] | None = ...
    optional_attributes: tuple[type[ClusterAttributeDescriptor], ...] | None = ...
    value_contains: Any | None = ...
    featuremap_contains: int | None = ...
    allow_multi: bool = ...
