from . import views as views
from .const import DOMAIN as DOMAIN, STEPS as STEPS, STEP_ANALYTICS as STEP_ANALYTICS, STEP_CORE_CONFIG as STEP_CORE_CONFIG, STEP_INTEGRATION as STEP_INTEGRATION, STEP_USER as STEP_USER
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.storage import Store as Store
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass
from typing import TypedDict

STORAGE_KEY = DOMAIN
STORAGE_VERSION: int
CONFIG_SCHEMA: Incomplete

@dataclass
class OnboardingData:
    listeners: list[Callable[[], None]]
    onboarded: bool
    steps: OnboardingStoreData

class OnboardingStoreData(TypedDict):
    done: list[str]

class OnboardingStorage(Store[OnboardingStoreData]):
    async def _async_migrate_func(self, old_major_version: int, old_minor_version: int, old_data: OnboardingStoreData) -> OnboardingStoreData: ...

@bind_hass
@callback
def async_is_onboarded(hass: HomeAssistant) -> bool: ...
@bind_hass
@callback
def async_is_user_onboarded(hass: HomeAssistant) -> bool: ...
@callback
def async_add_listener(hass: HomeAssistant, listener: Callable[[], None]) -> None: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
