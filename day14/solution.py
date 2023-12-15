import re
import numpy as np

with open('input.txt') as file:
    platform = file.readlines()
platform = np.stack([list(x.rstrip("\n")) for x in platform], axis = 0)

def tilt_north(p):
    p = np.concatenate( # add a buffer row at top so always starts with #
        [
            np.array(['#']*len(p[0])).reshape(1, len(p[0])), 
            p
        ], axis = 0
    )
    rows, cols = p.shape
    for c in range(cols):
        for r in range(2, rows): # we know anything in first (platform) row stays put
            if p[r,c] == 'O':
                # count how many empty spaces before a blocking piece
                shift = len(re.findall('(?<=[#O])\.*$', ''.join(p[:r,c]))[0]) 
                p[r,c] = '.' # swap out empty piece
                p[r-shift,c] = 'O'
    return(p[1:])

tilted = tilt_north(platform)

def load(p):
    return sum([sum(p[i] == 'O')*(p.shape[0]-i) for i in range(p.shape[0])])

# solution
load(tilted)

## PART 2
def spin(p):
    for _ in range(4):
        p = tilt_north(p)
        p = np.rot90(p, k = 3)
    return p

def part_2(p):
    SPIN_MEMO = {}
    cycle = 0
    while ''.join(p.flatten()) not in SPIN_MEMO:
        SPIN_MEMO[''.join(p.flatten())] = cycle
        p = spin(p)
        cycle += 1
    
    print(cycle) 
    
    chkpt = SPIN_MEMO[''.join(p.flatten())]
    cycle_len = max(SPIN_MEMO.values()) + 1 - chkpt
    
    for _ in range((1_000_000_000 - chkpt)%cycle_len):
        p = spin(p)
    
    return load(p)
        
part_2(platform)