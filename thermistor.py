from math import log

# CONSTANTS
VCC = 3.3  # Voltage In
T_0 = 298.15  # Kelvin
THERM_MIN = 263  # Kelvin, min expected thermistor value
THERM_MAX = 333  # Kelvin, max expected thermistor value
KELVIN_AT_0_CELSIUS = 273.15
UV_TO_V_CONVERSION = 1e6  # Microvolts in a Volt
FAHRENHEIT_MULTIPLIER = 9 / 5
FAHRENHEIT_OFFSET = 32


class Thermistor:
    def __init__(self, pin_adc, beta, therm_ohm, divider_ohm):
        # todo: Add some checks here

        self.pin = pin_adc
        self.beta = beta
        self.therm_ohm = therm_ohm
        self.divider_ohm = divider_ohm

    def read_voltage(self):
        """
        Assumes a voltage divider with ground side thermistor, provides the voltage drop accross the thermistor.
        """
        return self.pin.read_uv() / UV_TO_V_CONVERSION

    def read_resistance(self):
        """
        Assumes a voltage divider with ground side thermistor, provides the resistance accross the thermistor based on voltage drop.
        """
        voltage_reading = self.read_voltage()
        try:
            resistance_therm = (self.divider_ohm) / (VCC / voltage_reading - 1)
            if resistance_therm > self.therm_ohm * 10 or resistance_therm < self.therm_ohm / 10:
                raise ZeroDivisionError
            return resistance_therm
        except ZeroDivisionError:
            raise RuntimeError("Thermistor seems broken; there's a connection issue")

    def beta_parameter_equation(self, resistance_measured):
        """
        A method of converting a measured resistance, beta value, nominal resistance, and nominal temperature into the current temperature in Kelvin.
        Read more here: https://en.wikipedia.org/wiki/Thermistor#B_or_%CE%B2_parameter_equation
        """
        return (1 / T_0 + (1 / self.beta) * log(resistance_measured / self.therm_ohm)) ** -1

    def read_temperature_kelvin(self):
        """
        Applies the beta_parameter_equation to get the temperature in Kelvin then checks that the result is within the specified range
        as defined with THERM_MIN and THERM_MAX.
        """
        temp = self.beta_parameter_equation(self.read_resistance())
        if THERM_MIN < temp < THERM_MAX:
            return temp
        else:
            raise RuntimeError("Thermistor seems broken; reading a temperature of: " + str(temp) + "Kelvin")

    def read_temperature_celsius(self):
        return self.read_temperature_kelvin() - KELVIN_AT_0_CELSIUS

    def read_temperature_fahrenheit(self):
        return self.read_temperature_celsius() * FAHRENHEIT_MULTIPLIER + FAHRENHEIT_OFFSET
