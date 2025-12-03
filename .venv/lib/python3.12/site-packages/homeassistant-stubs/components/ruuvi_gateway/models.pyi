import dataclasses
from .bluetooth import RuuviGatewayScanner as RuuviGatewayScanner
from .coordinator import RuuviGatewayUpdateCoordinator as RuuviGatewayUpdateCoordinator

@dataclasses.dataclass(frozen=True)
class RuuviGatewayRuntimeData:
    update_coordinator: RuuviGatewayUpdateCoordinator
    scanner: RuuviGatewayScanner
