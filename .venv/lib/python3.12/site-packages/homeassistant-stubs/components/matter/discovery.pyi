from .const import FEATUREMAP_ATTRIBUTE_ID as FEATUREMAP_ATTRIBUTE_ID
from .models import MatterDiscoverySchema as MatterDiscoverySchema, MatterEntityInfo as MatterEntityInfo
from _typeshed import Incomplete
from chip.clusters.Objects import ClusterAttributeDescriptor as ClusterAttributeDescriptor
from collections.abc import Generator
from homeassistant.const import Platform as Platform
from homeassistant.core import callback as callback
from matter_server.client.models.node import MatterEndpoint as MatterEndpoint

DISCOVERY_SCHEMAS: dict[Platform, list[MatterDiscoverySchema]]
SUPPORTED_PLATFORMS: Incomplete

@callback
def iter_schemas() -> Generator[MatterDiscoverySchema]: ...
@callback
def async_discover_entities(endpoint: MatterEndpoint) -> Generator[MatterEntityInfo]: ...
