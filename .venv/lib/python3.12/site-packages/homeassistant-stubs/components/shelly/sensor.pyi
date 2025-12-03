from .const import CONF_SLEEP_PERIOD as CONF_SLEEP_PERIOD, SHAIR_MAX_WORK_HOURS as SHAIR_MAX_WORK_HOURS
from .coordinator import ShellyBlockCoordinator as ShellyBlockCoordinator, ShellyConfigEntry as ShellyConfigEntry, ShellyRpcCoordinator as ShellyRpcCoordinator
from .entity import BlockEntityDescription as BlockEntityDescription, RestEntityDescription as RestEntityDescription, RpcEntityDescription as RpcEntityDescription, ShellyBlockAttributeEntity as ShellyBlockAttributeEntity, ShellyRestAttributeEntity as ShellyRestAttributeEntity, ShellyRpcAttributeEntity as ShellyRpcAttributeEntity, ShellySleepingBlockAttributeEntity as ShellySleepingBlockAttributeEntity, ShellySleepingRpcAttributeEntity as ShellySleepingRpcAttributeEntity, async_setup_entry_attribute_entities as async_setup_entry_attribute_entities, async_setup_entry_rest as async_setup_entry_rest, async_setup_entry_rpc as async_setup_entry_rpc
from .utils import async_remove_orphaned_entities as async_remove_orphaned_entities, get_device_entry_gen as get_device_entry_gen, get_device_uptime as get_device_uptime, get_virtual_component_ids as get_virtual_component_ids, is_rpc_wifi_stations_disabled as is_rpc_wifi_stations_disabled
from _typeshed import Incomplete
from aioshelly.block_device import Block as Block
from dataclasses import dataclass
from homeassistant.components.sensor import RestoreSensor as RestoreSensor, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorExtraStoredData as SensorExtraStoredData, SensorStateClass as SensorStateClass
from homeassistant.const import CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, DEGREE as DEGREE, EntityCategory as EntityCategory, LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfApparentPower as UnitOfApparentPower, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfFrequency as UnitOfFrequency, UnitOfPower as UnitOfPower, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.entity_registry import RegistryEntry as RegistryEntry
from homeassistant.helpers.typing import StateType as StateType
from typing import Final

@dataclass(frozen=True, kw_only=True)
class BlockSensorDescription(BlockEntityDescription, SensorEntityDescription): ...
@dataclass(frozen=True, kw_only=True)
class RpcSensorDescription(RpcEntityDescription, SensorEntityDescription): ...
@dataclass(frozen=True, kw_only=True)
class RestSensorDescription(RestEntityDescription, SensorEntityDescription): ...

SENSORS: dict[tuple[str, str], BlockSensorDescription]
REST_SENSORS: Final[Incomplete]
RPC_SENSORS: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, config_entry: ShellyConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BlockSensor(ShellyBlockAttributeEntity, SensorEntity):
    entity_description: BlockSensorDescription
    _attr_native_unit_of_measurement: Incomplete
    def __init__(self, coordinator: ShellyBlockCoordinator, block: Block, attribute: str, description: BlockSensorDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...

class RestSensor(ShellyRestAttributeEntity, SensorEntity):
    entity_description: RestSensorDescription
    @property
    def native_value(self) -> StateType: ...

class RpcSensor(ShellyRpcAttributeEntity, SensorEntity):
    entity_description: RpcSensorDescription
    _attr_options: Incomplete
    def __init__(self, coordinator: ShellyRpcCoordinator, key: str, attribute: str, description: RpcSensorDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...

class BlockSleepingSensor(ShellySleepingBlockAttributeEntity, RestoreSensor):
    entity_description: BlockSensorDescription
    restored_data: SensorExtraStoredData | None
    def __init__(self, coordinator: ShellyBlockCoordinator, block: Block | None, attribute: str, description: BlockSensorDescription, entry: RegistryEntry | None = None) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def native_unit_of_measurement(self) -> str | None: ...

class RpcSleepingSensor(ShellySleepingRpcAttributeEntity, RestoreSensor):
    entity_description: RpcSensorDescription
    restored_data: SensorExtraStoredData | None
    def __init__(self, coordinator: ShellyRpcCoordinator, key: str, attribute: str, description: RpcEntityDescription, entry: RegistryEntry | None = None) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def native_unit_of_measurement(self) -> str | None: ...
