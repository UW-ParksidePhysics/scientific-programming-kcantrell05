import math

from numpy import maximum


def sinusoidal_sum(time, number_of_functions, period):
  fourier_series = 0
  for index in range(1, number_of_functions + 1):
    fourier_series += math.sin(2 * math.pi * (2 * index - 1) * time / period)/ (2 * index - 1)
  return fourier_series * 4/math.pi

def piecewise_function(time, period):
  if time < period/2:
    return 1
  elif time == period/2:
    return 0
  elif time > period/2:
    return -1

if __name__ == '__main__':
  maximum_numbers = [1, 3, 5, 10, 30, 100]
  alphas = [0.01, 0.25, 0.49]
  period = 2 * math.pi
  print(f"  n\t Error")
  for maximum_number in maximum_numbers:
    table_row = f'{maximum_number:3}'+ '\t'
    for alpha in alphas:
      time = alpha * period
      piecewise_value = piecewise_function(time, period)
      fourier_value = sinusoidal_sum(time, maximum_number, period)
      error = piecewise_value - fourier_value
      table_row = table_row + f'{error:9.6f}' + '\t'
    print(table_row)




