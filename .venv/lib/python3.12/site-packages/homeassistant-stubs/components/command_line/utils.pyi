from _typeshed import Incomplete

_LOGGER: Incomplete
_EXEC_FAILED_CODE: int

async def async_call_shell_with_timeout(command: str, timeout: int, *, log_return_code: bool = True) -> int: ...
async def async_check_output_or_log(command: str, timeout: int) -> str | None: ...
