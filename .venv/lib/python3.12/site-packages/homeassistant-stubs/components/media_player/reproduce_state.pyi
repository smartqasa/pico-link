from .const import ATTR_INPUT_SOURCE as ATTR_INPUT_SOURCE, ATTR_MEDIA_CONTENT_ID as ATTR_MEDIA_CONTENT_ID, ATTR_MEDIA_CONTENT_TYPE as ATTR_MEDIA_CONTENT_TYPE, ATTR_MEDIA_VOLUME_LEVEL as ATTR_MEDIA_VOLUME_LEVEL, ATTR_MEDIA_VOLUME_MUTED as ATTR_MEDIA_VOLUME_MUTED, ATTR_SOUND_MODE as ATTR_SOUND_MODE, DOMAIN as DOMAIN, MediaPlayerEntityFeature as MediaPlayerEntityFeature, SERVICE_PLAY_MEDIA as SERVICE_PLAY_MEDIA, SERVICE_SELECT_SOUND_MODE as SERVICE_SELECT_SOUND_MODE, SERVICE_SELECT_SOURCE as SERVICE_SELECT_SOURCE
from collections.abc import Iterable
from homeassistant.const import ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES, SERVICE_MEDIA_PAUSE as SERVICE_MEDIA_PAUSE, SERVICE_MEDIA_PLAY as SERVICE_MEDIA_PLAY, SERVICE_MEDIA_STOP as SERVICE_MEDIA_STOP, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, SERVICE_VOLUME_MUTE as SERVICE_VOLUME_MUTE, SERVICE_VOLUME_SET as SERVICE_VOLUME_SET, STATE_BUFFERING as STATE_BUFFERING, STATE_IDLE as STATE_IDLE, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON, STATE_PAUSED as STATE_PAUSED, STATE_PLAYING as STATE_PLAYING
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant, State as State
from typing import Any

async def _async_reproduce_states(hass: HomeAssistant, state: State, *, context: Context | None = None, reproduce_options: dict[str, Any] | None = None) -> None: ...
async def async_reproduce_states(hass: HomeAssistant, states: Iterable[State], *, context: Context | None = None, reproduce_options: dict[str, Any] | None = None) -> None: ...
