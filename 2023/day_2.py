import re
from collections import defaultdict
import numpy
import os, sys
path = os.path.dirname(os.path.realpath(__file__)) 
with open(path + '/day_2_input.txt', 'r') as text_file: 
    DATA = text_file.read().splitlines()


EXAMPLE = [
"Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
"Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
"Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
"Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]



LIMIT = {"red": 12, "green": 13, "blue": 14}

def part_1(input):
    global game_data
    game_data = defaultdict(list)
    for line in input:
        _parse_results(line)

    return sum(id for id, game in game_data.items() if _test_game_possible(game))

def _parse_results(game: str):
    id = int(game.split(":")[0].split("Game ")[1])
    sets = game.split(":")[1].split("; ")

    for set in sets:
        nums = re.findall(r'\d+ ', set)
        colors = (re.sub(r'\d+', "", set)).split(", ")
        set_data = {cube_color.strip():int(nums[i]) for i, cube_color in enumerate(colors)}
        game_data[id].append(set_data)


def _test_game_possible(game: list):
    for set in game:
        for color, num in set.items():
            if LIMIT[color] < num:
                return False
    return True


def part_2(input):
    return sum(_count_min_cubes(game) for game in game_data.values())


def _count_min_cubes(game: list):
    minimum_cubes = {}
    for set in game:
        for color, num in set.items():
            if minimum_cubes.get(color,0) < num:
                minimum_cubes[color] = num
    return numpy.prod(list(minimum_cubes.values()))


print(f"part 1: {part_1(EXAMPLE)}")
print(f"part 2: {part_2(EXAMPLE)}")

print(f"part 1: {part_1(DATA)}")
print(f"part 2: {part_2(DATA)}")
