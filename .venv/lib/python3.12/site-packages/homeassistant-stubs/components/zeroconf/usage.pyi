from .models import HaZeroconf as HaZeroconf
from homeassistant.helpers.frame import ReportBehavior as ReportBehavior, report_usage as report_usage

def install_multiple_zeroconf_catcher(hass_zc: HaZeroconf) -> None: ...
