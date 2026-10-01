"""Identity of the installation-wide, selectable light target placeholder."""

from homeassistant.const import Platform
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.discovery import async_load_platform

from .const import DOMAIN

UNIQUE_ID = "pico_link_placeholder"
NAME = "Pico Link placeholder"


def placeholder_entity_id(hass) -> str | None:
    """Look up our identity, never mistake an unrelated entity for a placeholder."""
    return er.async_get(hass).async_get_entity_id(Platform.LIGHT, DOMAIN, UNIQUE_ID)


def placeholder_info(hass) -> dict:
    entity_id = placeholder_entity_id(hass)
    entry = er.async_get(hass).async_get(entity_id) if entity_id else None
    return {"entity_id": entity_id, "name": (entry.name if entry else None) or NAME}


async def async_setup_placeholder(hass, config) -> None:
    """Load once for the installation, shared by YAML and UI controllers.

    Reserve the registry identity before parsing actions. Discovery loads the
    entity asynchronously; a collision or user rename must already resolve to
    the right ID while controllers are being prepared. UI reloads do not unload
    this shared platform, just as they do not unload the configuration panel.
    """
    er.async_get(hass).async_get_or_create(
        Platform.LIGHT,
        DOMAIN,
        UNIQUE_ID,
        suggested_object_id=UNIQUE_ID,
        original_name=NAME,
    )
    await async_load_platform(hass, Platform.LIGHT, DOMAIN, {}, config)
