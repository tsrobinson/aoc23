import re
def s2d(source, mapper):
    destination = None
    i = 0
    while destination is None:
        if i >= len(mapper):
            destination = source
        elif mapper[i][1] <= source <= mapper[i][1] + mapper[i][2]-1:
            destination = mapper[i][0] + source-mapper[i][1]
        else:
            i += 1
    return destination

input = [re.sub('\n','',x) for x in open('input.txt').readlines()]
seeds = [int(x) for x in re.sub('seeds: ','',input[0]).split()]

maps = {}
i = 2
while i < len(input):
    if re.search('\A[a-zA-Z]',input[i]) is not None:
        map_name = input[i][:-5]
        i += 1
        map_list = []
    while i < len(input) and input[i] != '':
        map_list.append([int(x) for x in input[i].split()])
        i += 1
    maps[map_name] = map_list
    i += 1

def solution(seeds):
    locs = []
    for seed in seeds:
        soil_id = s2d(seed, maps['seed-to-soil'])
        fert_id = s2d(soil_id, maps['soil-to-fertilizer'])
        water_id = s2d(fert_id, maps['fertilizer-to-water'])
        light_id = s2d(water_id, maps['water-to-light'])
        temp_id = s2d(light_id, maps['light-to-temperature'])
        humid_id = s2d(temp_id, maps['temperature-to-humidity'])
        loc_id = s2d(humid_id, maps['humidity-to-location'])

        locs.append(loc_id)

    return min(locs)   

# PART 1
solution(seeds)

# PART 2

