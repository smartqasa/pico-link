from .const import DOMAIN as DOMAIN
from .entity import CoordinatedTPLinkFeatureEntity as CoordinatedTPLinkFeatureEntity, TPLinkFeatureEntityDescription as TPLinkFeatureEntityDescription
from collections.abc import Sequence
from dataclasses import dataclass
from homeassistant.components.automation import automations_with_entity as automations_with_entity
from homeassistant.components.script import scripts_with_entity as scripts_with_entity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue

@dataclass(slots=True)
class DeprecatedInfo:
    platform: str
    new_platform: str
    breaks_in_ha_version: str

def async_check_create_deprecated(hass: HomeAssistant, unique_id: str, entity_description: TPLinkFeatureEntityDescription) -> bool: ...
def async_cleanup_deprecated(hass: HomeAssistant, platform: str, entry_id: str, entities: Sequence[CoordinatedTPLinkFeatureEntity]) -> None: ...
