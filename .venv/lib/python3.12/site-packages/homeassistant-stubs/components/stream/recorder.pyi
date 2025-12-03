from .const import RECORDER_CONTAINER_FORMAT as RECORDER_CONTAINER_FORMAT, RECORDER_PROVIDER as RECORDER_PROVIDER, SEGMENT_CONTAINER_FORMAT as SEGMENT_CONTAINER_FORMAT
from .core import IdleTimer as IdleTimer, PROVIDERS as PROVIDERS, Segment as Segment, StreamOutput as StreamOutput, StreamSettings as StreamSettings
from .fmp4utils import read_init as read_init, transform_init as transform_init
from _typeshed import Incomplete
from homeassistant.components.camera import DynamicStreamSettings as DynamicStreamSettings
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

_LOGGER: Incomplete

@callback
def async_setup_recorder(hass: HomeAssistant) -> None: ...

class RecorderOutput(StreamOutput):
    video_path: str
    def __init__(self, hass: HomeAssistant, idle_timer: IdleTimer, stream_settings: StreamSettings, dynamic_stream_settings: DynamicStreamSettings) -> None: ...
    @property
    def name(self) -> str: ...
    def prepend(self, segments: list[Segment]) -> None: ...
    def cleanup(self) -> None: ...
    async def async_record(self) -> None: ...
