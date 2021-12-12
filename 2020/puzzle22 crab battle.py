from collections import defaultdict
import os, sys
path = os.path.dirname(os.path.realpath(__file__)) 
with open(path + '/day_22_input.txt', 'r') as text_file: 

    data = text_file.read().splitlines()



# data = [
# "Player 1:",
# "9",
# "2",
# "6",
# "3",
# "1",
# "",
# "Player 2:",
# "5",
# "8",
# "4",
# "7",
# "10",
# ]

# more readable
# if player1[0] > player2[0]:
#     wins_loses(player1, player2)
# else:
#     wins_loses(player2, player1)



half = data.index("")
player1 = [int(i) for i in data[1:half]]
player2 = [int(i) for i in data[half+2:]]


def wins_loses(p1, p2):
    lost_card = p2.pop(0)
    win_card = p1.pop(0)
    p1 += [win_card, lost_card]

def play_standard_rules(players):
    while not 0 in [len(player1), len(player2)]:
        players.sort(key=lambda y: y[0])
        wins_loses(players[::-1][0], players[::-1][1])

def part1():
    players = [player1, player2]
    play_standard_rules(players)
    winner = [p for p in players if not len(p) == 0][0]
    winning_score = sum([i*card for i, card in enumerate(winner[::-1], 1)])

    print ("PART 1: " + str(winning_score))

part1()


from collections import defaultdict

def wins_loses2(players, custom=False):
    winner, loser = "p1", "p2"
    if players["p1"][0] < players["p2"][0]:
        winner, loser = "p2", "p1"
    if custom:
        winner, loser = custom["winner"], custom["loser"]

    lost_card = players[loser].pop(0)
    win_card = players[winner].pop(0)
    players[winner] += [win_card, lost_card]
    return players


def part2(players, universe=0):
    remember_rounds = set() ## sets are extremely faster for the purpose of checking if item is contained!!
    winner_game = None

    while winner_game == None:
        ####### to break recursion
        this_round = ( tuple(players["p1"]), tuple(players["p2"]) )
        if this_round in remember_rounds:
            winner_game = "p1"
        remember_rounds.add(this_round)

        ##### one player regularly wins the (sub)game
        if [] in players.values():
            winner_game = "p1"
            if players["p1"] == []:
                winner_game = "p2"
        
        ##### special recursion rules: creates a subgame
        elif len(players["p1"])-1 >= players["p1"][0] and len(players["p2"])-1 >= players["p2"][0]:
            p1max, p2max = players["p1"][0]+1, players["p2"][0]+1
            subgame = {"p1": list(players["p1"][1:p1max]), 
                       "p2": list(players["p2"][1:p2max])}

            winner = part2(subgame, universe+1)
            loser = [p for p in ["p1", "p2"] if p != winner] [0]
            players = wins_loses2(players, {"winner": winner, "loser":loser})

        ##### the game proceeds normally
        else:
            players = wins_loses2(players)

    ##### the outermost recursion layer. this ends all games and the function
    if universe == 0:
        winner = [p for p in players.values() if not len(p) == 0][0]
        winning_score = sum([i*card for i, card in enumerate(winner[::-1], 1)])
        print ("PART 2: " + str(winning_score))

    #### returning the winner from a subgame recursion
    else:
        return winner_game



half = data.index("")
decks = {"p1": [int(i) for i in data[1:half]], "p2": [int(i) for i in data[half+2:]]}
part2(decks)


# https://adventofcode.com/2020/day/22


# from collections import deque
# from itertools import islice
# from copy import deepcopy


# def parse_input(input_txt):
#     decks = []
#     for deck in input_txt.split("\n\n"):
#         deck = [int(card) for card in deck.splitlines()[1:]]
#         decks.append(deque(deck))
#     decks = tuple(decks)
#     return decks


# def calculate_score(cards):
#     return sum(i * v for i, v in enumerate(reversed(cards), start=1))


# def part_1(decks):
#     decks = deepcopy(decks)
#     while True:
#         p0 = decks[0].popleft()
#         p1 = decks[1].popleft()
#         if p0 > p1:
#             decks[0].extend((p0, p1))
#             if len(decks[1]) == 0:
#                 return calculate_score(decks[0])
#         else:
#             decks[1].extend((p1, p0))
#             if len(decks[0]) == 0:
#                 return calculate_score(decks[1])


# def part_2(decks, return_index=False):
#     cache = set()
#     winner_game = None
#     while winner_game is None:
#         d = (tuple(decks[0]), tuple(decks[1]))
#         if d in cache:
#             winner_game = 0  # player 1 (= index 0) wins
#             break
#         cache.add(d)
#         p0 = decks[0].popleft()
#         p1 = decks[1].popleft()
#         if p0 <= len(decks[0]) and p1 <= len(decks[1]):
#             winner_round = part_2(
#                 (deque(islice(decks[0], 0, p0)),
#                  deque(islice(decks[1], 0, p1))),
#                 True
#             )
#         elif p0 > p1:
#             winner_round = 0
#         else:
#             winner_round = 1
#         if winner_round == 0:
#             decks[0].extend((p0, p1))
#             if len(decks[1]) == 0:
#                 winner_game = 0
#         else:
#             decks[1].extend((p1, p0))
#             if len(decks[0]) == 0:
#                 winner_game = 1

#     if return_index:
#         return winner_game
#     else:
#         print (decks)
#         return calculate_score(decks[winner_game])




# with open(path + '/day_22_input.txt', 'r') as file:
#     challenge_decks = parse_input(file.read())
# print(part_1(challenge_decks))  # 30138
# print(part_2(challenge_decks))  # 31587