import re
import os, sys
path = os.path.dirname(os.path.realpath(__file__)) 
with open(path + '/day_1_input', 'r') as text_file: 
    DATA = text_file.read().splitlines() 

EXAMPLE = [
"3   4",
"4   3",
"2   5",
"1   3",
"3   9",
"3   3",
]


def parse_nums(data):
    return [tuple(int(num) for num in number_pair.split()) for number_pair in data]
    
print(parse_nums(EXAMPLE))

def part_1(data):
    num_pairs = parse_nums(data)
    row1 = sorted([first for first, _ in num_pairs])
    row2 = sorted([second for _, second in num_pairs])
    return sum([abs(a - b) for a, b in zip(row1, row2)])
    

print(part_1(EXAMPLE))
print(part_1(DATA))


def part_2(data):
    num_pairs = parse_nums(data)
    row1 = [first for first, _ in num_pairs]
    row2 = [second for _, second in num_pairs]
    return sum([row2.count(first)*first for first in row1])


print(part_2(EXAMPLE))
print(part_2(DATA))