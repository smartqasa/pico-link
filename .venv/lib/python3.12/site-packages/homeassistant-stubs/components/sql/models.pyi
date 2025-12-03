from dataclasses import dataclass
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE
from sqlalchemy.orm import scoped_session as scoped_session

@dataclass(slots=True)
class SQLData:
    shutdown_event_cancel: CALLBACK_TYPE
    session_makers_by_db_url: dict[str, scoped_session]
