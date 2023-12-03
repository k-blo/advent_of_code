import os, sys
path = os.path.dirname(os.path.realpath(__file__)) 
with open(path + '/day_x_input.txt', 'r') as text_file: 
    DATA = text_file.read().splitlines()


EXAMPLE = []


def part_1(input):
    pass


def part_2(input):
    pass



print(f"EXAMPLE 1: {part_1(EXAMPLE)}")
print(f"PART 1: {part_1(DATA)}")


print(f"EXAMPLE 2: {part_2(EXAMPLE)}")
print(f"PART 2: {part_2(DATA)}")