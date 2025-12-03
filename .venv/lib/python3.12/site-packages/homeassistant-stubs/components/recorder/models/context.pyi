from _typeshed import Incomplete
from homeassistant.util.ulid import bytes_to_ulid as bytes_to_ulid, bytes_to_ulid_or_none as bytes_to_ulid_or_none, ulid_to_bytes as ulid_to_bytes, ulid_to_bytes_or_none as ulid_to_bytes_or_none

_LOGGER: Incomplete

def uuid_hex_to_bytes_or_none(uuid_hex: str | None) -> bytes | None: ...
def bytes_to_uuid_hex_or_none(_bytes: bytes | None) -> str | None: ...
