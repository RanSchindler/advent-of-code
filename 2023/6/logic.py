from collections import defaultdict
import math

def calc(races):
    with open(races, 'r') as f:
        file_lines = [line.strip() for line in f.readlines()]
        times = file_lines[0].split()[1:]
        distance = file_lines[1].split()[1:]
        print(times)
        print(distance)
        resuls = 1
        for race_time, race_distance in zip(times, distance):
            a = -1
            b = int(race_time)
            c = -1*int(race_distance)

            adjust = 0

            #print('a: ',a,' b: ',b,' c: ',c)
            first_solution = (-1*b + math.sqrt(math.pow(b,2) - 4*a*c))/2*a
            second_solution = (-1*b - math.sqrt(math.pow(b,2) - 4*a*c))/2*a

            #print('solutions: ', first_solution, second_solution)

            min_solution = min(first_solution, second_solution)
            max_solution = max(second_solution, second_solution)

            min_solution_ceil = math.ceil(min_solution)
            max_solution_floor = math.floor(max_solution)

            if min_solution_ceil == min_solution:
                adjust +=1
            if max_solution_floor == max_solution:
                adjust +=1

            #print('min_solution',min_solution)
            #print('max_solution',max_solution)

            amount_of_solutions = (max_solution_floor - min_solution_ceil + 1) - adjust
            print('amount_of_solutions',amount_of_solutions)
            resuls *= amount_of_solutions
        print(resuls)




