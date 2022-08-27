"""Constants for the utility meter component."""
DOMAIN = "my_utility_meter"

TARIFF_ICON = "mdi:clock-outline"

QUARTER_HOURLY = "quarter-hourly"
HOURLY = "hourly"
DAILY = "daily"
WEEKLY = "weekly"
MONTHLY = "monthly"
BIMONTHLY = "bimonthly"
QUARTERLY = "quarterly"
YEARLY = "yearly"

METER_TYPES = [
    QUARTER_HOURLY,
    HOURLY,
    DAILY,
    WEEKLY,
    MONTHLY,
    BIMONTHLY,
    QUARTERLY,
    YEARLY,
]

DATA_UTILITY = "my_utility_meter_data"
DATA_TARIFF_SENSORS = "my_utility_meter_sensors"

CONF_METER = "meter"
CONF_SOURCE_SENSOR = "source"
CONF_METER_TYPE = "cycle"
CONF_METER_OFFSET = "offset"
CONF_METER_DELTA_VALUES = "delta_values"
CONF_METER_NET_CONSUMPTION = "net_consumption"
CONF_PAUSED = "paused"
CONF_TARIFFS = "tariffs"
CONF_TARIFF = "tariff"
CONF_TARIFF_ENTITY = "tariff_entity"
CONF_CRON_PATTERN = "cron"

ATTR_TARIFF = "tariff"
ATTR_TARIFFS = "tariffs"
ATTR_VALUE = "value"
ATTR_CRON_PATTERN = "cron pattern"

SIGNAL_START_PAUSE_METER = "my_utility_meter_start_pause"
SIGNAL_RESET_METER = "my_utility_meter_reset"

SERVICE_RESET = "reset"
SERVICE_CALIBRATE_METER = "calibrate"
