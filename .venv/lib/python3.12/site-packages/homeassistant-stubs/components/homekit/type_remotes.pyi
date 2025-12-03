import abc
from .accessories import HomeAccessory as HomeAccessory, TYPES as TYPES
from .const import ATTR_KEY_NAME as ATTR_KEY_NAME, CHAR_ACTIVE as CHAR_ACTIVE, CHAR_ACTIVE_IDENTIFIER as CHAR_ACTIVE_IDENTIFIER, CHAR_CONFIGURED_NAME as CHAR_CONFIGURED_NAME, CHAR_CURRENT_VISIBILITY_STATE as CHAR_CURRENT_VISIBILITY_STATE, CHAR_IDENTIFIER as CHAR_IDENTIFIER, CHAR_INPUT_SOURCE_TYPE as CHAR_INPUT_SOURCE_TYPE, CHAR_IS_CONFIGURED as CHAR_IS_CONFIGURED, CHAR_NAME as CHAR_NAME, CHAR_REMOTE_KEY as CHAR_REMOTE_KEY, CHAR_SLEEP_DISCOVER_MODE as CHAR_SLEEP_DISCOVER_MODE, EVENT_HOMEKIT_TV_REMOTE_KEY_PRESSED as EVENT_HOMEKIT_TV_REMOTE_KEY_PRESSED, KEY_ARROW_DOWN as KEY_ARROW_DOWN, KEY_ARROW_LEFT as KEY_ARROW_LEFT, KEY_ARROW_RIGHT as KEY_ARROW_RIGHT, KEY_ARROW_UP as KEY_ARROW_UP, KEY_BACK as KEY_BACK, KEY_EXIT as KEY_EXIT, KEY_FAST_FORWARD as KEY_FAST_FORWARD, KEY_INFORMATION as KEY_INFORMATION, KEY_NEXT_TRACK as KEY_NEXT_TRACK, KEY_PLAY_PAUSE as KEY_PLAY_PAUSE, KEY_PREVIOUS_TRACK as KEY_PREVIOUS_TRACK, KEY_REWIND as KEY_REWIND, KEY_SELECT as KEY_SELECT, SERV_INPUT_SOURCE as SERV_INPUT_SOURCE, SERV_TELEVISION as SERV_TELEVISION
from .util import cleanup_name_for_homekit as cleanup_name_for_homekit
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from homeassistant.components.remote import ATTR_ACTIVITY as ATTR_ACTIVITY, ATTR_ACTIVITY_LIST as ATTR_ACTIVITY_LIST, ATTR_CURRENT_ACTIVITY as ATTR_CURRENT_ACTIVITY, RemoteEntityFeature as RemoteEntityFeature
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_ON as STATE_ON
from homeassistant.core import State as State, callback as callback
from typing import Any

MAXIMUM_SOURCES: int
_LOGGER: Incomplete
REMOTE_KEYS: Incomplete

class RemoteInputSelectAccessory(HomeAccessory, ABC, metaclass=abc.ABCMeta):
    _mapped_sources_list: list[str]
    _mapped_sources: dict[str, str]
    source_key: Incomplete
    source_list_key: Incomplete
    sources: Incomplete
    support_select_source: bool
    chars_tv: Incomplete
    char_remote_key: Incomplete
    char_active: Incomplete
    char_input_source: Incomplete
    def __init__(self, required_feature: int, source_key: str, source_list_key: str, *args: Any, category: int = ..., **kwargs: Any) -> None: ...
    def _get_mapped_sources(self, state: State) -> dict[str, str]: ...
    def _get_ordered_source_list_from_state(self, state: State) -> list[str]: ...
    @abstractmethod
    def set_on_off(self, value: bool) -> None: ...
    @abstractmethod
    def set_input_source(self, value: int) -> None: ...
    @abstractmethod
    def set_remote_key(self, value: int) -> None: ...
    @callback
    def _async_update_input_state(self, hk_state: int, new_state: State) -> None: ...

class ActivityRemote(RemoteInputSelectAccessory):
    def __init__(self, *args: Any) -> None: ...
    def set_on_off(self, value: bool) -> None: ...
    def set_input_source(self, value: int) -> None: ...
    def set_remote_key(self, value: int) -> None: ...
    @callback
    def async_update_state(self, new_state: State) -> None: ...
