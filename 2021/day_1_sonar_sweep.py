import os, sys
path = os.path.dirname(os.path.realpath(__file__)) 
with open(path + '/day_1_input.txt', 'r') as text_file: 

    data = text_file.read().splitlines() 



# data = [
# 199,
# 200,
# 208,
# 210,
# 200,
# 207,
# 240,
# 269,
# 260,
# 263,
# ]
data = [int(i) for i in data]
data = list(map(int, data))

def part_1():
    previous_depth = None
    differences = []
    for depth in data:
        if previous_depth:
            differences += [depth - previous_depth]
        previous_depth = depth

    print ("Part 1 solution: ")
    print(len([d for d in differences if d > 0]))

part_1()


def part_2():
    previous_depth = None
    differences = []
    for count, depth in enumerate(data):

        if count + 3 < len(data):

            this_window = depth + data[count+1] + data[count+2]
            next_window = data[count+1] + data[count+2] + data[count+3]
            differences += [next_window - this_window]

    print ("Part 2 solution: ")
    print(len([d for d in differences if d > 0]))

part_2()