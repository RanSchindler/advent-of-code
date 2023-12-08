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

def get_next_node(mapping, node, direction):
    next_node = mapping[node][direction]
    return next_node

def get_all_starting_points(mapping):
    starting_points = []
    for key in mapping.keys():
        if key[2]=='A':
            starting_points.append(key)
    return starting_points

def amount_of_z(all_next_nodes):
    amount_z = 0
    for node in all_next_nodes:
        if node[2]=='Z':
            amount_z +=1
    return amount_z

def rout(maps):
    mapping, instructions = read_maps(maps)
    print('mapping:',mapping)
    print('instructions: ', instructions)
    starting_points = get_all_starting_points(mapping)
    starting_point_amount = len(starting_points)
    print('starting_point_amount: ', starting_point_amount)
    steps = 0
    node_end_w_z = 0
    nodes_to_scan = starting_points
    while node_end_w_z != starting_point_amount:
        if steps % 10000000 == 0:
            print(steps)
        direction = get_next_instuction(instructions)
        all_next_nodes = []
        for node in nodes_to_scan:
            next_node = get_next_node(mapping, node, direction)
            all_next_nodes.append(next_node)
        steps += 1
        node_end_w_z = amount_of_z(all_next_nodes)
        nodes_to_scan = all_next_nodes
    print(steps)