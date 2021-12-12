

import os, sys
path = os.path.dirname(os.path.realpath(__file__)) 
with open(path + '/day_16_input.txt', 'r') as text_file: 

    data = text_file.read().splitlines()



data = [
".#.",
"..#",
"###"
]


data = [
"##...#.#",
"#..##..#",
"..#.####",
".#..#...",
"########",
"######.#",
".####..#",
".###.#..",
]




space = {} #{(1,1,1): "#"}

for y_coordinate, row in enumerate(data):
    for x_coordinate, cube_state in enumerate(row):
        space[(x_coordinate, y_coordinate, 0)] = cube_state


from collections import defaultdict
from itertools import product


def cycle():
    def neighbours(x,y,z):
        cartesian_product_3d = list(product((-1, 0, 1), repeat=3)) #list(product((-1, 0, 1), (-1, 0, 1), (-1, 0, 1))) 
        cartesian_product_3d.remove((0,0,0))
        return [(x+dx, y+dy, z+dz) for dx, dy, dz in cartesian_product_3d]

    def expand_space():
        for cube in list(space):
            for neighbor_cube in neighbours(cube[0], cube[1], cube[2]):
                if neighbor_cube not in space:
                    space[neighbor_cube] = "."

    def count_active():
        for cube in list(space):
            for neighbor_cube in neighbours(cube[0], cube[1], cube[2]):
                if neighbor_cube in space and space[neighbor_cube] == "#":
                    neighbor_counter[cube] += 1

    def change_simultaneously():
        for cube in list(space):
            if neighbor_counter[cube] == 3:
                space[cube] = "#"
            if neighbor_counter[cube] not in [2,3]:
                space[cube] = "."

    neighbor_counter = defaultdict(int)
    expand_space()
    count_active()
    change_simultaneously()

def part_1():
    for cycle_it in range(6):
        cycle()
    print( sum([1 for cube in space if space[cube] == "#"])  )

part_1()
        






space = {} #{(1,1,1): "#"}
neighbor_counter = defaultdict(int)

for y_coordinate, row in enumerate(data):
    for x_coordinate, cube_state in enumerate(row):
        space[(x_coordinate, y_coordinate, 0,0)] = cube_state


def cycle_4d():
    def neighbours(x,y,z,w):
        cartesian_product_4d = list(product((-1, 0, 1), repeat=4)) #list(product((-1, 0, 1), (-1, 0, 1), (-1, 0, 1))) 
        cartesian_product_4d.remove((0,0,0,0))
        return [(x+dx, y+dy, z+dz, w+dw) for dx, dy, dz, dw in cartesian_product_4d]

    def expand_space():
        for cube in list(space):
            for neighbor_cube in neighbours(cube[0], cube[1], cube[2], cube[3]):
                if neighbor_cube not in space:
                    space[neighbor_cube] = "."

    def count_active():
        for cube in list(space):
            neighbor_counter[cube] = 0
            for neighbor_cube in neighbours(cube[0], cube[1], cube[2], cube[3]):
                if neighbor_cube in space and space[neighbor_cube] == "#":
                    neighbor_counter[cube] += 1

    def change_simultaneously():
        for cube in list(space):
            if neighbor_counter[cube] == 3:
                space[cube] = "#"
            if neighbor_counter[cube] not in [2,3]:
                space[cube] = "."


    expand_space()
    count_active()
    change_simultaneously()

def part_2():
    for cycle_it in range(6):
        cycle_4d()
    print( sum([1 for cube in space if space[cube] == "#"])  )

part_2()











    

    #pro way
# def part_1(data):
#     def neighbours(x, y, z):
#         return [(x + dx, y + dy, z + dz)
#                 for dx, dy, dz in itertools.product((-1, 0, 1), repeat=3)
#                 if not dx == dy == dz == 0]

#     active = set((x, y, 0) for y, line in enumerate(data)
#                  for x, c in enumerate(line)
#                  if c == "#")

#     for cycle in range(1, 7):
#         active_copy = set(active)
#         for z in range(-cycle, cycle+1):
#             for x, y in itertools.product(range(-cycle, cycle+1), repeat=2):
#                 active_neighbours = sum(n in active
#                                         for n in neighbours(x, y, z))
#                 if (x, y, z) in active and active_neighbours not in [2, 3]:
#                     active_copy.remove((x, y, z))
#                 elif (x, y, z) not in active and active_neighbours == 3:
#                     active_copy.add((x, y, z))
#         active = set(active_copy)

#     return len(active)