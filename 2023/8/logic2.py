from collections import defaultdict
import math

def get_next_instuction(instructions):
    try:
        next_instruction =  instructions[get_next_instuction.current_instuction_location]
    except:
        get_next_instuction.current_instuction_location = 0
        next_instruction =  instructions[get_next_instuction.current_instuction_location]

    get_next_instuction.current_instuction_location +=1
    return next_instruction

get_next_instuction.current_instuction_location = 0


def read_maps(maps):
    mapping={}
    with open(maps, 'r') as f:
        file_lines = f.readlines()
        instructions = file_lines[0].strip()
        for line in file_lines[2:]:
            code, next_code = line.split('=')
            L,R = next_code.strip(' (').strip(')\n').split(',')
            mapping[code.strip()] = {'L':L.strip(),'R':R.strip()}
    return mapping, instructions

def count_steps(mapping, instructions, starting_point):
    steps = 0
    current_step = starting_point
    while current_step[2] != 'Z':
        direction = get_next_instuction(instructions)
        current_step = mapping[current_step][direction]
        steps += 1
    return steps

def get_all_starting_points(mapping):
    starting_points = []
    for key in mapping.keys():
        if key[2]=='A':
            starting_points.append(key)
    return starting_points

def rout(maps):
    mapping, instructions = read_maps(maps)
    starting_points = get_all_starting_points(mapping)
    results = []
    for starting_point in starting_points:
        result = count_steps(mapping, instructions, starting_point)
        results.append(result)
    print(results)
    lcm = math.lcm(*results)
    print(lcm)