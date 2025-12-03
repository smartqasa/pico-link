from .core import Orientation as Orientation
from _typeshed import Incomplete
from collections.abc import Generator
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from io import BufferedIOBase

def find_box(mp4_bytes: bytes, target_type: bytes, box_start: int = 0) -> Generator[int]: ...
def get_codec_string(mp4_bytes: bytes) -> str: ...
def find_moov(mp4_io: BufferedIOBase) -> int: ...
def read_init(bytes_io: BufferedIOBase) -> bytes: ...

ZERO32: bytes
ONE32: bytes
NEGONE32: bytes
XYW_ROW: Incomplete
ROTATE_RIGHT: Incomplete
ROTATE_LEFT: Incomplete
ROTATE_180: Incomplete
MIRROR: Incomplete
FLIP: Incomplete
ROTATE_LEFT_FLIP: Incomplete
ROTATE_RIGHT_FLIP: Incomplete
TRANSFORM_MATRIX_TOP: Incomplete

def transform_init(init: bytes, orientation: Orientation) -> bytes: ...
