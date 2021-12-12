






def part1():
    spoken_words = [18, 11, 9, 0,5,1]
    spoken_words = [0,3,6]
    for i in range(2020-len(spoken_words)):
        last_number = spoken_words[-1]
        if spoken_words.count(last_number) == 1:
            spoken_words.append(0)
        else:
            last_turn_spoken = list(reversed(spoken_words[:-1])).index(last_number)+1
            spoken_words.append(last_turn_spoken)     

    print (spoken_words[-1])            


part1()

from collections import defaultdict
def part2():
    number_counter = defaultdict(int)
    turn_counter = defaultdict(list)
    starting_words = [18, 11, 9, 0,5,1]#[0,3,6]
    for turn, i in enumerate(starting_words):
        number_counter[i] += 1
        turn_counter[i].append( turn+1 )
    previous_number = starting_words[-1]

    for turn in range(len(starting_words)+1, 30000000+1):
        previous_number = (0 if number_counter[previous_number] == 1
                            else turn_counter[previous_number][-1] - turn_counter[previous_number][-2])

        number_counter[previous_number] += 1
        turn_counter[previous_number].append(turn)


        if turn % 1000 == 0:
            print (turn)

    print (previous_number)

part2()




# from collections import defaultdict
# def part_1(data):
#     return play(list(map(int, data.split(","))), 2020)

# def part_2(data):
#     # Takes a few seconds, but fast enough not to bother optimising
#     return play(list(map(int, data.split(","))), 30000000)


# def play(starting, iterations):
#     numbers = defaultdict(lambda: (None, None),
#                           {n: (None, i) for i, n in enumerate(starting)})
#     previous = starting[-1]

#     for i in range(len(numbers), iterations):
#         current = (0 if numbers[previous][0] is None
#                    else numbers[previous][1] - numbers[previous][0])
#         numbers[current] = (numbers[current][1], i)
#         previous = current

#     return previous


# if __name__ == '__main__':
#     inp = "18, 11, 9, 0,5,1"
#     print("Part 1 answer: " + str(part_1(inp)))
#     print("Part 2 answer: " + str(part_2(inp)))