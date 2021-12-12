from collections import defaultdict
import os, sys
path = os.path.dirname(os.path.realpath(__file__)) 
with open(path + '/day_24_input.txt', 'r') as text_file: 

    data = text_file.read().splitlines()



# data = [
# "sesenwnenenewseeswwswswwnenewsewsw",
# "neeenesenwnwwswnenewnwwsewnenwseswesw",
# "seswneswswsenwwnwse",
# "nwnwneseeswswnenewneswwnewseswneseene",
# "swweswneswnenwsewnwneneseenw",
# "eesenwseswswnenwswnwnwsewwnwsene",
# "sewnenenenesenwsewnenwwwse",
# "wenwwweseeeweswwwnwwe",
# "wsweesenenewnwwnwsenewsenwwsesesenwne",
# "neeswseenwwswnwswswnw",
# "nenwswwsewswnenenewsenwsenwnesesenew",
# "enewnwewneswsewnwswenweswnenwsenwsw",
# "sweneswneswneneenwnewenewwneswswnese",
# "swwesenesewenwneswnwwneseswwne",
# "enesenwswwswneneswsenwnewswseenwsese",
# "wnwnesenesenenwwnenwsewesewsesesew",
# "nenewswnwewswnenesenwnesewesw",
# "eneswnwswnwsenenwnwnwwseeswneewsenese",
# "neswnwewnwnwseenwseesewsenwsweewe",
# "wseweeenwnesenwwwswnew",
# ]


directions = {
"e": (2,0),
"se": (1,-1),
"sw": (-1,-1),
"w": (-2, 0),
"nw": (-1,1),
"ne": (1, 1),
}




# data = ["nwwswee"]
# data = ["esew"]
hexagonal_map = {}



for instruction in data:

    read_instructions = []
    while len(instruction) > 0:
        for i in [1,2]:
            if instruction[:i] in directions:
                read_instructions.append(instruction[:i])
                instruction = instruction[i:]
                break

    reference_tile = (0,0)
    for xy in read_instructions:
        xy = directions[xy]
        reference_tile = tuple(map(sum,zip(reference_tile,xy)))

    if reference_tile not in hexagonal_map:
        hexagonal_map[reference_tile] = "black"
    else:
        if hexagonal_map[reference_tile] == "black":
            hexagonal_map[reference_tile] = "white"
        else:
            hexagonal_map[reference_tile] = "black"

print ("PART 1: " + str(len([tile for tile in hexagonal_map.values() if tile == "black"])))
    


def adjacent_hex(xy_tuple):
    return [tuple(map(sum,zip(xy_tuple,xy))) for xy in directions.values()]
        
from copy import deepcopy

def part_2_rules(hexmap):
    for tile in list(hexmap):
        for adj in adjacent_hex((tile)):
            if adj not in hexmap:
                hexmap[adj] = "white"


    old_map = deepcopy(hexmap)
    for tile in old_map:
        black = 0
        for adj in adjacent_hex((tile)):
            if adj in old_map and old_map[adj] == "black":
                black += 1

        if hexmap[tile] == "black":
            if black > 2 or black == 0:
                hexmap[tile] = "white"
        elif hexmap[tile] == "white":
            if black == 2:
                hexmap[tile] = "black"


for i in range(100):
    part_2_rules(hexagonal_map)
print ("PART 2: " + str(len([tile for tile in hexagonal_map.values() if tile == "black"])))
    