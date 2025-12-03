from .models import BluetoothServiceInfoBleak as BluetoothServiceInfoBleak
from .storage import BluetoothStorage as BluetoothStorage
from bluetooth_adapters import AdapterDetails as AdapterDetails, BluetoothAdapters as BluetoothAdapters
from homeassistant.core import callback as callback

@callback
def async_load_history_from_system(adapters: BluetoothAdapters, storage: BluetoothStorage) -> tuple[dict[str, BluetoothServiceInfoBleak], dict[str, BluetoothServiceInfoBleak]]: ...
@callback
def adapter_title(adapter: str, details: AdapterDetails) -> str: ...
