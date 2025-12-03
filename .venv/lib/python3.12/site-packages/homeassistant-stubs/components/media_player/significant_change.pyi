from . import ATTR_ENTITY_PICTURE_LOCAL as ATTR_ENTITY_PICTURE_LOCAL, ATTR_MEDIA_POSITION as ATTR_MEDIA_POSITION, ATTR_MEDIA_POSITION_UPDATED_AT as ATTR_MEDIA_POSITION_UPDATED_AT, ATTR_MEDIA_VOLUME_LEVEL as ATTR_MEDIA_VOLUME_LEVEL, ATTR_TO_PROPERTY as ATTR_TO_PROPERTY
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.significant_change import check_absolute_change as check_absolute_change, check_valid_float as check_valid_float
from typing import Any

INSIGNIFICANT_ATTRIBUTES: set[str]
SIGNIFICANT_ATTRIBUTES: set[str]

@callback
def async_check_significant_change(hass: HomeAssistant, old_state: str, old_attrs: dict, new_state: str, new_attrs: dict, **kwargs: Any) -> bool | None: ...
