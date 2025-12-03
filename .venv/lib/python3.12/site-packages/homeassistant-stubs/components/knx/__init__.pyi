from .const import CONF_KNX_CONNECTION_TYPE as CONF_KNX_CONNECTION_TYPE, CONF_KNX_EXPOSE as CONF_KNX_EXPOSE, CONF_KNX_INDIVIDUAL_ADDRESS as CONF_KNX_INDIVIDUAL_ADDRESS, CONF_KNX_KNXKEY_FILENAME as CONF_KNX_KNXKEY_FILENAME, CONF_KNX_KNXKEY_PASSWORD as CONF_KNX_KNXKEY_PASSWORD, CONF_KNX_LOCAL_IP as CONF_KNX_LOCAL_IP, CONF_KNX_MCAST_GRP as CONF_KNX_MCAST_GRP, CONF_KNX_MCAST_PORT as CONF_KNX_MCAST_PORT, CONF_KNX_RATE_LIMIT as CONF_KNX_RATE_LIMIT, CONF_KNX_ROUTE_BACK as CONF_KNX_ROUTE_BACK, CONF_KNX_ROUTING as CONF_KNX_ROUTING, CONF_KNX_ROUTING_BACKBONE_KEY as CONF_KNX_ROUTING_BACKBONE_KEY, CONF_KNX_ROUTING_SECURE as CONF_KNX_ROUTING_SECURE, CONF_KNX_ROUTING_SYNC_LATENCY_TOLERANCE as CONF_KNX_ROUTING_SYNC_LATENCY_TOLERANCE, CONF_KNX_SECURE_DEVICE_AUTHENTICATION as CONF_KNX_SECURE_DEVICE_AUTHENTICATION, CONF_KNX_SECURE_USER_ID as CONF_KNX_SECURE_USER_ID, CONF_KNX_SECURE_USER_PASSWORD as CONF_KNX_SECURE_USER_PASSWORD, CONF_KNX_STATE_UPDATER as CONF_KNX_STATE_UPDATER, CONF_KNX_TELEGRAM_LOG_SIZE as CONF_KNX_TELEGRAM_LOG_SIZE, CONF_KNX_TUNNELING as CONF_KNX_TUNNELING, CONF_KNX_TUNNELING_TCP as CONF_KNX_TUNNELING_TCP, CONF_KNX_TUNNELING_TCP_SECURE as CONF_KNX_TUNNELING_TCP_SECURE, CONF_KNX_TUNNEL_ENDPOINT_IA as CONF_KNX_TUNNEL_ENDPOINT_IA, DATA_HASS_CONFIG as DATA_HASS_CONFIG, DOMAIN as DOMAIN, KNX_ADDRESS as KNX_ADDRESS, KNX_MODULE_KEY as KNX_MODULE_KEY, SUPPORTED_PLATFORMS_UI as SUPPORTED_PLATFORMS_UI, SUPPORTED_PLATFORMS_YAML as SUPPORTED_PLATFORMS_YAML, TELEGRAM_LOG_DEFAULT as TELEGRAM_LOG_DEFAULT
from .device import KNXInterfaceDevice as KNXInterfaceDevice
from .expose import KNXExposeSensor as KNXExposeSensor, KNXExposeTime as KNXExposeTime, create_knx_exposure as create_knx_exposure
from .project import KNXProject as KNXProject
from .schema import BinarySensorSchema as BinarySensorSchema, ButtonSchema as ButtonSchema, ClimateSchema as ClimateSchema, CoverSchema as CoverSchema, DateSchema as DateSchema, DateTimeSchema as DateTimeSchema, EventSchema as EventSchema, ExposeSchema as ExposeSchema, FanSchema as FanSchema, LightSchema as LightSchema, NotifySchema as NotifySchema, NumberSchema as NumberSchema, SceneSchema as SceneSchema, SelectSchema as SelectSchema, SensorSchema as SensorSchema, SwitchSchema as SwitchSchema, TextSchema as TextSchema, TimeSchema as TimeSchema, WeatherSchema as WeatherSchema
from .services import register_knx_services as register_knx_services
from .storage.config_store import KNXConfigStore as KNXConfigStore
from .telegrams import Telegrams as Telegrams
from .websocket import register_panel as register_panel
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_EVENT as CONF_EVENT, CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, CONF_TYPE as CONF_TYPE, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry
from homeassistant.helpers.reload import async_integration_yaml_config as async_integration_yaml_config
from homeassistant.helpers.storage import STORAGE_DIR as STORAGE_DIR
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Final
from xknx.core import XknxConnectionState
from xknx.core.telegram_queue import TelegramQueue as TelegramQueue
from xknx.dpt import DPTBase
from xknx.io import ConnectionConfig
from xknx.telegram import AddressFilter, Telegram as Telegram
from xknx.telegram.address import DeviceGroupAddress as DeviceGroupAddress

_LOGGER: Incomplete
_KNX_YAML_CONFIG: Final[str]
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_update_entry(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_remove_entry(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: ConfigEntry, device_entry: DeviceEntry) -> bool: ...

class KNXModule:
    hass: Incomplete
    config_yaml: Incomplete
    connected: bool
    exposures: list[KNXExposeSensor | KNXExposeTime]
    service_exposures: dict[str, KNXExposeSensor | KNXExposeTime]
    entry: Incomplete
    project: Incomplete
    config_store: Incomplete
    xknx: Incomplete
    telegrams: Incomplete
    interface_device: Incomplete
    _address_filter_transcoder: dict[AddressFilter, type[DPTBase]]
    group_address_transcoder: dict[DeviceGroupAddress, type[DPTBase]]
    knx_event_callback: TelegramQueue.Callback
    def __init__(self, hass: HomeAssistant, config: ConfigType, entry: ConfigEntry) -> None: ...
    async def start(self) -> None: ...
    async def stop(self, event: Event | None = None) -> None: ...
    def connection_config(self) -> ConnectionConfig: ...
    def connection_state_changed_cb(self, state: XknxConnectionState) -> None: ...
    def telegram_received_cb(self, telegram: Telegram) -> None: ...
    def register_event_callback(self) -> TelegramQueue.Callback: ...
