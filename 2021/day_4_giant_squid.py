import os, sys
path = os.path.dirname(os.path.realpath(__file__)) 
with open(path + '/day_4_input.txt', 'r') as text_file: 

    data = text_file.read().splitlines() 


# data = [
# "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
# "",
# "22 13 17 11  0",
# " 8  2 23  4 24",
# "21  9 14 16  7",
# " 6 10  3 18  5",
# " 1 12 20 15 19",
# "",
# " 3 15  0  2 22",
# " 9 18 13 17  5",
# "19  8  7 25 23",
# "20 11 10 24  4",
# "14 21 16 12  6",
# "",
# "14 21 17 24  4",
# "10 16 15  9 19",
# "18  8 23 26 20",
# "22 11 13  6  5",
# " 2  0 12  3  7",
# ]

data.append("") ### cheap hack

numbers_to_draw = list(map(int, data[0].split(",")))
boards = []
new_board = []
for row in data[1:]:
    if len(row) == 0: ### if we are at an empty line
        if new_board: ### and the board is filled with rows, append it
            new_board = [list(map(int ,row.split())) for row in new_board] 

            for i in range(len(new_board[0])):
                new_board_vertical = [row[i] for row in new_board[:5]]
                new_board.append(new_board_vertical)

            boards.append(new_board)

        new_board = [] ## 
    else:
        new_board.append(row)

for board in boards:
    print ("board:")
    print (board)

print (numbers_to_draw)


def part1():
    numbers_drawn = []
    for number in numbers_to_draw:
        numbers_drawn.append(number)

        for board in boards:
            for row_or_column in board:
                if all([False for number in row_or_column if number not in numbers_drawn]):

                    unmarked_numbers = []
                    for row_or_column in board[:5]:
                        unmarked_numbers += [number for number in row_or_column if number not in numbers_drawn]
                    print ("Part 1 solution: ")
                    print (sum(unmarked_numbers)*number)
                    return
part1()


def part2():
    numbers_drawn = []
    winning_boards = []
    for number in numbers_to_draw:
        numbers_drawn.append(number)

        for board in boards:
            if board not in winning_boards:
                for row_or_column in board:
                    if all([False for number in row_or_column if number not in numbers_drawn]):
                        winning_boards.append(board)

                        unmarked_numbers = []
                        for row_or_column in board[:5]:
                            unmarked_numbers += [number for number in row_or_column if number not in numbers_drawn]
                        print ("Part 2 solution: ")
                        print (sum(unmarked_numbers)*number)
part2()