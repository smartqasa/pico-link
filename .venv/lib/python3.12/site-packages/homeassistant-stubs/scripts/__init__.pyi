from collections.abc import Sequence
from homeassistant import runner as runner
from homeassistant.bootstrap import async_mount_local_lib_path as async_mount_local_lib_path
from homeassistant.config import get_default_config_dir as get_default_config_dir
from homeassistant.requirements import pip_kwargs as pip_kwargs
from homeassistant.util.package import install_package as install_package, is_installed as is_installed, is_virtual_env as is_virtual_env

def run(args: list[str]) -> int: ...
def extract_config_dir(args: Sequence[str] | None = None) -> str: ...
