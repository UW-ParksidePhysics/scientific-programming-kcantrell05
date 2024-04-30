#Make a program that asks the user for a temperature in Fahrenheit degrees and reads the number; computes the corresponding temperature in Celsius degrees; and prints out the input temperature in Fahrenheit and the output temperature in the Celsius scale.
fahrenheit_degrees = input('F=? ')
fahrenheit_degrees = float(fahrenheit_degrees)
celsius_degrees = (fahrenheit_degrees - 32)*5./9
print(f'The temperature in Fahrenheit is: {fahrenheit_degrees} degrees, and the temperature in Celsius is: {celsius_degrees:.3f} degrees')


if __name__ == '__main__':
  pass