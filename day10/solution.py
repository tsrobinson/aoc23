import re
map = [list(re.sub('\n','', x)) for x in open("input.txt").readlines()]

def move(last, tile):

    point = map[tile[1]][tile[0]]
    xchange = tile[0] - last[0]
    ychange = tile[1] - last[1]

    if point == "|":
        return [tile[0], tile[1]+ychange]
    elif point == "-":
        return [tile[0] + xchange, tile[1]]
    elif point == "L":
        if ychange == 1:
            return [tile[0] + 1, tile[1]]
        else:
            return [tile[0], tile[1] - 1]
    elif point == "J":
        if ychange == 1:
            return [tile[0] - 1, tile[1]]
        else:
            return [tile[0], tile[1] - 1]
    elif point == "7":
        if xchange == 1:
            return [tile[0], tile[1] + 1]
        else:
            return [tile[0] - 1, tile[1]]
    elif point == "F":
        if xchange == -1:
            return [tile[0], tile[1] + 1]
        else:
            return [tile[0] + 1, tile[1]]
    else:
        return None

# PART 1
lst = [25,83] # manual instantiation, because ... 
nxt = [24,83]
i = 0
map_path = [lst, nxt]
while map[nxt[1]][nxt[0]] != "S":
    tmp = move(lst, nxt)
    lst = nxt
    nxt = tmp
    map_path.append(nxt)
    i += 1

# solution
(i+1)//2

# PART 2

# I used the solution here for **heavy** inspiration: https://github.com/marcodelmastro/AdventOfCode2023/blob/main/Day10.ipynb
# Recursive flood-fill was too intensive for laptop, so adapted a non-recursive version here: https://playandlearntocode.com/article/flood-fill-algorithm-in-python

import numpy as np
map[83][25] = '7'


def x3(piece):
    if piece == ".":
        return np.array([['.','.','.'],
                  ['.','.','.'],
                  ['.','.','.']])
    elif piece == "F":
        return np.array([['.','.','.'],
                  ['.','#','#'],
                  ['.','#','.']])
    elif piece == "L":
        return np.array([['.','#','.'],
                  ['.','#','#'],
                  ['.','.','.']])
    elif piece == "J":
        return np.array([['.','#','.'],
                  ['#','#','.'],
                  ['.','.','.']])
    elif piece == "7":
        return np.array([['.','.','.'],
                  ['#','#','.'],
                  ['.','#','.']])
    elif piece == "-":
        return np.array([['.','.','.'],
                  ['#','#','#'],
                  ['.','.','.']])
    elif piece == "|":
        return np.array([['.','#','.'],
                  ['.','#','.'],
                  ['.','#','.']])

def make_3x(map):
    new_map = []
    for y in range(len(map)):
        row_tmp = []
        for x in range(len(map[y])):
            if [x,y] not in map_path:
                map[y][x] = "."
            row_tmp.append(x3(map[y][x]))
        new_map.append(np.concatenate(row_tmp, axis = 1))
    return np.concatenate(new_map, axis = 0)

def mprint(map):
    for i in range(map.shape[0]):
        print(''.join(map[i]))
def is_one(map, row, col):
        '''
        Helper method for checking whether the pixel belongs to an island or not
        '''
        if (row < 0 or row > len(map) - 1):
            return False

        if (col < 0 or col > len(map[0]) - 1):
            return False

        if map[row][col] == '.':
            return True
        else:
            return False

def iterative_flood_fill(map, row, col):
    '''
    Iterative version of flood fill algorithm. Works better for larger maps.
    '''
    if (row < 0 or row > len(map) - 1):
        return

    if (col < 0 or col > len(map[0]) - 1):
        return

    if (map[row][col] != '.'):
        return

    q = []  # init empty queue (FIFO)
    map[row][col] = ' '  # mark as visited
    q.append([row, col])  # add to queue

    while len(q) > 0:
        [cur_row, cur_col] = q[0]
        del q[0]

        if (is_one(map, cur_row - 1, cur_col) == True):
            map[cur_row - 1][cur_col] = ' '
            q.append([cur_row - 1, cur_col])

        if (is_one(map, cur_row + 1, cur_col) == True):
            map[cur_row + 1][cur_col] = ' '
            q.append([cur_row + 1, cur_col])

        if (is_one(map, cur_row, cur_col - 1) == True):
            map[cur_row][cur_col - 1] = ' '
            q.append([cur_row, cur_col - 1])

        if (is_one(map, cur_row, cur_col + 1) == True):
            map[cur_row][cur_col + 1] = ' '
            q.append([cur_row, cur_col + 1])

map2 = make_3x(map)
iterative_flood_fill(map2, 0,0)

inside = 0
for i in range(len(map2)):
    for j in range(len(map2[i])):
        inside += 1 if map2[i][j] == "." else 0

map3 = []
for y in range(len(map)):
    row_tmp = []
    for x in range(len(map[0])):
        xe = 3*x+1
        ye = 3*y+1
        row_tmp.append(map2[ye,xe])
    map3.append(row_tmp)

# solution
sum([map3[y][x] == '.' for y in range(len(map)) for x in range(len(map[0]))])

plot_map = []
for y in range(len(map2)):
    row_tmp = []
    for x in range(len(map2[0])):
        row_tmp.append(1 if map2[y,x] == "#" else 0)
    plot_map.append(row_tmp)

# BONUS: SAVE MAP IMAGE
import matplotlib.pyplot as plt 
fig = plt.figure(figsize=(10,10), dpi=300)
plt.gca().set_axis_off()
plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, 
            hspace = 0, wspace = 0)
plt.margins(0,0)
plt.gca().xaxis.set_major_locator(plt.NullLocator())
plt.gca().yaxis.set_major_locator(plt.NullLocator())
plt.imshow(plot_map,cmap="binary")
plt.savefig('../day10_pipe.pdf')