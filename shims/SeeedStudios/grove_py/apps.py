from counterfit_connection import CounterFitConnection
from counterfit_shims_grove.grove_light_sensor_v1_2 import GroveLightSensor
from counterfit_shims_grove.grove_led import GroveLed
CounterFitConnection.init('127.0.0.1', 5000)
light_sensor = GroveLightSensor(1, 1231)
sensor_value = light_sensor.light