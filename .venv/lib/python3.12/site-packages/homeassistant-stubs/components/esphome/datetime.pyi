from .entity import EsphomeEntity as EsphomeEntity, esphome_state_property as esphome_state_property, platform_async_setup_entry as platform_async_setup_entry
from _typeshed import Incomplete
from aioesphomeapi import DateTimeInfo, DateTimeState
from datetime import datetime
from homeassistant.components.datetime import DateTimeEntity as DateTimeEntity

class EsphomeDateTime(EsphomeEntity[DateTimeInfo, DateTimeState], DateTimeEntity):
    @property
    @esphome_state_property
    def native_value(self) -> datetime | None: ...
    async def async_set_value(self, value: datetime) -> None: ...

async_setup_entry: Incomplete
