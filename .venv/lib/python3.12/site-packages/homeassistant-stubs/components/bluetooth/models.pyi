from _typeshed import Incomplete
from collections.abc import Callable
from home_assistant_bluetooth import BluetoothServiceInfoBleak

BluetoothChange: Incomplete
type BluetoothCallback = Callable[[BluetoothServiceInfoBleak, BluetoothChange], None]
type ProcessAdvertisementCallback = Callable[[BluetoothServiceInfoBleak], bool]
