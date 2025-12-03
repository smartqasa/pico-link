from .const import DOMAIN as DOMAIN
from .entity import HomeWizardEntity as HomeWizardEntity
from collections.abc import Callable as Callable, Coroutine
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any, Concatenate

def homewizard_exception_handler[_HomeWizardEntityT: HomeWizardEntity, **_P](func: Callable[Concatenate[_HomeWizardEntityT, _P], Coroutine[Any, Any, Any]]) -> Callable[Concatenate[_HomeWizardEntityT, _P], Coroutine[Any, Any, None]]: ...
