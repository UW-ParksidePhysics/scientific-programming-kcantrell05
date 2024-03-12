time_positions = [[0,7.86,15.71,23.57,31.42,39.28,47.14,54.99,62.85,70.71,78.57,86.43,94.29,102.12,109.98,117.83,125.69,133.54,141.40,149.25],[0.00,74.42,140.57,198.45,248.07,289.41,322.49,347.29,363.83,372.10,372.10,363.83,347.29,322.49,289.41,248.07,198.45,140.57,74.42,0.00]]


print("Time (s)  Position (m)")
print("-----------------------")


for time, pos in zip(*time_positions):
  print(f"{time:8.2f}  {pos:10.2f}")

print ()
time_positions_transposed = [list(row) for row in zip(*time_positions)]

print("Time (s)  Position (m)")
print("-----------------------")


for row in time_positions_transposed:
    t, y = row
    print(f"{t:.2f}      {y:.2f}")