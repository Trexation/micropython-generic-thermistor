from machine import ADC
from thermistor import Thermistor
import time

therm = Thermistor(ADC(4, atten=ADC.ATTN_11DB), beta=3435, therm_ohm=10_000, divider_ohm=10_000)

while True:
    print("Measured Voltage:      " + str(therm.read_voltage()) + " V")
    print("Measured Resistance:   " + str(therm.read_resistance()) + " Ohm")
    print("Measured Temperature:  " + str(therm.read_temperature_celsius()) + " C")
    print("")
    time.sleep(2)

