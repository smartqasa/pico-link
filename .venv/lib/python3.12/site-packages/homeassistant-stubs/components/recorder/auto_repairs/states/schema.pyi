from ... import Recorder as Recorder
from ...db_schema import StateAttributes as StateAttributes, States as States
from ..schema import correct_db_schema_precision as correct_db_schema_precision, correct_db_schema_utf8 as correct_db_schema_utf8, validate_db_schema_precision as validate_db_schema_precision, validate_table_schema_has_correct_collation as validate_table_schema_has_correct_collation, validate_table_schema_supports_utf8 as validate_table_schema_supports_utf8
from _typeshed import Incomplete

TABLE_UTF8_COLUMNS: Incomplete

def validate_db_schema(instance: Recorder) -> set[str]: ...
def correct_db_schema(instance: Recorder, schema_errors: set[str]) -> None: ...
