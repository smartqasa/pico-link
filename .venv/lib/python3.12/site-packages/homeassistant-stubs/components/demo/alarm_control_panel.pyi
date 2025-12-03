from homeassistant.components.alarm_control_panel import AlarmControlPanelState as AlarmControlPanelState
from homeassistant.components.manual.alarm_control_panel import ManualAlarm as ManualAlarm
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ARMING_TIME as CONF_ARMING_TIME, CONF_DELAY_TIME as CONF_DELAY_TIME, CONF_TRIGGER_TIME as CONF_TRIGGER_TIME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
