"""Automatic recovery for bluetooth adapters."""

from __future__ import annotations

import array
import asyncio
import errno
import logging
import socket
import struct
from contextlib import asynccontextmanager
from dataclasses import dataclass
from functools import cached_property

try:
    from fcntl import ioctl

    import pyric.utils.rfkill as rfkill
except ImportError:
    ioctl = None  # type: ignore
    rfkill = None

from typing import Any, AsyncIterator, cast

import pyric.net.wireless.rfkill_h as rfkh
from bluetooth_adapters import get_adapters_from_hci
from btsocket import btmgmt_protocol, btmgmt_socket
from btsocket.btmgmt_socket import AF_BLUETOOTH, BTPROTO_HCI
from usb_devices import BluetoothDevice, NotAUSBDeviceError

from .util import asyncio_timeout

_LOGGER = logging.getLogger(__name__)

POWER_OFF_TIME = 2
POWER_ON_TIME = 3
MAX_RFKILL_TIME = 3
DBUS_REGISTER_TIME = 3.5

MGMT_PROTOCOL_TIMEOUT = 5

# https://git.kernel.org/pub/scm/bluetooth/bluez.git/tree/lib/hci.h
HCIDEVUP = 0x400448C9  # 201
HCIDEVDOWN = 0x400448CA  # 202


@dataclass
class RFKillInfo:
    """RFKill info."""

    soft_block: bool | None
    hard_block: bool | None
    idx: int | None


def rfkill_unblock(adapter: MGMTBluetoothCtl, rfkill_idx: int) -> bool:
    """Try to remove an rfkill soft block."""
    try:
        with open(rfkill.dpath, "wb") as fout:
            fout.write(
                rfkh.rfkill_event(
                    rfkill_idx, rfkh.RFKILL_TYPE_ALL, rfkh.RFKILL_OP_CHANGE, 0, 0
                )
            )
    except Exception:  # pylint: disable=broad-except
        _LOGGER.exception(
            "RF kill switch unblock of %s (rfkill_idx:%s) failed",
            adapter.name,
            rfkill_idx,
        )
        return False

    return True


def rfkill_list_bluetooth(adapter: MGMTBluetoothCtl) -> RFKillInfo:
    """Execute the rfkill list bluetooth command."""
    try:
        rfkill_dict = rfkill.rfkill_list()
    except FileNotFoundError as ex:
        _LOGGER.debug(
            "rfkill at /dev/rfkill is not accessible, cannot check bluetooth adapter %s: %s",
            adapter.name,
            ex,
        )
        return RFKillInfo(None, None, None)
    except IndexError as ex:
        _LOGGER.debug(
            "rfkill at /dev/rfkill returned unexpected results, cannot check bluetooth adapter %s: %s",
            adapter.name,
            ex,
        )
        return RFKillInfo(None, None, None)
    except PermissionError as ex:
        _LOGGER.debug(
            "Access to rfkill at /dev/rfkill is not permitted, cannot check bluetooth adapter %s: %s",
            adapter.name,
            ex,
        )
        return RFKillInfo(None, None, None)
    except UnicodeDecodeError as ex:
        _LOGGER.debug(
            "RF kill switch check failed - data for %s is not UTF-8 encoded: %s",
            adapter.name,
            ex,
        )
        return RFKillInfo(None, None, None)
    except Exception:  # pylint: disable=broad-except
        _LOGGER.exception("RF kill switch check failed")
        return RFKillInfo(None, None, None)
    try:
        rfkill_hci_state = rfkill_dict[adapter.hci_name]
    except KeyError:
        _LOGGER.debug(
            "RF kill switch check failed - no data for %s. Available data: %s",
            adapter.name,
            rfkill_dict,
        )
        return RFKillInfo(None, None, None)

    return RFKillInfo(
        rfkill_hci_state["soft"], rfkill_hci_state["hard"], rfkill_hci_state["idx"]
    )


class BluetoothMGMTProtocol(asyncio.Protocol):
    """Bluetooth MGMT protocol."""

    def __init__(
        self,
        timeout: float,
        connection_mode_future: asyncio.Future[None],
        sock: socket.socket,
    ) -> None:
        """Initialize the protocol."""
        self.future: asyncio.Future[btmgmt_protocol.Response] | None = None
        self.transport: asyncio.Transport | None = None
        self.timeout = timeout
        self.connection_mode_future = connection_mode_future
        self.loop = asyncio.get_running_loop()
        self.sock = sock

    def connection_made(self, transport: asyncio.BaseTransport) -> None:
        """Handle connection made."""
        if not self.connection_mode_future.done():
            self.connection_mode_future.set_result(None)
        self.transport = cast(asyncio.Transport, transport)

    def data_received(self, data: bytes) -> None:
        """Handle data received."""
        try:
            if (
                self.future
                and not self.future.done()
                and (response := btmgmt_protocol.reader(data))
                and response.cmd_response_frame
            ):
                self.future.set_result(response)
        except ValueError as ex:
            # ValueError: 47 is not a valid Events may happen on newer kernels
            # and we need to ignore these events
            _LOGGER.debug("Error parsing response: %s", ex)

    async def send(self, *args: Any) -> btmgmt_protocol.Response:
        """Send command."""
        pkt_objs = btmgmt_protocol.command(*args)
        self.future = self.loop.create_future()
        if self.transport is None:
            raise btmgmt_socket.BluetoothSocketError("Connection was closed")
        # Write directly to the socket to work around kernel ABI inconsistency
        # where sendto() may return 0 on certain systems (e.g., Odroid M1 with kernel 6.12.43-haos)
        # even though data was successfully sent. Using transport.write() can cause
        # infinite retries in asyncio's transport layer.
        # See: https://github.com/Bluetooth-Devices/habluetooth/pull/303
        # See: https://github.com/home-assistant/core/issues/152204
        data = b"".join(frame.octets for frame in pkt_objs if frame)
        self.sock.send(data)
        cancel_timeout = self.loop.call_later(
            self.timeout, self._timeout_future, self.future
        )
        try:
            return await self.future
        finally:
            cancel_timeout.cancel()
            self.future = None

    def _timeout_future(self, future: asyncio.Future[btmgmt_protocol.Response]) -> None:
        if future and not future.done():
            future.set_exception(asyncio.TimeoutError("Timeout waiting for response"))

    def connection_lost(self, exc: Exception | None) -> None:
        """Handle connection lost."""
        if exc:
            _LOGGER.warning("Bluetooth management socket connection lost: %s", exc)
        self.transport = None


class MGMTBluetoothCtl:
    """Class to control interfaces using the BlueZ management API"""

    def __init__(self, hci_name: str, mac: str, timeout: float) -> None:
        """Initialize the control class."""
        # These get set when we enumerate the controllers
        self.idx: int | None = None
        self.hci_name: str | None = None
        self.mac: str | None = None

        # This is what we expect to find
        self._expected_bdaddr = mac.upper()
        self._expected_hci_name = hci_name

        # Internal state
        self.timeout = timeout
        self.protocol: BluetoothMGMTProtocol | None = None
        self.presented_list: dict[int, str] = {}
        self.sock: socket.socket | None = None

    @cached_property
    def name(self) -> str:
        """Return the name of the adapter."""
        return f"{self.hci_name} [{self.mac}] ({self.idx})"

    async def close(self) -> None:
        """Close the management interface."""
        if self.protocol and self.protocol.transport:
            self.protocol.transport.close()
            self.protocol = None
        btmgmt_socket.close(self.sock)

    async def setup(self) -> None:
        """Set up management interface."""
        sock = btmgmt_socket.open()
        self.sock = sock
        loop = asyncio.get_running_loop()
        connection_made_future: asyncio.Future[None] = loop.create_future()
        try:
            async with asyncio_timeout(5):
                # _create_connection_transport accessed directly to avoid SOCK_STREAM check
                # see https://bugs.python.org/issue38285
                _, protocol = await loop._create_connection_transport(  # type: ignore[attr-defined]
                    sock,
                    lambda: BluetoothMGMTProtocol(
                        self.timeout, connection_made_future, sock
                    ),
                    None,
                    None,
                )
                await connection_made_future
        except asyncio.TimeoutError:
            btmgmt_socket.close(sock)
            raise
        assert isinstance(protocol, BluetoothMGMTProtocol)  # nosec
        self.protocol = protocol
        await self._find_controller()

    async def _find_controller(self) -> None:
        """Find the controller."""
        assert self.protocol is not None  # nosec
        loop = asyncio.get_running_loop()
        # Try to get the adapter index from the hci device first
        # since it can see downed adapters.
        if adapters_from_hci := await loop.run_in_executor(None, get_adapters_from_hci):
            _LOGGER.debug("Found adapters from hci: %s", adapters_from_hci)
            for adapter in adapters_from_hci.values():
                if adapter["bdaddr"] == self._expected_bdaddr:
                    self.idx = adapter["dev_id"]
                    self.hci_name = adapter["name"]
                    self.mac = adapter["bdaddr"]
                    _LOGGER.debug(
                        "Found adapter %s by mac in hci device as %s",
                        self.mac,
                        self.idx,
                    )
                    return

            for adapter in adapters_from_hci.values():
                if adapter["name"] == self._expected_hci_name:
                    self.idx = adapter["dev_id"]
                    self.hci_name = adapter["name"]
                    self.mac = adapter["bdaddr"]
                    _LOGGER.debug(
                        "Found adapter %s by name as hci device %s as %s",
                        self.mac,
                        self._expected_hci_name,
                        self.idx,
                    )
                    return

        idxdata = await self.protocol.send("ReadControllerIndexList", None)
        if idxdata.event_frame.status.value != 0x00:  # 0x00 - Success
            _LOGGER.error(
                "Unable to get hci controllers index list! Event frame status: %s",
                idxdata.event_frame.status,
            )
            return
        if idxdata.cmd_response_frame.num_controllers == 0:
            _LOGGER.warning("There are no BT controllers present in the system!")
            return
        hci_idx_list = getattr(idxdata.cmd_response_frame, "controller_index[i]")
        _LOGGER.debug("hci_idx_list: %s", hci_idx_list)
        for idx in hci_idx_list:
            hci_info = await self.protocol.send("ReadControllerInformation", idx)
            _LOGGER.debug("controller idx %s: %s", idx, hci_info)
            response = hci_info.cmd_response_frame
            mac: str = response.address.upper()
            self.presented_list[idx] = mac
            if self._expected_bdaddr == mac:
                _LOGGER.debug(
                    "Found adapter %s by mac by reading controller info %s", mac, idx
                )
                self.idx = idx
                self.hci_name = f"hci{idx}"
                self.mac = mac
                return
        expected_hci = hci_name_to_number(self._expected_hci_name)
        if maybe_mac := self.presented_list.get(expected_hci):
            _LOGGER.warning(
                "The mac address %s was not found in the adapter list: %s, "
                "falling back to matching by %s",
                self._expected_bdaddr,
                self.presented_list,
                self._expected_hci_name,
            )
            self.idx = expected_hci
            self.hci_name = self._expected_hci_name
            self.mac = maybe_mac

    async def get_powered(self) -> bool | None:
        """Powered state of the interface."""
        assert self.protocol is not None  # nosec
        if self.idx is not None:
            response = await self.protocol.send("ReadControllerInformation", self.idx)
            return response.cmd_response_frame.current_settings.get(
                btmgmt_protocol.SupportedSettings.Powered
            )
        return None

    async def set_powered(self, new_state: bool) -> bool:
        """Set the powered state of the interface."""
        assert self.protocol is not None  # nosec
        response = await self.protocol.send(
            "SetPowered", self.idx, int(new_state is True)
        )
        if response.event_frame.status.value == 0x00:  # 0x00 - Success
            return True
        return False

    async def wait_for_power_state(
        self, new_state: bool, timeout: float
    ) -> bool | None:
        """Wait for the adapter to be powered on or off."""
        assert self.protocol is not None  # nosec
        current_state: bool | None = not new_state
        try:
            async with asyncio_timeout(timeout):
                while True:
                    current_state = await self.get_powered()
                    if current_state == new_state:
                        return current_state
                    await asyncio.sleep(0.1)
        except asyncio.TimeoutError:
            return current_state


async def _check_rfkill(adapter: MGMTBluetoothCtl) -> RFKillInfo:
    """Check if rfkill is blocked."""
    loop = asyncio.get_running_loop()
    try:
        async with asyncio_timeout(MAX_RFKILL_TIME):
            return await loop.run_in_executor(None, rfkill_list_bluetooth, adapter)
    except asyncio.TimeoutError:
        _LOGGER.warning(
            "Checking rfkill for %s timed out after %s seconds!",
            adapter.name,
            MAX_RFKILL_TIME,
        )

    return RFKillInfo(None, None, None)


async def _unblock_rfkill(adapter: MGMTBluetoothCtl, rfkill_idx: int) -> bool:
    """Try to unblock an adapter."""
    loop = asyncio.get_running_loop()
    try:
        async with asyncio_timeout(MAX_RFKILL_TIME):
            return await loop.run_in_executor(None, rfkill_unblock, adapter, rfkill_idx)
    except asyncio.TimeoutError:
        _LOGGER.warning(
            "Unblocking rfkill for %s with idx:%s timed out after %s seconds!",
            adapter.name,
            rfkill_idx,
            MAX_RFKILL_TIME,
        )

    return False


async def _check_or_unblock_rfkill(adapter: MGMTBluetoothCtl) -> bool:
    """Check if rfkill is blocked, and try to unblock if possible.

    Returns False if the adapter is blocked or the state
    could not be determined.
    """
    rfkill_info = await _check_rfkill(adapter)
    if rfkill_info.idx is None:
        _LOGGER.debug(
            "Could not determine rfkill_idx of %s: %s", adapter.name, rfkill_info
        )
        return True

    _LOGGER.debug("rfkill_idx of %s is %s", adapter.name, rfkill_info.idx)

    if rfkill_info.hard_block:
        _LOGGER.warning(
            "Bluetooth adapter %s is hard blocked by rfkill; hardware reboot required: %s",
            adapter.name,
            rfkill_info,
        )
        return False

    if not rfkill_info.soft_block:
        _LOGGER.debug(
            "Bluetooth adapter %s is NOT soft blocked by rfkill: %s",
            adapter.name,
            rfkill_info,
        )
        return True

    _LOGGER.debug(
        "Bluetooth adapter %s is soft blocked by rfkill; trying to unblock",
        adapter.name,
    )
    await _unblock_rfkill(adapter, rfkill_info.idx)
    # Give kernel some time to catch up
    _LOGGER.debug(
        "Waiting %ss for kernel catch up after rfkill unblock", DBUS_REGISTER_TIME
    )
    await asyncio.sleep(DBUS_REGISTER_TIME)

    rfkill_info = await _check_rfkill(adapter)
    if rfkill_info.soft_block or rfkill_info.hard_block:
        _LOGGER.warning(
            "Bluetooth adapter %s is blocked by rfkill and could not be unblocked",
            adapter.name,
        )
        return False

    _LOGGER.debug("Bluetooth adapter %s was successfully unblocked", adapter.name)
    return True


async def recover_adapter(hci: int, mac: str, gone_silent: bool = False) -> bool:
    """Reset the bluetooth adapter."""
    mac = mac.upper()
    hci_name = f"hci{hci}"
    _LOGGER.debug(
        "Attempting to recover bluetooth adapter %s with mac address %s (gone_silent=%s)",
        hci_name,
        mac,
        gone_silent,
    )
    async with _get_adapter(hci_name, mac) as adapter:
        if (
            not adapter
            or adapter.idx is None
            or adapter.hci_name is None
            or adapter.mac is None
        ):
            _LOGGER.warning(
                "Could not find adapter with mac address %s or %s", mac, hci_name
            )
            return False

        if adapter.hci_name != hci_name:
            hci_name = adapter.hci_name
            _LOGGER.warning(
                "Adapter with mac address %s has moved to %s", mac, hci_name
            )

        if adapter.mac != mac:
            mac = adapter.mac
            _LOGGER.warning(
                "Adapter with name %s mac address resolved to %s", hci_name, mac
            )

        if not await _check_or_unblock_rfkill(adapter):
            _LOGGER.warning(
                "rfkill has blocked %s, and could not be unblocked", adapter.name
            )

        # If the adapter has gone silent, do the USB reset as well
        if await _power_cycle_adapter(adapter) and not gone_silent:
            # Give Dbus some time to catch up
            _LOGGER.debug(
                "Waiting %ss for kernel and Dbus to catch up after successful power cycle",
                DBUS_REGISTER_TIME,
            )
            await asyncio.sleep(DBUS_REGISTER_TIME)
            return True

        if not await _usb_reset_adapter(adapter):
            return False

        # Give Dbus some time to catch up in case
        # the adapter is going to move to a new hci number.
        _LOGGER.debug(
            "Waiting %ss for kernel and Dbus to catch up after successful USB reset",
            DBUS_REGISTER_TIME,
        )
        await asyncio.sleep(DBUS_REGISTER_TIME)

    # We just did a USB reset which may cause the adapter
    # to move to a different hci number. Try to find it again.
    async with _get_adapter(hci_name, mac) as adapter:
        if not adapter or adapter.idx is None or adapter.hci_name is None:
            _LOGGER.warning(
                "Could not find adapter with mac address %s or %s", mac, hci_name
            )
            return False

        if adapter.hci_name != hci_name:
            hci_name = adapter.hci_name
            _LOGGER.warning(
                "Adapter with mac address %s has moved to %s", mac, hci_name
            )

        # After the reset, rfkill may be blocked so we need
        # to check and unblock it.
        if not await _check_or_unblock_rfkill(adapter):
            _LOGGER.warning(
                "rfkill has blocked %s, and could not be unblocked", adapter.name
            )
            return False

    return True


@asynccontextmanager
async def _get_adapter(
    hci_name: str, mac: str
) -> AsyncIterator[MGMTBluetoothCtl | None]:
    """Get the adapter."""
    name = f"{hci_name} [{mac}]"
    _LOGGER.debug("Attempting to power cycle bluetooth adapter %s", name)
    adapter = None
    try:
        adapter = MGMTBluetoothCtl(hci_name, mac, MGMT_PROTOCOL_TIMEOUT)
        await adapter.setup()
        _LOGGER.debug(
            "_get_adapter: %s (hci_name=%s) (mac=%s) (idx=%s)",
            name,
            adapter.hci_name,
            adapter.mac,
            adapter.idx,
        )
        if adapter.idx is not None:
            yield adapter
        else:
            yield None
    except btmgmt_socket.BluetoothSocketError as ex:
        _LOGGER.warning(
            "Getting Bluetooth adapter failed %s "
            "because the system cannot create a bluetooth socket: %s",
            name,
            ex,
        )
        yield None
    except OSError as ex:
        _LOGGER.warning("Getting Bluetooth adapter %s failed: %s", name, ex)
        yield None
    except asyncio.TimeoutError:
        _LOGGER.warning("Getting Bluetooth adapter %s failed due to timeout", name)
        yield None
    finally:
        if adapter:
            try:
                await adapter.close()
            except Exception as ex:  # pylint: disable=broad-except
                _LOGGER.warning("Closing Bluetooth adapter %s failed: %s", name, ex)


async def _power_cycle_adapter(adapter: MGMTBluetoothCtl) -> bool:
    _LOGGER.debug("Attempting to power cycle bluetooth adapter %s", adapter.name)
    try:
        return await _execute_reset(adapter)
    except btmgmt_socket.BluetoothSocketError as ex:
        _LOGGER.warning(
            "Bluetooth adapter %s could not be reset "
            "because the system cannot create a bluetooth socket: %s",
            adapter.name,
            ex,
        )
        return False
    except OSError as ex:
        _LOGGER.warning("Bluetooth adapter %s could not be reset: %s", adapter.name, ex)
        return False
    except asyncio.TimeoutError:
        _LOGGER.warning(
            "Bluetooth adapter %s could not be reset due to timeout after %s seconds",
            adapter.name,
            adapter.timeout,
        )
        return False


def hci_name_to_number(hci_name: str) -> int:
    """Convert hci name to number."""
    return int(hci_name.removeprefix("hci"))


async def _usb_reset_adapter(adapter: MGMTBluetoothCtl) -> bool:
    """Reset the bluetooth adapter."""
    assert adapter.hci_name is not None  # nosec
    hci = hci_name_to_number(adapter.hci_name)
    _LOGGER.debug("Executing USB reset for Bluetooth adapter hci%i", hci)
    dev = BluetoothDevice(hci)
    try:
        return await dev.async_reset()
    except NotAUSBDeviceError as ex:
        _LOGGER.debug(
            "hci%s is not a USB devices while attempting USB reset: %s", hci, ex
        )
        return False
    except FileNotFoundError as ex:
        _LOGGER.debug("hci%s not found while attempting USB reset: %s", hci, ex)
        return False
    except PermissionError as ex:
        _LOGGER.info(
            "hci%s permission denied to %s while attempting USB reset: %s",
            hci,
            ex.filename,
            ex,
        )
        return False
    except Exception as ex:  # pylint: disable=broad-except
        _LOGGER.exception(
            "Unexpected error while attempting USB reset of hci%s: %s", hci, ex
        )
        return False


async def _set_adapter_up_down(
    adapter: MGMTBluetoothCtl,
    sock: socket.socket,
    loop: asyncio.AbstractEventLoop,
    code: int,
    state: str,
) -> None:
    """Set the adapter up or down."""
    req_str = struct.pack("H", adapter.idx)
    request = array.array("b", req_str)
    _LOGGER.debug("Setting hci%i %s", adapter.idx, state)
    await loop.run_in_executor(None, ioctl, sock.fileno(), code, request[0])


async def _bounce_adapter_interface(
    adapter: MGMTBluetoothCtl, *, up: bool, down: bool
) -> None:
    """Bounce the adapter ex. hciconfig down/up."""
    loop = asyncio.get_running_loop()
    assert adapter.idx is not None, "Adapter must have an idx"  # nosec
    sock = await loop.run_in_executor(None, raw_open, adapter.idx)
    try:
        _LOGGER.debug("Bouncing Bluetooth adapter hci%i", adapter.idx)
        if down:
            await _set_adapter_up_down(adapter, sock, loop, HCIDEVDOWN, "down")
            await asyncio.sleep(0.5)
        if up:
            await _set_adapter_up_down(adapter, sock, loop, HCIDEVUP, "up")
            await asyncio.sleep(0.5)
        _LOGGER.debug("Finished bouncing hci%i", adapter.idx)
    finally:
        await loop.run_in_executor(None, raw_close, sock)


async def _execute_reset(adapter: MGMTBluetoothCtl) -> bool:
    """Execute the reset."""
    timed_out_getting_powered: bool = False
    power_state_before_reset: bool | None = None
    try:
        power_state_before_reset = await adapter.get_powered()
    except AttributeError as ex:
        _LOGGER.warning(
            "Could not determine the power state of the Bluetooth adapter %s: %s",
            adapter.name,
            ex,
        )
    except asyncio.TimeoutError:
        _LOGGER.warning(
            "Could not determine the power state of the Bluetooth adapter %s due to timeout after %s seconds",
            adapter.name,
            adapter.timeout,
        )
        timed_out_getting_powered = True
    except Exception:  # pylint: disable=broad-except
        _LOGGER.exception(
            "Could not determine the power state of the Bluetooth adapter %s: %s",
            adapter.name,
        )

    # Do not attempt to power off if it timed out getting the power state
    # as it likely means the adapter interface is frozen and will not respond to
    # power off commands so we need to proceed to bounce the interface
    if not timed_out_getting_powered:
        try:
            await _execute_power_off(adapter, power_state_before_reset)
        except asyncio.TimeoutError:
            _LOGGER.warning(
                "Could not reset the power state of the Bluetooth adapter %s due to timeout after %s seconds",
                adapter.name,
                adapter.timeout,
            )
        except Exception:
            _LOGGER.exception(
                "Could not reset the power state of the Bluetooth adapter %s",
                adapter.name,
            )

    try:
        await _bounce_adapter_interface(adapter, down=True, up=True)
    except Exception as ex:  # pylint: disable=broad-except
        _LOGGER.warning(
            "Could not cycle the Bluetooth adapter %s: %s", adapter.name, ex
        )

    try:
        power_on_ok = await _execute_power_on(adapter, power_state_before_reset)
    except asyncio.TimeoutError:
        _LOGGER.warning(
            "Could not reset the power state of the Bluetooth adapter %s due to timeout after %s seconds",
            adapter.name,
            adapter.timeout,
        )
        return False
    except Exception:
        _LOGGER.exception(
            "Could not reset the power state of the Bluetooth adapter %s", adapter.name
        )
        return False

    if not power_on_ok:
        return False

    try:
        await _bounce_adapter_interface(adapter, down=False, up=True)
    except OSError as ex:
        if ex.errno == errno.EALREADY:
            _LOGGER.debug("Adapter %s is already up", adapter.name)
            return True
        _LOGGER.warning(
            "Could not bring up the Bluetooth adapter %s: %s", adapter.name, ex
        )
        return False
    except Exception as ex:  # pylint: disable=broad-except
        _LOGGER.warning(
            "Could not bring up the Bluetooth adapter %s: %s", adapter.name, ex
        )
        return False

    return True


async def _execute_power_on(
    adapter: MGMTBluetoothCtl, power_state_before_reset: bool | None
) -> bool:
    """Execute the power off."""
    try:
        await adapter.set_powered(True)
    except AttributeError as ex:
        _LOGGER.warning(
            "Could not re-enable power after cycle of the Bluetooth adapter %s: %s",
            adapter.name,
            ex,
        )
        return False

    pstate_after = await adapter.wait_for_power_state(True, POWER_ON_TIME)

    # Check the state after the reset
    if pstate_after is True:
        if power_state_before_reset is False:
            _LOGGER.debug(
                "Bluetooth adapter %s successfully turned back ON", adapter.name
            )
        else:
            _LOGGER.debug(
                "Power state of bluetooth adapter %s is ON after power cycle",
                adapter.name,
            )
        return True

    if pstate_after is False:
        _LOGGER.warning(
            "Power state of bluetooth adapter %s is OFF after power cycle", adapter.name
        )
        return False

    _LOGGER.debug(
        "Power state of bluetooth adapter %s could not be determined after power cycle",
        adapter.name,
    )
    return False


async def _execute_power_off(
    adapter: MGMTBluetoothCtl, power_state_before_reset: bool | None
) -> bool:
    """Execute the power off."""
    if power_state_before_reset is True:
        _LOGGER.debug("Current power state of bluetooth adapter is ON.")
        try:
            await adapter.set_powered(False)
        except AttributeError as ex:
            _LOGGER.warning(
                "Could not power cycle the Bluetooth adapter %s: %s", adapter.name, ex
            )
            return False
        await adapter.wait_for_power_state(False, POWER_OFF_TIME)
    elif power_state_before_reset is False:
        _LOGGER.debug(
            "Current power state of bluetooth adapter %s is OFF, trying to turn it back ON",
            adapter.name,
        )
    else:
        _LOGGER.debug("Power state of bluetooth adapter could not be determined")
        return False

    return True


def raw_open(adapter_idx: int) -> socket.socket:
    """Create a bluetooth socket for a specific adapter."""
    sock = socket.socket(AF_BLUETOOTH, socket.SOCK_RAW, BTPROTO_HCI)
    sock.bind((adapter_idx,))
    return sock


def raw_close(bt_socket: socket.socket) -> None:
    """Close the bluetooth socket."""
    fd = bt_socket.detach()
    socket.close(fd)
