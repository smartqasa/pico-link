from enum import IntFlag
from typing import Final

DOMAIN: Final[str]

class UpdateEntityFeature(IntFlag):
    INSTALL = 1
    SPECIFIC_VERSION = 2
    PROGRESS = 4
    BACKUP = 8
    RELEASE_NOTES = 16

SERVICE_INSTALL: Final[str]
SERVICE_SKIP: Final[str]
ATTR_AUTO_UPDATE: Final[str]
ATTR_BACKUP: Final[str]
ATTR_DISPLAY_PRECISION: Final[str]
ATTR_INSTALLED_VERSION: Final[str]
ATTR_IN_PROGRESS: Final[str]
ATTR_LATEST_VERSION: Final[str]
ATTR_RELEASE_SUMMARY: Final[str]
ATTR_RELEASE_URL: Final[str]
ATTR_SKIPPED_VERSION: Final[str]
ATTR_TITLE: Final[str]
ATTR_UPDATE_PERCENTAGE: Final[str]
ATTR_VERSION: Final[str]
