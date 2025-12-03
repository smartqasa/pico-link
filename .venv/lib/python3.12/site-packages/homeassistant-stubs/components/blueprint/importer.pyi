from .models import Blueprint as Blueprint
from .schemas import BLUEPRINT_SCHEMA as BLUEPRINT_SCHEMA, is_blueprint_config as is_blueprint_config
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.util import yaml as yaml

COMMUNITY_TOPIC_PATTERN: Incomplete
COMMUNITY_CODE_BLOCK: Incomplete
GITHUB_FILE_PATTERN: Incomplete
WEBSITE_PATTERN: Incomplete
COMMUNITY_TOPIC_SCHEMA: Incomplete

class UnsupportedUrl(HomeAssistantError): ...

@dataclass(frozen=True)
class ImportedBlueprint:
    suggested_filename: str
    raw_data: str
    blueprint: Blueprint

def _get_github_import_url(url: str) -> str: ...
def _get_community_post_import_url(url: str) -> str: ...
def _extract_blueprint_from_community_topic(url: str, topic: dict) -> ImportedBlueprint: ...
async def fetch_blueprint_from_community_post(hass: HomeAssistant, url: str) -> ImportedBlueprint: ...
async def fetch_blueprint_from_github_url(hass: HomeAssistant, url: str) -> ImportedBlueprint: ...
async def fetch_blueprint_from_github_gist_url(hass: HomeAssistant, url: str) -> ImportedBlueprint: ...
async def fetch_blueprint_from_website_url(hass: HomeAssistant, url: str) -> ImportedBlueprint: ...
async def fetch_blueprint_from_generic_url(hass: HomeAssistant, url: str) -> ImportedBlueprint: ...

FETCH_FUNCTIONS: Incomplete

async def fetch_blueprint_from_url(hass: HomeAssistant, url: str) -> ImportedBlueprint: ...
