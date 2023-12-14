import re
import numpy as np 

with open("input.txt") as f:
    maps_data = f.readlines()

m = 0
maps = [[]]
for row in maps_data:
    if row != '\n':
        maps[m].append(list(row[:-1]))
    else:
        maps.append([])
        m += 1

maps = [np.stack(ms, axis = 0) for ms in maps]

def col_checker(map):
    for c in range(1,map.shape[1]):
        i = 1
        symm = True
        while (c - i) >= 0 and (c+i-1) < map.shape[1]:
            if (map[:,c-i] != map[:,c+i-1]).any():
                symm = False
                break
            else:
                i += 1
        if symm:
            return c
        else:
            continue
    return False

def row_checker(map):
    for r in range(1,map.shape[0]):
        i = 1
        while (r - i) >= 0 and (r+i-1) < map.shape[0]:
            symm = True
            if (map[r-i,:] != map[r+i-1,:]).any():
                symm = False
                break
            else:
                i += 1
        if symm:
            return r
        else:
            continue
    return -1

def part1(map_list):
    symms = [[],[]]
    for mapi in maps:
        row_symm = row_checker(mapi)
        col_symm = col_checker(mapi)
        if row_symm > 0:
            symms[0].append(row_symm)
        elif col_symm > 0:
            symms[1].append(col_symm)
    return symms
        
axes = part1(maps)

# solution
np.sum(axes[1]) + 100*np.sum(axes[0])
    
            
        

