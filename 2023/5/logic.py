from collections import defaultdict

def mirror(x): 
    return x

MAPS = {
    'seed-to-soil':{},
    'soil-to-fertilizer': {},
    'fertilizer-to-water': {},
    'water-to-light': {},
    'light-to-temperature': {},
    'temperature-to-humidity': {},
    'humidity-to-location': {},
}

def map_seed_to_location(seed,MAPS):
    try:
        soil = MAPS['seed-to-soil'][seed]
    except:
        soil = seed
    print('soil', soil)

    try:
        fertilizer = MAPS['soil-to-fertilizer'][soil]
    except:
        fertilizer = soil
    print('fertilizer', fertilizer)

    try:
        water = MAPS['fertilizer-to-water'][fertilizer]
    except:
        water = fertilizer
    print('water', water)

    try:
        light = MAPS['water-to-light'][water]
    except:
        light = water
    print('light', light)

    try:
        temperature = MAPS['light-to-temperature'][light]
    except:
        temperature = light
    print('temperature', temperature)

    try:
        humidity = MAPS['temperature-to-humidity'][temperature]
    except:
        humidity = temperature
    print('humidity', humidity)

    try:
        location = MAPS['humidity-to-location'][humidity]
    except:
        location = humidity
    print('location', location)    

    return location



def get_relevant_map(MAPS, map_line):
    return MAPS[map_line.split()[0]]

def parse_seed_line(seed_line):
    seeds = seed_line.strip('seeds: ').split()
    return seeds

def update_map(relevant_map, line):
    data = line.split()
    for i in range(0,int(data[2])):
        relevant_map[i+int(data[1])] = i+int(data[0])


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

# def check_game(games):
#     with open(games, 'r') as f:
#         total_score = 0
#         for line in f:
#             sections = line.split(':')[1].split('|')
#             winning_numbers = set(sections[0].split())
#             check_numbers = set(sections[1].split())
#             print(winning_numbers, check_numbers)
#             intersection_size = len(winning_numbers.intersection(check_numbers))
#             if intersection_size > 0:
#                 score = pow(2,(intersection_size-1))
#                 print(score)
#                 total_score += score
#         print(total_score)


#             #Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53


# def check_game_1(games):
#     with open(games, 'r') as f:
#         total_cards = defaultdict(int)
#         game_number = 0
#         for line in f:
#             sections = line.split(':')[1].split('|')
#             game_number = int(line.split(':')[0].strip('Card '))
#             total_cards[game_number]+=1
#             print('total_cards start ', total_cards)
#             print(game_number)
#             winning_numbers = set(sections[0].split())
#             check_numbers = set(sections[1].split())
#             #print(winning_numbers, check_numbers)
#             intersection_size = len(winning_numbers.intersection(check_numbers))
#             if intersection_size > 0:
#                 print('intersection_size',intersection_size)
#                 for i in range(game_number+1, game_number+intersection_size+1):
#                     total_cards[i]+=total_cards[game_number]
#                 print(total_cards)
#         print(game_number)
#         total_cards_count = 0
#         for i in range(1,game_number+1):
#             total_cards_count+=total_cards[i]
#         print(total_cards_count)