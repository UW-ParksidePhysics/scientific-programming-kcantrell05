maximum_integer = 20
sequence = range(maximum_integer + 1)
start_stop = [1, 2]
interval = (start_stop[1] - start_stop[0])/(maximum_integer)                                         
coordinates_find_coordinate = []
for index in sequence:
  coordinate = start_stop[0] + index * interval
  coordinates_find_coordinate.append(coordinate)

coordinates_find_coordinate_2 = [start_stop[0] + index * interval for index in range(maximum_integer)]
  
print(f'For x in {start_stop} with {maximum_integer} intervals, the interval length is {interval}, and')
print(f'Using a for loop: x = {coordinates_find_coordinate}')
print(f'Using list comprehension: x = {coordinates_find_coordinate_2}')
