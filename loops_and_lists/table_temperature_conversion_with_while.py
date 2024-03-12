# Write a Python program that prints out a table with Fahrenheit degrees 0, 10, 20, …, 100 in the first column and the corresponding Celsius degrees in the second column using a while loop. Be sure to label the columns as °F and °C. Filename: table_temperature_conversion_with_while.py.

print ('°F,°C ')
print ('------------------')
F = 0
dF = 10
while F <= 100:
    C = (F - 32) * 5.0/9.0
    print(F, C)
    F = F + dF
    print ('------------------')
  