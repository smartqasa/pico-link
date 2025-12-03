from .const import ATTR_MESSAGE as ATTR_MESSAGE, DOMAIN as DOMAIN, KEYRINGS_KEY_TYPE as KEYRINGS_KEY_TYPE, KEYRINGS_KEY_TYPE_ID_FINGERPRINT as KEYRINGS_KEY_TYPE_ID_FINGERPRINT, KEYRINGS_KEY_TYPE_ID_NFC as KEYRINGS_KEY_TYPE_ID_NFC, KEYRINGS_ULP_ID as KEYRINGS_ULP_ID, KEYRINGS_USER_FULL_NAME as KEYRINGS_USER_FULL_NAME, KEYRINGS_USER_STATUS as KEYRINGS_USER_STATUS
from .data import async_ufp_instance_for_config_entry_ids as async_ufp_instance_for_config_entry_ids
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID, ATTR_NAME as ATTR_NAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.service import async_extract_referenced_entity_ids as async_extract_referenced_entity_ids
from homeassistant.util.json import JsonValueType as JsonValueType
from homeassistant.util.read_only_dict import ReadOnlyDict as ReadOnlyDict
from typing import Any
from uiprotect.api import ProtectApiClient as ProtectApiClient
from uiprotect.data import Camera

SERVICE_ADD_DOORBELL_TEXT: str
SERVICE_REMOVE_DOORBELL_TEXT: str
SERVICE_SET_PRIVACY_ZONE: str
SERVICE_REMOVE_PRIVACY_ZONE: str
SERVICE_SET_CHIME_PAIRED: str
SERVICE_GET_USER_KEYRING_INFO: str
ALL_GLOBAL_SERIVCES: Incomplete
DOORBELL_TEXT_SCHEMA: Incomplete
CHIME_PAIRED_SCHEMA: Incomplete
REMOVE_PRIVACY_ZONE_SCHEMA: Incomplete
GET_USER_KEYRING_INFO_SCHEMA: Incomplete

@callback
def _async_get_ufp_instance(hass: HomeAssistant, device_id: str) -> ProtectApiClient: ...
@callback
def _async_get_ufp_camera(call: ServiceCall) -> Camera: ...
@callback
def _async_get_protect_from_call(call: ServiceCall) -> set[ProtectApiClient]: ...
async def _async_service_call_nvr(call: ServiceCall, method: str, *args: Any, **kwargs: Any) -> None: ...
async def add_doorbell_text(call: ServiceCall) -> None: ...
async def remove_doorbell_text(call: ServiceCall) -> None: ...
async def remove_privacy_zone(call: ServiceCall) -> None: ...
@callback
def _async_unique_id_to_mac(unique_id: str) -> str: ...
async def set_chime_paired_doorbells(call: ServiceCall) -> None: ...
async def get_user_keyring_info(call: ServiceCall) -> ServiceResponse: ...

SERVICES: Incomplete

def async_setup_services(hass: HomeAssistant) -> None: ...
