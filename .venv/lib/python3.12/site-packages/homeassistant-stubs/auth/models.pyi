from . import permissions as perm_mdl
from .const import GROUP_ID_ADMIN as GROUP_ID_ADMIN
from attr import Attribute
from datetime import datetime, timedelta
from homeassistant.const import __version__ as __version__
from homeassistant.data_entry_flow import FlowContext as FlowContext, FlowResult as FlowResult
from ipaddress import IPv4Address, IPv6Address
from propcache import cached_property
from typing import Any, NamedTuple

TOKEN_TYPE_NORMAL: str
TOKEN_TYPE_SYSTEM: str
TOKEN_TYPE_LONG_LIVED_ACCESS_TOKEN: str

class AuthFlowContext(FlowContext, total=False):
    credential_only: bool
    ip_address: IPv4Address | IPv6Address
    redirect_uri: str
AuthFlowResult = FlowResult[AuthFlowContext, tuple[str, str]]

class Group:
    name: str | None
    policy: perm_mdl.PolicyType
    id: str
    system_generated: bool
    def __init__(self, name, policy, id, system_generated) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

def _handle_permissions_change(self, user_attr: Attribute, new: Any) -> Any: ...

class User:
    name: str | None
    perm_lookup: perm_mdl.PermissionLookup
    id: str
    is_owner: bool
    is_active: bool
    system_generated: bool
    local_only: bool
    groups: list[Group]
    credentials: list[Credentials]
    refresh_tokens: dict[str, RefreshToken]
    @cached_property
    def permissions(self) -> perm_mdl.AbstractPermissions: ...
    @cached_property
    def is_admin(self) -> bool: ...
    def invalidate_cache(self) -> None: ...
    def __init__(self, name, perm_lookup, id, is_owner, is_active, system_generated, local_only, groups, credentials, refresh_tokens) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class RefreshToken:
    user: User
    client_id: str | None
    access_token_expiration: timedelta
    client_name: str | None
    client_icon: str | None
    token_type: str
    id: str
    created_at: datetime
    token: str
    jwt_key: str
    last_used_at: datetime | None
    last_used_ip: str | None
    expire_at: float | None
    credential: Credentials | None
    version: str | None
    def __init__(self, user, client_id, access_token_expiration, client_name, client_icon, token_type, id, created_at, token, jwt_key, last_used_at, last_used_ip, expire_at, credential, version) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class Credentials:
    auth_provider_type: str
    auth_provider_id: str | None
    data: dict
    id: str
    is_new: bool
    def __init__(self, auth_provider_type, auth_provider_id, data, id, is_new) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class UserMeta(NamedTuple):
    name: str | None
    is_active: bool
    group: str | None = ...
    local_only: bool | None = ...
