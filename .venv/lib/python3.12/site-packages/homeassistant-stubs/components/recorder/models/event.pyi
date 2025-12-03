from homeassistant.util.event_type import EventType as EventType
from typing import Any

def extract_event_type_ids(event_type_to_event_type_id: dict[EventType[Any] | str, int | None]) -> list[int]: ...
