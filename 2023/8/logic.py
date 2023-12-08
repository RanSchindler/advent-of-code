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

def count_steps(mapping, instructions):
    steps = 0
    current_step = 'AAA'
    while current_step != 'ZZZ':
        direction = get_next_instuction(instructions)
        current_step = mapping[current_step][direction]
        steps += 1
    print(steps)



def rout(maps):
    mapping, instructions = read_maps(maps)
    print('mapping:',mapping)
    print('instructions: ', instructions)
    result = count_steps(mapping, instructions)


