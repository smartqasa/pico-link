import json
import orjson
from .deprecation import DeprecatedConstant as DeprecatedConstant, all_with_deprecated_constants as all_with_deprecated_constants, check_if_deprecated_constant as check_if_deprecated_constant, deprecated_function as deprecated_function, dir_with_deprecated_constants as dir_with_deprecated_constants
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.util.file import write_utf8_file as write_utf8_file, write_utf8_file_atomic as write_utf8_file_atomic
from homeassistant.util.json import SerializationError as SerializationError, format_unserializable_data as format_unserializable_data
from typing import Any, Final

_DEPRECATED_JSON_DECODE_EXCEPTIONS: Incomplete
_DEPRECATED_JSON_ENCODE_EXCEPTIONS: Incomplete
json_loads: Incomplete
__getattr__: Incomplete
__dir__: Incomplete
__all__: Incomplete
_LOGGER: Incomplete

class JSONEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any: ...

def json_encoder_default(obj: Any) -> Any: ...
def json_bytes(obj: Any) -> bytes: ...

class ExtendedJSONEncoder(JSONEncoder):
    def default(self, o: Any) -> Any: ...

def _strip_null(obj: Any) -> Any: ...
def json_bytes_strip_null(data: Any) -> bytes: ...
json_fragment = orjson.Fragment

def json_dumps(data: Any) -> str: ...

json_bytes_sorted: Incomplete

def json_dumps_sorted(data: Any) -> str: ...

JSON_DUMP: Final[Incomplete]

def _orjson_default_encoder(data: Any) -> str: ...
def _orjson_bytes_default_encoder(data: Any) -> bytes: ...
def save_json(filename: str, data: list | dict, private: bool = False, *, encoder: type[json.JSONEncoder] | None = None, atomic_writes: bool = False) -> None: ...
def find_paths_unserializable_data(bad_data: Any, *, dump: Callable[[Any], str] = ...) -> dict[str, Any]: ...
