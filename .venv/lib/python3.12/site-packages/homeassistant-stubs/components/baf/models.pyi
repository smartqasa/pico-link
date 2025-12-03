from dataclasses import dataclass

@dataclass
class BAFDiscovery:
    ip_address: str
    name: str
    uuid: str
    model: str
