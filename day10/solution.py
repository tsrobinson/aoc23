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
while map[nxt[1]][nxt[0]] != "S":
    tmp = move(lst, nxt)
    lst = nxt
    nxt = tmp
    i += 1

# solution
(i+1)//2


