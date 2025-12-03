from . import OnboardingData as OnboardingData, OnboardingStorage as OnboardingStorage, OnboardingStoreData as OnboardingStoreData
from .const import DEFAULT_AREAS as DEFAULT_AREAS, DOMAIN as DOMAIN, STEPS as STEPS, STEP_ANALYTICS as STEP_ANALYTICS, STEP_CORE_CONFIG as STEP_CORE_CONFIG, STEP_INTEGRATION as STEP_INTEGRATION, STEP_USER as STEP_USER
from _typeshed import Incomplete
from aiohttp import web as web
from homeassistant.auth.const import GROUP_ID_ADMIN as GROUP_ID_ADMIN
from homeassistant.auth.providers.homeassistant import HassAuthProvider as HassAuthProvider
from homeassistant.components import person as person
from homeassistant.components.auth import indieauth as indieauth
from homeassistant.components.http import KEY_HASS as KEY_HASS, KEY_HASS_REFRESH_TOKEN_ID as KEY_HASS_REFRESH_TOKEN_ID
from homeassistant.components.http.data_validator import RequestDataValidator as RequestDataValidator
from homeassistant.components.http.view import HomeAssistantView as HomeAssistantView
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.hassio import is_hassio as is_hassio
from homeassistant.helpers.system_info import async_get_system_info as async_get_system_info
from homeassistant.helpers.translation import async_get_translations as async_get_translations
from homeassistant.setup import async_setup_component as async_setup_component
from homeassistant.util.async_ import create_eager_task as create_eager_task
from typing import Any

async def async_setup(hass: HomeAssistant, data: OnboardingStoreData, store: OnboardingStorage) -> None: ...

class OnboardingView(HomeAssistantView):
    requires_auth: bool
    url: str
    name: str
    _store: Incomplete
    _data: Incomplete
    def __init__(self, data: OnboardingStoreData, store: OnboardingStorage) -> None: ...
    async def get(self, request: web.Request) -> web.Response: ...

class InstallationTypeOnboardingView(HomeAssistantView):
    requires_auth: bool
    url: str
    name: str
    _data: Incomplete
    def __init__(self, data: OnboardingStoreData) -> None: ...
    async def get(self, request: web.Request) -> web.Response: ...

class _BaseOnboardingView(HomeAssistantView):
    step: str
    _store: Incomplete
    _data: Incomplete
    _lock: Incomplete
    def __init__(self, data: OnboardingStoreData, store: OnboardingStorage) -> None: ...
    @callback
    def _async_is_done(self) -> bool: ...
    async def _async_mark_done(self, hass: HomeAssistant) -> None: ...

class UserOnboardingView(_BaseOnboardingView):
    url: str
    name: str
    requires_auth: bool
    step = STEP_USER
    async def post(self, request: web.Request, data: dict[str, str]) -> web.Response: ...

class CoreConfigOnboardingView(_BaseOnboardingView):
    url: str
    name: str
    step = STEP_CORE_CONFIG
    async def post(self, request: web.Request) -> web.Response: ...

class IntegrationOnboardingView(_BaseOnboardingView):
    url: str
    name: str
    step = STEP_INTEGRATION
    async def post(self, request: web.Request, data: dict[str, Any]) -> web.Response: ...

class AnalyticsOnboardingView(_BaseOnboardingView):
    url: str
    name: str
    step = STEP_ANALYTICS
    async def post(self, request: web.Request) -> web.Response: ...

@callback
def _async_get_hass_provider(hass: HomeAssistant) -> HassAuthProvider: ...
