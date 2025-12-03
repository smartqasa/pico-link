from .const import REGEX_NUMBER as REGEX_NUMBER, UNKNOWN_NAME as UNKNOWN_NAME
from _typeshed import Incomplete
from dataclasses import dataclass
from fritzconnection.lib.fritzphonebook import FritzPhonebook
from homeassistant.util import Throttle as Throttle

_LOGGER: Incomplete
MIN_TIME_PHONEBOOK_UPDATE: Incomplete

@dataclass
class Contact:
    name: str
    numbers: list[str]
    vip: bool
    def __init__(self, name: str, numbers: list[str] | None = None, category: str | None = None) -> None: ...

unknown_contact: Incomplete

class FritzBoxPhonebook:
    fph: FritzPhonebook
    phonebook_dict: dict[str, list[str]]
    contacts: list[Contact]
    number_dict: dict[str, Contact]
    host: Incomplete
    username: Incomplete
    password: Incomplete
    phonebook_id: Incomplete
    prefixes: Incomplete
    def __init__(self, host: str, username: str, password: str, phonebook_id: int | None = None, prefixes: list[str] | None = None) -> None: ...
    def init_phonebook(self) -> None: ...
    def update_phonebook(self) -> None: ...
    def get_phonebook_ids(self) -> list[int]: ...
    def get_contact(self, number: str) -> Contact: ...
