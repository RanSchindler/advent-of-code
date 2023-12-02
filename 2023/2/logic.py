import re
from functools import reduce

def color_gamr_1(games_sets):
    top_color = {'red': 12, 'green': 13, 'blue': 14}
    with open(games_sets, 'r') as f:
        winning_games = []
        min_colors_per_games_power = []
        for line in f:
            line = line.lstrip('Game ')
            games_raw_sets = line.split(':')
            game_number = games_raw_sets[0]
            games_turns_raw_cleaned = games_raw_sets[1].rstrip('\n').strip()
            games_turns_split = games_turns_raw_cleaned.split(';')
            winning_turn = True
            max_extracted_cubes = {}
            for game_turn in games_turns_split:
                extracted_cubes = game_turn.split(',')
                extracted_cubes_numbers = {}
                for cube in extracted_cubes:
                    for k,v in top_color.items():
                        if k in cube:
                            color_amount = int(cube.rstrip(' ' + k))
                            extracted_cubes_numbers[k] = color_amount
                            ##
                            if color_amount > top_color[k]:
                                winning_turn = False
                            ##
                for k,v in extracted_cubes_numbers.items():
                    if k not in max_extracted_cubes:
                        max_extracted_cubes[k] = v
                    else:
                        max_extracted_cubes[k] = max(max_extracted_cubes[k],v)
            if winning_turn:
                winning_games.append(int(game_number))
            min_colors_per_games_power.append(reduce(lambda x, y: x*y, max_extracted_cubes.values()))

        print('-Q1-')
        print(winning_games)
        print(sum(winning_games))
        print('-Q2-')
        print(min_colors_per_games_power)
        print(sum(min_colors_per_games_power))



if __name__ == "__main__":
    pass