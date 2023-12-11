import re
import numpy as np
import itertools

map = np.array([list(p) for x in open('input.txt').readlines() for p in re.sub('\n','', x).split()])

# BOTH PARTS GENERAL SOLUTION

# Find empty row and column indexes
empty_rows = [i for i in range(map.shape[0]) if set(map[i]) == {"."}]
empty_cols = [i for i in range(map.shape[1]) if set(map[:,i]) == {"."}]

# Construct dictionary of galaxy positions
galaxies = {}
g = 0
for i in range(map.shape[0]):
    for j in range(map.shape[1]):
        if map[i,j] == "#":
            galaxies[g] = (i,j)
            g+=1

# Create paths between every pair of galaxies
g_combs = list(itertools.combinations(galaxies.keys(), 2))        

# Distance function
def g_dist_space(pair, empty_multiplier = 1):
    g1x, g1y = galaxies[pair[0]]
    g2x, g2y = galaxies[pair[1]]

    # Count no. of times you pass empty space (row or col)
    x_empty_rows = sum([er in empty_rows for er in range(g1x, g2x, 1 if g2x > g1x else -1)])
    x_empty_cols = sum([ec in empty_cols for ec in range(g1y, g2y, 1 if g2y > g1y else -1)])

    x_empty = x_empty_rows + x_empty_cols
    steps = abs(g2x - g1x) + abs(g2y - g1y)

    total_steps = (steps-x_empty) + x_empty*empty_multiplier

    return total_steps

# part 1 solution
sum([g_dist_space(p, 2) for p in g_combs])
# part 2 solution
sum([g_dist_space(p, 1_000_000) for p in g_combs])

###########

## PART 1 ORIGINAL
# Pasting here to archive my original solution


# # expand rows
# map_exp = map[:0]
# for r in range(map.shape[0]):
#     map_exp = np.append(map_exp, map[r].reshape(1, len(map[r])), axis  = 0)
#     if set(map[r]) == {'.'}:
#         map_exp = np.append(map_exp, map[r].reshape(1, len(map[r])), axis  = 0)

# # expand cols
# c = 0    
# while c < map_exp.shape[1]:
#     if set(map_exp[:,c]) == {'.'}:
#         map_exp = np.insert(map_exp, c, map_exp[:,c], axis  = 1)
#         c+=1 # skip inserted col
#     c+=1

# # hash galaxies

# galaxies = {}
# g = 0
# for i in range(map_exp.shape[0]):
#     for j in range(map_exp.shape[1]):
#         if map_exp[i,j] == "#":
#             galaxies[g] = (i,j)
#             g+=1

# g_combs = list(itertools.combinations(galaxies.keys(), 2))

# def g_dist(pair):
#     g1x, g1y = galaxies[pair[0]]
#     g2x, g2y = galaxies[pair[1]]

#     return abs(g2x - g1x) + abs(g2y - g1y)

# # solution
# sum([g_dist(p) for p in g_combs])
