from .client import CloudClient as CloudClient
from .const import REQUEST_TIMEOUT as REQUEST_TIMEOUT
from _typeshed import Incomplete
from hass_nabucasa import Cloud as Cloud
from typing import Any

_LOGGER: Incomplete

async def async_subscription_info(cloud: Cloud[CloudClient]) -> dict[str, Any] | None: ...
async def async_migrate_paypal_agreement(cloud: Cloud[CloudClient]) -> dict[str, Any] | None: ...
