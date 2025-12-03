import abc
from . import WithingsConfigEntry as WithingsConfigEntry
from .const import LOGGER as LOGGER
from _typeshed import Incomplete
from abc import abstractmethod
from aiowithings import Activity, Device, Goals, MeasurementPosition, MeasurementType, NotificationCategory, SleepSummary, WithingsClient as WithingsClient, Workout
from datetime import datetime, timedelta
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

UPDATE_INTERVAL: Incomplete

class WithingsDataUpdateCoordinator[_DataT](DataUpdateCoordinator[_DataT], metaclass=abc.ABCMeta):
    config_entry: WithingsConfigEntry
    _default_update_interval: timedelta | None
    _last_valid_update: datetime | None
    webhooks_connected: bool
    coordinator_name: str
    name: Incomplete
    _client: Incomplete
    notification_categories: set[NotificationCategory]
    def __init__(self, hass: HomeAssistant, client: WithingsClient) -> None: ...
    update_interval: Incomplete
    def webhook_subscription_listener(self, connected: bool) -> None: ...
    async def async_webhook_data_updated(self, notification_category: NotificationCategory) -> None: ...
    async def _async_update_data(self) -> _DataT: ...
    @abstractmethod
    async def _internal_update_data(self) -> _DataT: ...

class WithingsMeasurementDataUpdateCoordinator(WithingsDataUpdateCoordinator[dict[tuple[MeasurementType, MeasurementPosition | None], float]]):
    coordinator_name: str
    notification_categories: Incomplete
    _previous_data: dict[tuple[MeasurementType, MeasurementPosition | None], float]
    def __init__(self, hass: HomeAssistant, client: WithingsClient) -> None: ...
    _last_valid_update: Incomplete
    async def _internal_update_data(self) -> dict[tuple[MeasurementType, MeasurementPosition | None], float]: ...

class WithingsSleepDataUpdateCoordinator(WithingsDataUpdateCoordinator[SleepSummary | None]):
    coordinator_name: str
    notification_categories: Incomplete
    def __init__(self, hass: HomeAssistant, client: WithingsClient) -> None: ...
    async def _internal_update_data(self) -> SleepSummary | None: ...

class WithingsBedPresenceDataUpdateCoordinator(WithingsDataUpdateCoordinator[None]):
    coordinator_name: str
    in_bed: bool | None
    _default_update_interval: Incomplete
    notification_categories: Incomplete
    def __init__(self, hass: HomeAssistant, client: WithingsClient) -> None: ...
    async def async_webhook_data_updated(self, notification_category: NotificationCategory) -> None: ...
    async def _internal_update_data(self) -> None: ...

class WithingsGoalsDataUpdateCoordinator(WithingsDataUpdateCoordinator[Goals]):
    coordinator_name: str
    _default_update_interval: Incomplete
    def webhook_subscription_listener(self, connected: bool) -> None: ...
    async def _internal_update_data(self) -> Goals: ...

class WithingsActivityDataUpdateCoordinator(WithingsDataUpdateCoordinator[Activity | None]):
    coordinator_name: str
    _previous_data: Activity | None
    notification_categories: Incomplete
    def __init__(self, hass: HomeAssistant, client: WithingsClient) -> None: ...
    _last_valid_update: Incomplete
    async def _internal_update_data(self) -> Activity | None: ...

class WithingsWorkoutDataUpdateCoordinator(WithingsDataUpdateCoordinator[Workout | None]):
    coordinator_name: str
    _previous_data: Workout | None
    notification_categories: Incomplete
    def __init__(self, hass: HomeAssistant, client: WithingsClient) -> None: ...
    _last_valid_update: Incomplete
    async def _internal_update_data(self) -> Workout | None: ...

class WithingsDeviceDataUpdateCoordinator(WithingsDataUpdateCoordinator[dict[str, Device]]):
    coordinator_name: str
    _default_update_interval: Incomplete
    async def _internal_update_data(self) -> dict[str, Device]: ...
