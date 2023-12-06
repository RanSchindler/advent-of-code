from collections import defaultdict


def check_game(games):
    with open(games, 'r') as f:
        total_score = 0
        for line in f:
            sections = line.split(':')[1].split('|')
            winning_numbers = set(sections[0].split())
            check_numbers = set(sections[1].split())
            print(winning_numbers, check_numbers)
            intersection_size = len(winning_numbers.intersection(check_numbers))
            if intersection_size > 0:
                score = pow(2,(intersection_size-1))
                print(score)
                total_score += score
        print(total_score)


            #Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53


def check_game_1(games):
    with open(games, 'r') as f:
        total_cards = defaultdict(int)
        game_number = 0
        for line in f:
            sections = line.split(':')[1].split('|')
            game_number = int(line.split(':')[0].strip('Card '))
            total_cards[game_number]+=1
            print('total_cards start ', total_cards)
            print(game_number)
            winning_numbers = set(sections[0].split())
            check_numbers = set(sections[1].split())
            #print(winning_numbers, check_numbers)
            intersection_size = len(winning_numbers.intersection(check_numbers))
            if intersection_size > 0:
                print('intersection_size',intersection_size)
                for i in range(game_number+1, game_number+intersection_size+1):
                    total_cards[i]+=total_cards[game_number]
                print(total_cards)
        print(game_number)
        total_cards_count = 0
        for i in range(1,game_number+1):
            total_cards_count+=total_cards[i]
        print(total_cards_count)