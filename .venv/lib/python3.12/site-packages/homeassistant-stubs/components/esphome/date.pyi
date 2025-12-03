from .entity import EsphomeEntity as EsphomeEntity, esphome_state_property as esphome_state_property, platform_async_setup_entry as platform_async_setup_entry
from _typeshed import Incomplete
from aioesphomeapi import DateInfo, DateState
from datetime import date
from homeassistant.components.date import DateEntity as DateEntity

class EsphomeDate(EsphomeEntity[DateInfo, DateState], DateEntity):
    @property
    @esphome_state_property
    def native_value(self) -> date | None: ...
    async def async_set_value(self, value: date) -> None: ...

async_setup_entry: Incomplete
