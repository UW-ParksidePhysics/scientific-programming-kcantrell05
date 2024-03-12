# maximum_integer = n
# integers = [1,1+n]
# sum_of_integers = maximum_integer + 1
maximum_integer = 4

sequence = range(1, maximum_integer + 1)
total = 0
for index in sequence:
    total += index


gauss_sum = (maximum_integer * (maximum_integer + 1)) / 2


print(f'n = {maximum_integer}')
print(f'sum (1, {maximum_integer}) = {total}')
print(f'n(n+1)/2 = {gauss_sum}')
