import re
import numpy as np

times = [int(x.group()) for x in re.finditer('\d+', open('input.txt').readlines()[0])]
distances = [int(x.group()) for x in re.finditer('\d+', open('input.txt').readlines()[1])]

possibilities = []
for i in range(len(times)):
    travel = [(times[i]-x)*x > distances[i] for x in range(times[i])] # could improve with early termination
    possibilities.append(sum(travel))

# solution
np.prod(possibilities)

# PART 2

time = ''
distance = ''
for i in range(len(times)):
    time += str(times[i]) 
    distance += str(distances[i]) 
time = int(time)
distance = int(distance)

i = 0
while (time-i)*i <= distance:
    i += 1

# solution
(time - 2*i) + 1