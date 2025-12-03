from datetime import datetime, timedelta
from typing import Literal, TypedDict

class StatisticResult(TypedDict):
    meta: StatisticMetaData
    stat: StatisticData

class StatisticDataTimestampBase(TypedDict):
    start_ts: float

class StatisticDataBase(TypedDict):
    start: datetime

class StatisticMixIn(TypedDict, total=False):
    state: float
    sum: float
    min: float
    max: float
    mean: float

class StatisticData(StatisticDataBase, StatisticMixIn, total=False):
    last_reset: datetime | None

class StatisticDataTimestamp(StatisticDataTimestampBase, StatisticMixIn, total=False):
    last_reset_ts: float | None

class StatisticMetaData(TypedDict):
    has_mean: bool
    has_sum: bool
    name: str | None
    source: str
    statistic_id: str
    unit_of_measurement: str | None

class CalendarStatisticPeriod(TypedDict, total=False):
    period: Literal['hour', 'day', 'week', 'month', 'year']
    offset: int

class FixedStatisticPeriod(TypedDict, total=False):
    end_time: datetime
    start_time: datetime

class RollingWindowStatisticPeriod(TypedDict, total=False):
    duration: timedelta
    offset: timedelta

class StatisticPeriod(TypedDict, total=False):
    calendar: CalendarStatisticPeriod
    fixed_period: FixedStatisticPeriod
    rolling_window: RollingWindowStatisticPeriod
