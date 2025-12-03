import ssl
from _typeshed import Incomplete
from enum import StrEnum
from functools import cache

class SSLCipherList(StrEnum):
    PYTHON_DEFAULT = 'python_default'
    INTERMEDIATE = 'intermediate'
    MODERN = 'modern'
    INSECURE = 'insecure'

SSL_CIPHER_LISTS: Incomplete

@cache
def _client_context_no_verify(ssl_cipher_list: SSLCipherList) -> ssl.SSLContext: ...
@cache
def _client_context(ssl_cipher_list: SSLCipherList = ...) -> ssl.SSLContext: ...

_DEFAULT_SSL_CONTEXT: Incomplete
_DEFAULT_NO_VERIFY_SSL_CONTEXT: Incomplete
_NO_VERIFY_SSL_CONTEXTS: Incomplete
_SSL_CONTEXTS: Incomplete

def get_default_context() -> ssl.SSLContext: ...
def get_default_no_verify_context() -> ssl.SSLContext: ...
def client_context_no_verify(ssl_cipher_list: SSLCipherList = ...) -> ssl.SSLContext: ...
def client_context(ssl_cipher_list: SSLCipherList = ...) -> ssl.SSLContext: ...
def create_no_verify_ssl_context(ssl_cipher_list: SSLCipherList = ...) -> ssl.SSLContext: ...
def server_context_modern() -> ssl.SSLContext: ...
def server_context_intermediate() -> ssl.SSLContext: ...
