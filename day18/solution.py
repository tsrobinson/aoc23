import re
import numpy as np

def shoelace(x: list[int],y: list[int]):
    x = np.array(x) 
    y = np.array(y) 
    i= np.arange(len(x))
    area=np.abs(np.sum(x[i-1]*y[i]-x[i]*y[i-1])*0.5) # one line of code for the shoelace formula
    return(area)

instrucs = [
    re.split(
        '\s',re.split('\s(?=\()',x)[0]
        ) for x in open("input.txt").readlines()
    ]

xcoords = [0]
ycoords = [0]

MOVES = {'L':(-1,0),'R':(1,0),'U':(0,-1),'D':(0,1)}

cx,cy = (0,0)
border_length = 0

for d, n in instrucs:
    cx += MOVES[d][0]*int(n)
    cy += MOVES[d][1]*int(n)
    
    border_length += abs(MOVES[d][0]*int(n)) + abs(MOVES[d][1]*int(n))
    
    xcoords.append(cx)
    ycoords.append(cy)
    
int(abs(shoelace(xcoords, ycoords)) - 0.5 * border_length + 1) + border_length

