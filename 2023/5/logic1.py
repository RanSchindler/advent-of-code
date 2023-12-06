from collections import defaultdict

 

MAPS = {
    'seed-to-soil':[],
    'soil-to-fertilizer': [],
    'fertilizer-to-water': [],
    'water-to-light': [],
    'light-to-temperature': [],
    'temperature-to-humidity': [],
    'humidity-to-location': [],
}

def calc_mapping(mapping_maps, value):
    for mapping in mapping_maps:
        range_start = mapping[0]
        range_end = mapping[1]
        gap = mapping[2]

        if range_start <= value <= range_end:
            return value+gap
    return value

def map_seed_to_location(seed,MAPS):

    soil = calc_mapping(MAPS['seed-to-soil'], seed)
    fertilizer = calc_mapping(MAPS['soil-to-fertilizer'], soil)
    water = calc_mapping(MAPS['fertilizer-to-water'], fertilizer)
    light = calc_mapping(MAPS['water-to-light'], water)
    temperature = calc_mapping(MAPS['light-to-temperature'], light)
    humidity = calc_mapping(MAPS['temperature-to-humidity'], temperature)
    location = calc_mapping(MAPS['humidity-to-location'], humidity)
    return location


def get_relevant_map(MAPS, map_line):
    return MAPS[map_line.split()[0]]

def parse_seed_line(seed_line):
    seeds = seed_line.strip('seeds: ').split()
    return seeds

def update_map(relevant_map, line):
    data = line.split()
    range_start = int(data[1])
    range_end = int(data[1])+int(data[2])-1
    gap = int(data[0])-int(data[1])
    relevant_map.append((range_start, range_end, gap))

def find_closest_location(almanac):
    seeds=[]
    with open(almanac, 'r') as f:
        file_lines = [line.strip() for line in f.readlines()]
        index = 0
        while index < len(file_lines):
            if 'seeds' in file_lines[index]:
                seeds = parse_seed_line(file_lines[index])
                print(seeds)
                index +=1
                continue
            if 'map' in file_lines[index]:
                relevant_map = get_relevant_map(MAPS, file_lines[index])
                index +=1
                while index < len(file_lines) and file_lines[index] != '':
                    update_map(relevant_map, file_lines[index])
                    index +=1
            index +=1

    locations = []
    for seed in seeds:
        seed = int(seed)
        print('seed', int(seed))
        location = map_seed_to_location(seed,MAPS)
        locations.append(location)
    print(locations)
    print(min(locations))

