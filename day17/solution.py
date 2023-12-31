from math import inf
from heapq import heappop, heappush
from collections import defaultdict

# map of heatloss
hmap = list(list(map(int, line.rstrip('\n'))) for line in open('input.txt').readlines())
# dijkstra map to update
dmap = defaultdict(lambda: float('infinity'))
tx = len(hmap[0]) - 1
ty = len(hmap) - 1

# create a heap
HEAP = [(0,(0,0),'',0)]

# helper for finding improper neighbours
def bad_neighbour(pnx,pny):
    if pnx < 0 or pnx >= len(hmap[0]):
        return True
    elif pny < 0 or pny >= len(hmap):
        return True
    else:
        return False
    
def is_opposite(cd,nd):
    if (cd,nd) in [('l','r'),('r','l'),('u','d'),('d','u')]:
        return True
    else:
        return False
    
MOVES = {(1,0):'r',(-1,0):'l',(0,1):'d',(0,-1):'u'}

while HEAP:
    cdist, (px,py), pdir, pruns = heappop(HEAP) # get info then remove from heap
    
    if (px, py) == (tx,ty):
        print("Solution: "+str(cdist))
        break
    
    # for every possible move
    for dx, dy in MOVES:
        ndir = MOVES[(dx,dy)] # get direction of move
        
        nruns = pruns + 1 if ndir == pdir else 1
        
        # movement constraints 
        if nruns > 3 or is_opposite(pdir, ndir):
            continue
        
        # get neighbour coordinates
        nx = px + dx
        ny = py + dy
        
        # check doesn't violate board/already visited
        if bad_neighbour(nx,ny):
            continue
        
        # propose new distance
        new_dist = cdist + hmap[ny][nx]
        if new_dist < dmap[((nx,ny), ndir, nruns)]:
            dmap[((nx,ny), ndir, nruns)] = new_dist
            heappush(HEAP, [new_dist, (nx, ny), ndir, nruns])
            
