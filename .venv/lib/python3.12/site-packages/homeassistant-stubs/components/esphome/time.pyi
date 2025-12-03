from .entity import EsphomeEntity as EsphomeEntity, esphome_state_property as esphome_state_property, platform_async_setup_entry as platform_async_setup_entry
from _typeshed import Incomplete
from aioesphomeapi import TimeInfo, TimeState
from datetime import time
from homeassistant.components.time import TimeEntity as TimeEntity

class EsphomeTime(EsphomeEntity[TimeInfo, TimeState], TimeEntity):
    @property
    @esphome_state_property
    def native_value(self) -> time | None: ...
    async def async_set_value(self, value: time) -> None: ...

async_setup_entry: Incomplete
