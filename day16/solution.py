import re
import sys

# won't work on input without increasing limit
sys.setrecursionlimit(20000)

# maps for obstacles and record of light path
mmap = [[c for c in x.rstrip('\n')] for x in open('input.txt').readlines()]
lmap = [[0]*len(x) for x in mmap]

# convenience function to detect map edges
def out_of_bounds(x,y):
    if x < 0 or y < 0:
        return True
    elif y >= len(mmap[0]) or x >= len(mmap):
        return True
    return False

# hashmap to store (tile, direction)
MEMO = {}

def move(curr, d):
    cx,cy = curr
    
    if out_of_bounds(cx, cy):
        return None
    
    if (cx, cy, d) in MEMO:
        return None
    else:
        MEMO[(cx, cy, d)] = True
    
    lmap[cy][cx] = 1
    
    # please ignore how horrid this looks
    if mmap[cy][cx] == ".":
        if d == "l":
            nx = cx + 1
        elif d == "r":
            nx = cx - 1
        else:
            nx = cx
        if d == "t":
            ny = cy + 1
        elif d == "b":
            ny = cy - 1
        else:
            ny = cy
        move((nx,ny), d)
    elif mmap[cy][cx] == "|":
        if d in 'lr':
            move((cx,cy-1),'b')
            move((cx,cy+1), 't')
        elif d == 't':
            move((cx, cy+1),d)
        elif d == 'b':
            move((cx, cy-1),d)
    elif mmap[cy][cx] == "-":
        if d in 'tb':
            move((cx+1,cy),'l')
            move((cx-1,cy), 'r')
        elif d == 'l':
            move((cx+1, cy),d)
        elif d == 'r':
            move((cx-1, cy),d)
    elif mmap[cy][cx] == '\\':
        if d == 'l':
            move((cx,cy+1),'t')
        elif d == 'r':
            move((cx,cy-1),'b')
        elif d == 't':
            move((cx+1,cy),'l')
        elif d == 'b':
            move((cx-1,cy),'r')
    elif mmap[cy][cx] == '/':
        if d == 'l':
            move((cx,cy-1),'b')
        elif d == 'r':
            move((cx,cy+1),'t')
        elif d == 't':
            move((cx-1,cy),'r')
        elif d == 'b':
            move((cx+1,cy),'l')

    return None

# start moving
move([0,0],'l')

# solution
sum([sum(x) for x in lmap])