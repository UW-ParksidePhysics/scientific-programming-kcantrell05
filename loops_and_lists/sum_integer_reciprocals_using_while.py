#Original Scipt:
#summation = 0
#starting_index = 1
#index = starting_index
#maximum_index = 100
#while index < maximum_index:
    #summation += 1/index
#print(f'sum(k = {starting_index}, {maximum_index\1/k = {summation}')

summation = 0
starting_index = 1
index = starting_index
maximum_index = 1000

while index < maximum_index:
    summation += 1/index
    index += 1
print(f'sum(k = {starting_index}, {maximum_index}) 1/k = {summation}')

#Index is not within the loop therefore it will cause an infinite loop.
#K(Max) = 3 Which returns 1.5 K9Max) = 1000 returns 7.48
#LLM Output:
#from __future__ import division
#summation = 0
#starting_index = 1
#index = starting_index
#maximum_index = 1000
#while index < maximum_index:
    #summation += 1 / index
    #index += 1
#print(f'sum(k = {starting_index}, {maximum_index}) 1/k = {summation}')
