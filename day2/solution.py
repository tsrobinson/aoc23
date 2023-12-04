import re

# read in and strip newline
input_data = [re.sub('\n','',x) for x in open('input.txt').readlines()]

## PART 1
# max is 12 red, 13 green, 14 blue
pattern = '1[5-9] [rgb]|[2-9]\d+ [rgb]|1[3-4] r|14 g'

# +1 due to 0 indexing
possible = [i +1 for i in range(len(input_data)) if not bool(re.search(pattern, input_data[i]))]

# solution
sum(possible)

## PART 2
power = []

for x in input_data:
    red= max([int(y) for y in re.findall('\d+(?=\sred)',x)])
    blue = max([int(y) for y in re.findall('\d+(?=\sblue)',x)])
    green = max([int(y) for y in re.findall('\d+(?=\sgreen)',x)])
    power.append(red*blue*green)

# solution
sum(power)