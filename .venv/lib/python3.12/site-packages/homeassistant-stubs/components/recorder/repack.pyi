from . import Recorder as Recorder
from .const import SupportedDialect as SupportedDialect
from .db_schema import ALL_TABLES as ALL_TABLES
from _typeshed import Incomplete

_LOGGER: Incomplete

def repack_database(instance: Recorder) -> None: ...
