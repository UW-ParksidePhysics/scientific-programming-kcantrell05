#Modify the program from Exercise 4.1 such that the Fahrenheit temperature is read from the command line.

import sys
if len(sys.argv) != 2:
  print("Usage: python3 convert_fahrenheit_temperature_to_celsius_from_command_line.py")
fahrenheit_degrees = input('F=?')
fahrenheit_degrees = float(sys.argv[1])
celsius_degrees = (fahrenheit_degrees - 32)*5./9
print(f'The temperature in Fahrenheit is: {fahrenheit_degrees} degrees, and the temperature in Celsius is: {celsius_degrees:.3f} degrees')

if __name__ == '__main__':
  pass