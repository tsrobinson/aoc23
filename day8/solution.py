import re
from math import lcm
from itertools import cycle

input = [re.sub('\n','', x) for x in open('input.txt').readlines()]
steps = cycle(input[0])
map = {}

for m in input[2:]:
    path = re.findall('\w{3}', m)
    map[path[0]] = [path[1],path[2]]

# PART 1
loc = 'AAA'
i = 0
while loc != 'ZZZ':
    step = next(steps)
    loc = map[loc][0] if step == "L" else map[loc][1]
    i += 1

# solution
print(i)

# PART 2 - 53754334 (FOR REF. NOT ANSWER)
locs = [x for x in map.keys() if x[-1] == 'A']

step_counts = []
for loc in locs:
    i = 0
    steps = cycle(input[0])
    while loc[-1] != 'Z':
        step = next(steps)
        loc = map[loc][0] if step == "L" else map[loc][1]    
        i += 1
    step_counts.append(i)

# solution
print(lcm(*step_counts))