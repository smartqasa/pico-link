from enum import IntFlag, StrEnum
from typing import Final

DOMAIN: Final[str]
ATTR_CHANGED_BY: Final[str]
ATTR_CODE_ARM_REQUIRED: Final[str]

class AlarmControlPanelState(StrEnum):
    DISARMED = 'disarmed'
    ARMED_HOME = 'armed_home'
    ARMED_AWAY = 'armed_away'
    ARMED_NIGHT = 'armed_night'
    ARMED_VACATION = 'armed_vacation'
    ARMED_CUSTOM_BYPASS = 'armed_custom_bypass'
    PENDING = 'pending'
    ARMING = 'arming'
    DISARMING = 'disarming'
    TRIGGERED = 'triggered'

class CodeFormat(StrEnum):
    TEXT = 'text'
    NUMBER = 'number'

class AlarmControlPanelEntityFeature(IntFlag):
    ARM_HOME = 1
    ARM_AWAY = 2
    ARM_NIGHT = 4
    TRIGGER = 8
    ARM_CUSTOM_BYPASS = 16
    ARM_VACATION = 32

CONDITION_TRIGGERED: Final[str]
CONDITION_DISARMED: Final[str]
CONDITION_ARMED_HOME: Final[str]
CONDITION_ARMED_AWAY: Final[str]
CONDITION_ARMED_NIGHT: Final[str]
CONDITION_ARMED_VACATION: Final[str]
CONDITION_ARMED_CUSTOM_BYPASS: Final[str]
