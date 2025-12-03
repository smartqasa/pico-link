from _typeshed import Incomplete
from homeassistant.components.script import CONF_MODE as CONF_MODE
from homeassistant.const import CONF_DESCRIPTION as CONF_DESCRIPTION, CONF_TYPE as CONF_TYPE, SERVICE_RELOAD as SERVICE_RELOAD
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.helpers import intent as intent, script as script, service as service, template as template
from homeassistant.helpers.reload import async_integration_yaml_config as async_integration_yaml_config
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import TypedDict

_LOGGER: Incomplete
DOMAIN: str
CONF_PLATFORMS: str
CONF_INTENTS: str
CONF_SPEECH: str
CONF_REPROMPT: str
CONF_ACTION: str
CONF_CARD: str
CONF_TITLE: str
CONF_CONTENT: str
CONF_TEXT: str
CONF_ASYNC_ACTION: str
DEFAULT_CONF_ASYNC_ACTION: bool
CONFIG_SCHEMA: Incomplete

async def async_reload(hass: HomeAssistant, service_call: ServiceCall) -> None: ...
def async_load_intents(hass: HomeAssistant, intents: dict[str, ConfigType]) -> None: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class _IntentSpeechRepromptData(TypedDict):
    content: template.Template
    title: template.Template
    text: template.Template
    type: str

class _IntentCardData(TypedDict):
    type: str
    title: template.Template
    content: template.Template

class ScriptIntentHandler(intent.IntentHandler):
    slot_schema: Incomplete
    intent_type: Incomplete
    config: Incomplete
    description: Incomplete
    platforms: Incomplete
    def __init__(self, intent_type: str, config: ConfigType) -> None: ...
    async def async_handle(self, intent_obj: intent.Intent) -> intent.IntentResponse: ...
