t = [0,.177, .354, .531, .708, .885, 1.062, 1.239, 1.416]
y = [0,1.5,3.0,4.5,6.0,7.5,9.0,10.5]

zipped = zip(t, y)
result = list(zipped)

print("Time (s)  Position (m)")
print("-----------------------")

for time, position in zip(t, y):
    print(f"{time}  {position}")
