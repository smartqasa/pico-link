from _typeshed import Incomplete
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path

RESTORE_BACKUP_FILE: str
KEEP_BACKUPS: Incomplete
KEEP_DATABASE: Incomplete
_LOGGER: Incomplete

@dataclass
class RestoreBackupFileContent:
    backup_file_path: Path
    password: str | None
    remove_after_restore: bool
    restore_database: bool
    restore_homeassistant: bool

def password_to_key(password: str) -> bytes: ...
def restore_backup_file_content(config_dir: Path) -> RestoreBackupFileContent | None: ...
def _clear_configuration_directory(config_dir: Path, keep: Iterable[str]) -> None: ...
def _extract_backup(config_dir: Path, restore_content: RestoreBackupFileContent) -> None: ...
def restore_backup(config_dir_path: str) -> bool: ...
