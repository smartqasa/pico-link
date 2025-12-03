from .const import ATTR_CONFIG_ENTRY_ID as ATTR_CONFIG_ENTRY_ID, ATTR_END_DATE as ATTR_END_DATE, ATTR_ENTRY_TYPE as ATTR_ENTRY_TYPE, ATTR_INCLUDE_TAGS as ATTR_INCLUDE_TAGS, ATTR_NOTE_TEXT as ATTR_NOTE_TEXT, ATTR_NOTE_TITLE as ATTR_NOTE_TITLE, ATTR_RECIPE_ID as ATTR_RECIPE_ID, ATTR_START_DATE as ATTR_START_DATE, ATTR_URL as ATTR_URL, DOMAIN as DOMAIN
from .coordinator import MealieConfigEntry as MealieConfigEntry
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.const import ATTR_DATE as ATTR_DATE
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError

SERVICE_GET_MEALPLAN: str
SERVICE_GET_MEALPLAN_SCHEMA: Incomplete
SERVICE_GET_RECIPE: str
SERVICE_GET_RECIPE_SCHEMA: Incomplete
SERVICE_IMPORT_RECIPE: str
SERVICE_IMPORT_RECIPE_SCHEMA: Incomplete
SERVICE_SET_RANDOM_MEALPLAN: str
SERVICE_SET_RANDOM_MEALPLAN_SCHEMA: Incomplete
SERVICE_SET_MEALPLAN: str
SERVICE_SET_MEALPLAN_SCHEMA: Incomplete

def async_get_entry(hass: HomeAssistant, config_entry_id: str) -> MealieConfigEntry: ...
def setup_services(hass: HomeAssistant) -> None: ...
