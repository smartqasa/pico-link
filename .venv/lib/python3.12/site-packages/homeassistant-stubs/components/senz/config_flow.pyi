import logging
from .const import DOMAIN as DOMAIN
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow

class OAuth2FlowHandler(config_entry_oauth2_flow.AbstractOAuth2FlowHandler, domain=DOMAIN):
    DOMAIN = DOMAIN
    @property
    def logger(self) -> logging.Logger: ...
    @property
    def extra_authorize_data(self) -> dict: ...
