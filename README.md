# Micropython Generic Thermistor Library

Micropython Generic Thermistor Library is a basic software module designed to simplify temperature sensing using NTC thermistors within MicroPython-based projects. The library assumes a generic NTC thermistor on the ground side of a voltage divider. It provides functions for converting raw analog sensor readings into temperature values, taking into account the non-linear nature of thermistors using the β parameter equation.

## Features
- Temperature output in Kelvin, Celsius, or Fahrenheit
- Checks for thermistor shorts to VCC or GND
- Checks for reasonable output values as specified in Constants
- New thermistors only require one line of code!

## Installation - Hardware

## Installation - Software
1. Have a Micropython environment set up on something; for example, an ESP32
2. Upload the thermistor.py file onto the Micropython device; upload steps vary based on familiarity with the terminal, OS, and/or IDE. You can create a new file named thermistor.py on the embedded device and copy-paste the code into the file.
3. Configure the object constructor "Thermistor" with your thermistor's beta & nominal resistance values and with your voltage divider ohm value.
4. See the example



