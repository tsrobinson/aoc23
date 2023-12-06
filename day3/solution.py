import re
import numpy as np

# read in and strip newline
input_data = [re.sub('\n','',x) for x in open('input.txt').readlines()]

symbols = '[\\\+\=\-\_\)\(\*\&\^\%\$\#\@\!\%\/]'

# PART 1
parts = []

for row_idx in range(len(input_data)):
    row = input_data[row_idx]
    for match in re.finditer('\d+', row):
        s_idx, e_idx = match.span()

        # get area around number
        start = max([s_idx-1,0])
        end = min([e_idx + 1, len(row)-1])

        # check current row
        if row[start] in symbols or row[end-1] in symbols:
            parts.append(int(match.group()))
        # check near cells in row above
        elif row_idx > 0 and re.search(symbols,input_data[row_idx - 1][start:end]) is not None:
            parts.append(int(match.group()))
        # check near cells in row below
        elif row_idx < len(input_data)-2 and re.search(symbols,input_data[row_idx + 1][start:end]) is not None:
            parts.append(int(match.group()))

# solution
sum(parts)

# PART 2
gears = {}

def au_gears(key, val):
    if key in gears.keys():
        gears[key].append(int(val))
    else:
        gears[key] = [int(val)]

for row_idx in range(len(input_data)):
    row = input_data[row_idx]
    for match in re.finditer('\d+', row):
        s_idx, e_idx = match.span()
        e_idx -= 1
        # get area around number
        start = max([s_idx-1,0])
        end = min([e_idx+1, len(row)-1])

        # check current row 
        if row[start] == "*":
            au_gears(str(row_idx)+'_'+str(start), match.group())
        if row[end] == "*":
            au_gears(str(row_idx)+'_'+str(end), match.group())
        # check cells in row above
        if row_idx > 0:
            for gear in re.finditer("\*",input_data[row_idx - 1][start:end+1]):
                au_gears(str(row_idx - 1)+'_'+str(start + gear.span()[0]), match.group())
        # check cells in row below
        if row_idx < len(input_data)-2:
            for gear in re.finditer("\*",input_data[row_idx + 1][start:end+1]):
                au_gears(str(row_idx + 1)+'_'+str(start + gear.span()[0]), match.group())

# solution
sum([np.prod(gears[key]) for key in gears.keys() if len(gears[key]) == 2])
