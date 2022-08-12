

from itertools import cycle, islice, product
import math


def Player(position, score=0):
    return {"position": position, "score": score}


dice_rolls = cycle([i for i in range(1,101)])
Die100 = lambda : sum([next(dice_rolls) for i in range(3)])
Other_player = lambda player : 2 if player == 1 else 1


def Move_Board(from_where, how_far=1):
    game_board = cycle([i for i in range(1, 11)])  # has to be regenerated every time it is used
    return next(islice(game_board, from_where+how_far-1, None))


def Play_Game(position_1, position_2):
    players = { 1: Player(position_1), 2: Player(position_2)}
    count_dice_rolls = 0 

    while True:
        for i in [1,2]:
            die_roll = Die100()
            count_dice_rolls += 3
            players[i]["position"] = Move_Board(players[i]["position"], die_roll)
            players[i]["score"] += players[i]["position"]

            if players[i]["score"] >= 1000:
                return math.prod([players[Other_player(i)]["score"], count_dice_rolls])

print("Part 1:", Play_Game(6,2))



dice_sequences_trip = list(product([1,2,3],[1,2,3],[1,2,3])) 
dice_sequences = [sum(list(dice)) for dice in dice_sequences_trip]
print(dice_sequences)

dice_sequences2 = list(product(dice_sequences_trip, dice_sequences_trip)) 

dice_sequences3 = [sum(list(dice)) for dice in dice_sequences_trip]
track_dict = {}
for i in range(3):
    dice_sequences3 = list(product(dice_sequences3, dice_sequences3)) 
    dice_sequences3 = [sum(list(dice)) for dice in dice_sequences3]
    print("..", len(dice_sequences3))

# print ("..", len([dice for dice in dice_sequences3 if dice >= 21]))
# print(len([dice for dice in dice_sequences3 if dice >= 21])**2)
print(444356092776315 + 341960390180808)

universe_wins = {1:0, 2:0}

def Play_Game_Quantum(position_1, position_2, score1=0, score2=0, player_turn=1):
    players = {
        1: Player(position_1, score1),
        2: Player(position_2, score2),
    }


    for i in [player_turn, Other_player(player_turn)]:
        for roll_sequence in dice_sequences2:

            move = sum(roll_sequence[i-1])
            players[i]["position"] = Move_Board(players[i]["position"], move)
            players[i]["score"] += players[i]["position"]

            if players[i]["score"] >= 21:
                universe_wins[i] += 1
            else:
                Play_Game_Quantum(players[1]["position"], players[2]["position"], players[1]["score"], players[2]["score"], Other_player(i))


Play_Game_Quantum(4,8)
print("Part 2:", universe_wins)


