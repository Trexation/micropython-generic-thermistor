from machine import ADC
from thermistor import Thermistor

therm = Thermistor(ADC(4, atten=ADC.ATTN_11DB), beta=3435, therm_ohm=10_000, divider_ohm=10_000)

print(therm.read_temperature_fahrenheit())
