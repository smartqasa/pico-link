from .client import async_subscribe_internal as async_subscribe_internal
from .const import CONF_ENCODING as CONF_ENCODING, CONF_QOS as CONF_QOS, CONF_TOPIC as CONF_TOPIC, DEFAULT_ENCODING as DEFAULT_ENCODING, DEFAULT_QOS as DEFAULT_QOS, DOMAIN as DOMAIN
from .models import MqttCommandTemplate as MqttCommandTemplate, MqttValueTemplate as MqttValueTemplate, PayloadSentinel as PayloadSentinel, PublishPayloadType as PublishPayloadType, ReceiveMessage as ReceiveMessage
from .util import valid_subscribe_topic as valid_subscribe_topic, valid_subscribe_topic_template as valid_subscribe_topic_template
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.const import CONF_PAYLOAD as CONF_PAYLOAD, CONF_PLATFORM as CONF_PLATFORM, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HassJob as HassJob, HassJobType as HassJobType, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.service_info.mqtt import ReceivePayloadType as ReceivePayloadType
from homeassistant.helpers.template import Template as Template
from homeassistant.helpers.trigger import TriggerActionType as TriggerActionType, TriggerData as TriggerData, TriggerInfo as TriggerInfo
from homeassistant.helpers.typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType
from homeassistant.util.json import json_loads as json_loads

TRIGGER_SCHEMA: Incomplete
_LOGGER: Incomplete

async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: TriggerActionType, trigger_info: TriggerInfo) -> CALLBACK_TYPE: ...
