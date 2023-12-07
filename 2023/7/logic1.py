#A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2

from collections import defaultdict
import math

def readhands(raw_hand):
    hands = {}
    ranks = 0
    with open(raw_hand, 'r') as f:
        for line in f:
            line=line.split()
            hands[line[0]] = line[1]
            ranks +=1
    return hands, ranks
'''
Five of a kind, where all five cards have the same label: AAAAA
Four of a kind, where four cards have the same label and one card has a different label: AA8AA
Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
High card, where all cards' labels are distinct: 23456
''' 
HandTypes_to_Score = {'5':     6,
                      '41':    5,
                      '32':    4,
                      '311':   3,
                      '221':   2,
                      '2111':  1,
                      '11111': 0
}    


Upgrade_Mapping = {0:1,
                   1:3,
                   2:4,
                   3:5,
                   4:5,
                   5:6,
                   6:6
}

def get_hand_type(hand_data):
    result = defaultdict(int)
    for char in hand_data:
        result[char]+=1
    result_values = list(map(str, list(result.values())))
    result_values.sort(reverse=True)
    type_code = ('').join(result_values)
    return (type_code, HandTypes_to_Score[type_code])

CardValue = {'A':12 ,
             'K':11 ,
             'Q':10 ,
             'J':-1  ,
             'T':8  ,
             '9':7  ,
             '8':6  ,
             '7':5  ,
             '6':4  ,
             '5':3  ,
             '4':2  ,
             '3':1  ,
             '2':0
             }

def hand_sort(e):
  values = [1000000000000,1000000000,1000000,1000,1]
  hand_value = 0
  for i in range(5):
      hand_value += values[i]*CardValue[e[i]]
      
  return hand_value

def sort_hands_internally(hands):
    hands.sort(key=hand_sort)
    return hands

def calc(raw_hand):
    input, highest_rank = readhands(raw_hand)
    print('input',input)
    print('highest_rank',highest_rank)

    hands_by_rank = defaultdict(list)
    for hands_data in input.keys():
        hand_type = get_hand_type(hands_data)

        hand_group = hand_type[1]
        if 'J' in hands_data:
            if (hand_group==1 and hands_data.count('J')==2):
                hand_group = 3
            elif (hand_group==3 and hands_data.count('J')==3):
                hand_group = 5
            else: 
                for i in range(hands_data.count('J')):
                    hand_group = Upgrade_Mapping[hand_group]

        hands_by_rank[hand_group].append(hands_data)
        print(hands_data, hand_type)
    #print('hands_by_rank',hands_by_rank)

    current_rank = 1
    winnings = 0
    for i in range(0,6+1):
        if i in hands_by_rank:
            hands = hands_by_rank[i]
            sorted_hands = sort_hands_internally(hands)
            print('sorted_hands', sorted_hands)
            for hand in sorted_hands:
                print('Current Test', hand, current_rank, input[hand])
                winnings += current_rank * int(input[hand])
                current_rank +=1
    print(winnings)

    '''
    250680646
    '''