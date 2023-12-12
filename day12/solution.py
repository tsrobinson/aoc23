import re

records = [re.sub('\n', '', x) for x in open('input.txt').readlines()]
spring_map = [re.findall('.+(?=\s)',x)[0]+'.' for x in records]
group_map = [list(map(int, re.findall('(?<=\s).+',x)[0].split(','))) for x in records]


# The following is a lightly adapted version from:
# github.com/vanam/CodeUnveiled/Advent%20of%20Code%202023
# I simply replaced some variable names and added my own interp. of the conditionals 
def spring_placer(idx, g, smap, gmap):
    # start with assessing whether we still need to assign springs to groups
    # i.e. the group we are considering is outside the group_map
    if g >= len(gmap):
        # if we haven't got to the end of the spring map but there are still more springs
        # + we know already we've assigned all the group springs
        if idx < len(smap) and '#' in smap[idx:]:
            return 0
        else:
            # i.e. we've done all groups and there are no more springs, so we have a complete map!
            return 1 
    
    # One other terminal case is where we still have more groups to complete but we're already 
    #   at the end of the map:
    if idx >= len(smap):
        return 0

    # Now move to case where we can assign **groups** of springs
    # This is one of the key bits I think I missed: we want to look group by group rather than spring by spring
    res = None # store for recursion
    g_size = gmap[g]
    
    if smap[idx] == "?":
        # we can start entire group here AND we're not running into any existing springs at the end:
        # the other clever thing here is that it subsumes any existing # into the check implicitly
        if '.' not in smap[idx:idx+g_size] and smap[idx+g_size] != "#": # the second condition checks if our group would be >= 1 spring too long
            # If true, it's still possible we could start the group one step later! Hence we place the entire group NOW + move on
            # PLUS we also move one step further forward and see if we can place the current group there as well
            res = spring_placer(idx + g_size + 1, g + 1, smap, gmap) + spring_placer(idx + 1, g, smap, gmap)
        else:
            # we can't place the group so move to next step
            res = spring_placer(idx + 1, g, smap, gmap)
    elif smap[idx] == "#":
        if '.' not in smap[idx:idx + g_size] and smap[idx+g_size] != "#":
            res = spring_placer(idx + g_size + 1, g + 1, smap, gmap)
        else:
            # we have at least one spring, but cannot complete the group
            res = 0 
    elif smap[idx] == ".":
        res = spring_placer(idx + 1, g, smap, gmap) # it's a forced empty, group not resolved, so move to next step
    
    return res

# solution
sum([spring_placer(0,0, spring_map[i], group_map[i]) for i in range(len(spring_map))])


# PART 2
# So again, used CodeUnveiled's solution to learn about and understand MEMOISATION
# The key principle here is, given the recursion, you may have different function calls hitting the same spot. 
# So with a super long string to check, recalculating these steps is wasteful (and will take too long)
# So we just create a dictionary MEMO that stores previous function call results *within* the same spring map 
# (i.e. not across lines of the input)

# Adapt the input data
# The key!

MEMO = {}

# The same function, but after checking terminal cases, we check if we have prestored the results
def spring_placer2(idx, g, smap, gmap):
    if g >= len(gmap):
        if idx < len(smap) and "#" in smap[idx:]:
            return 0
        else:
            return 1
        
    if idx >= len(smap):
        return 0
    
    if (idx, g) in MEMO: return MEMO[(idx, g)]

    res = None
    gs = gmap[g]

    if smap[idx] == "?":
        if '.' not in smap[idx:idx+gs] and smap[idx + gs] != "#":
            res = spring_placer2(idx + gs+ 1, g + 1, smap, gmap) + spring_placer2(idx + 1, g, smap, gmap)
        else:
            res = spring_placer2(idx + 1, g, smap, gmap)
    elif smap[idx] == "#":
        if '.' not in smap[idx:idx + gs] and smap[idx + gs] != "#":
            res = spring_placer2(idx + gs+ 1, g + 1, smap, gmap)
        else:
            res = 0
    elif smap[idx] == ".":
        res = spring_placer2(idx + 1, g, smap, gmap)

    MEMO[(idx, g)] = res
    return res

max_combs = []
for i in range(len(records)):

    spring_map2, group_map2 = records[i].split()
    spring_map2 = "?".join([spring_map2] * 5)
    spring_map2 = spring_map2 + '.'

    group_map2 = group_map[i]*5
    MEMO = {}
    max_combs.append(spring_placer2(0,0,spring_map2, group_map2))

# solution
sum(max_combs)
