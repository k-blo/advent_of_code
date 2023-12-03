
import re
from collections import defaultdict
from itertools import product
from numpy import prod

import os, sys
path = os.path.dirname(os.path.realpath(__file__)) 
with open(path + '/day_3_input.txt', 'r') as text_file: 
    DATA = text_file.read().splitlines()


EXAMPLE = [
"467..114..",
"...*......",
"..35..633.",
"......#...",
"617*......",
".....+.58.",
"..592.....",
"......755.",
"...$.*....",
".664.598..",
]



class Coords():
    def __init__(self, input: list):
        self.arr = input
    

    def get_char(self, x,y, with_coordinates=False):
        if with_coordinates:
            return self.arr[y][x], x, y
        else:
            return self.arr[y][x]


    def surrounding_characters(self, x,y):
        return [self.get_char(x1,y1) for x1,y1 in self._get_adjacent_coords(x,y)]

    def surrounding_characters_with_coords(self, x,y):
        return [self.get_char(x1,y1, with_coordinates=True) for x1,y1 in self._get_adjacent_coords(x,y)]
        

    def _get_adjacent_coords(self, x,y):
        CARTESIAN_PRODUCT = list(product([0, 1, -1], [1, -1, 0]))
        SURROUNDING_COORDS = CARTESIAN_PRODUCT
        SURROUNDING_COORDS.remove((0,0))
        xmax=len(self.arr[0])
        ymax=len(self.arr)
        return [(xd + x, yd + y) for xd, yd in SURROUNDING_COORDS
                if not -1 in [xd + x, yd + y]
                and xd + x < xmax
                and yd + y < ymax]


def part_1(input):
    schematic = Coords(input)
    valid_numbers = []

    for y, line in enumerate(input):
        # also catches repeated occurrences
        for number_re in re.finditer(r'\d+', line):

            number = number_re.group(0)
            x = number_re.start()
            
            adjacent_chars = sum([schematic.surrounding_characters(x+x_offset, y) for x_offset, digit in enumerate(number)],[])
            adjacent_chars_stripped = [ char for char in adjacent_chars if not (char.isnumeric() or char == ".") ]
            valid_numbers += [int(number)] if len(adjacent_chars_stripped) > 0 else []

    return sum(valid_numbers)

    
def part_2(input):
    schematic = Coords(input)
    gears = defaultdict(list)

    for y, line in enumerate(input):
        # also catches repeated occurrences
        for number_re in re.finditer(r'\d+', line):

            number = number_re.group(0)
            x = number_re.start()
            
            adjacent_chars_with_coords = sum([schematic.surrounding_characters_with_coords(x+x_offset, y) for x_offset, digit in enumerate(number)],[])
            adjacent_chars_stripped = [ char for char in adjacent_chars_with_coords if "*" in char ]

            for gear in adjacent_chars_stripped:
                gears[gear] += [int(number)] if int(number) not in gears[gear] else []

    return sum(prod(numbers) for numbers in gears.values() if len(numbers) == 2)


print(f"EXAMPLE 1: {part_1(EXAMPLE)}")
print(f"PART 1: {part_1(DATA)}")


print(f"EXAMPLE 2: {part_2(EXAMPLE)}")
print(f"PART 2: {part_2(DATA)}")