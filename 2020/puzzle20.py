import os, sys
path = os.path.dirname(os.path.realpath(__file__)) 
with open(path + '/day_20_input.txt', 'r') as text_file: 

    data = text_file.read().splitlines()

# data = [
# "Tile 2311:",
# "..##.#..#.",
# "##..#.....",
# "#...##..#.",
# "####.#...#",
# "##.##.###.",
# "##...#.###",
# ".#.#.#..##",
# "..#....#..",
# "###...#.#.",
# "..###..###",
# "Tile 1951:",
# "#.##...##.",
# "#.####...#",
# ".....#..##",
# "#...######",
# ".##.#....#",
# ".###.#####",
# "###.##.##.",
# ".###....#.",
# "..#.#..#.#",
# "#...##.#..",
# "Tile 1171:",
# "####...##.",
# "#..##.#..#",
# "##.#..#.#.",
# ".###.####.",
# "..###.####",
# ".##....##.",
# ".#...####.",
# "#.##.####.",
# "####..#...",
# ".....##...",
# "Tile 1427:",
# "###.##.#..",
# ".#..#.##..",
# ".#.##.#..#",
# "#.#.#.##.#",
# "....#...##",
# "...##..##.",
# "...#.#####",
# ".#.####.#.",
# "..#..###.#",
# "..##.#..#.",
# "Tile 1489:",
# "##.#.#....",
# "..##...#..",
# ".##..##...",
# "..#...#...",
# "#####...#.",
# "#..#.#.#.#",
# "...#.#.#..",
# "##.#...##.",
# "..##.##.##",
# "###.##.#..",
# "Tile 2473:",
# "#....####.",
# "#..#.##...",
# "#.##..#...",
# "######.#.#",
# ".#...#.#.#",
# ".#########",
# ".###.#..#.",
# "########.#",
# "##...##.#.",
# "..###.#.#.",
# "Tile 2971:",
# "..#.#....#",
# "#...###...",
# "#.#.###...",
# "##.##..#..",
# ".#####..##",
# ".#..####.#",
# "#..#.#..#.",
# "..####.###",
# "..#.#.###.",
# "...#.#.#.#",
# "Tile 2729:",
# "...#.#.#.#",
# "####.#....",
# "..#.#.....",
# "....#..#.#",
# ".##..##.#.",
# ".#.####...",
# "####.#.#..",
# "##.####...",
# "##..#.##..",
# "#.##...##.",
# "Tile 3079:",
# "#.#.#####.",
# ".#..######",
# "..#.......",
# "######....",
# "####.#..#.",
# ".#...#.##.",
# "#.#####.##",
# "..#.###...",
# "..#.......",
# "..#.###...",
# ]

tiles = dict()

for line in data:
    if "Tile" in line:
        id = int(line[5:9])
        tiles[id] = []
    elif len(line) > 2:
        tiles[id].append(line)

grid = {(0,0): list(tiles)[0] }
rotated_flipped = {}




def rotate90(tile_list):
    rotated_tile = []
    for i in range(len(tile_list)-1,-1,-1):
        rotated_tile.append("".join([tile_line[i] for tile_line in tile_list]) )
    return rotated_tile

def flip_horizontal(tile_list):
    return [tile_line[::-1] for tile_line in tile_list]

def get_sides2(tile_list):
    top = tile_list[0]
    bottom = tile_list[-1]
    left = "".join([tile_row[0] for tile_row in tile_list])
    right = "".join([tile_row[9] for tile_row in tile_list])
    return {(0,1): top, (0,-1): bottom, (-1,0): left, (1,0): right}

def check_sides2(id, fixed_tile_xy):
    fixed_tile_id = grid[fixed_tile_xy]

    for side_key, side in get_sides2(tiles[fixed_tile_id]).items():
        for other_side_key, other_side in get_sides2(tiles[id]).items():

            if side in [other_side, other_side[::-1]] :
                grid[(fixed_tile_xy[0]+side_key[0], fixed_tile_xy[1]+side_key[1])] = id
                rearrange(fixed_tile_id, id, side_key)

def rearrange(fixed_tile_id, id, side_key):
    sides_attached = {(0,1):(0,-1), (0,-1):(0,1), (-1,0):(1,0), (1,0):(-1,0)}
    opposing_side = sides_attached[side_key]
    fixed_tile = get_sides2(tiles[fixed_tile_id])
    new_tile = get_sides2(tiles[id])

    for i in range(4):
        for function in [rotate90, flip_horizontal]:

            tiles[id] = function(tiles[id])
            new_tile = get_sides2(tiles[id])
            if fixed_tile[side_key] == new_tile[opposing_side]:
                return

        tiles[id] = flip_horizontal(tiles[id])




for i in range(10):
    for id in list(tiles)[1:]:
        if id not in grid.values():
            for fixed_tile_xy in list(grid):
                
                if check_sides2(id, fixed_tile_xy):
                    break

smallest_x, smallest_y = 0,0
for xy in grid:
    if xy[0] < smallest_x:
        smallest_x = xy[0]
    if xy[1] < smallest_y:
        smallest_y = xy[1]

grid_adjusted = {}
for xy in grid:
    grid_adjusted[(xy[0]-smallest_x, xy[1]-smallest_y)] = grid[xy]

import math
square_side = int(math.sqrt(len(tiles)))
matrix = []
for i in range(square_side):
    matrix.append(["x" for x in range(square_side)])

for xy in grid_adjusted:
    matrix[xy[1]][xy[0]] = grid_adjusted[xy]
# for matrix_row in matrix:
#     print (matrix_row)

print ("PART 1: ")
print(matrix[0][0] * matrix[0][-1] * matrix[-1][0] * matrix[-1][-1])


def cut_borders(tile_list):
    tile_list = tile_list[1:-1]
    new_tile = []
    for line in tile_list:
        new_tile.append(line[1:-1])
    return new_tile

for id in tiles:
    tiles[id] = cut_borders(tiles[id])
    tile_length = len(tiles[id])

print ("length: " + str(tile_length))



actual_image = []
for line in matrix:
    for i in range(tile_length):
        actual_image_line = ""
        for id in line:
            actual_image_line += tiles[id][i]
        actual_image.append(actual_image_line)
        #print (actual_image_line)

print("height/width: " + str(len(actual_image[0])) + "/" + str(len(actual_image)))





sea_monster = [
"                  # ",
"#    ##    ##    ###",
" #  #  #  #  #  #   ",
]



def create_grid(image):
    a_grid = {}
    for y, line in enumerate(image):
        for x, character in enumerate(line):
            a_grid[(x,y)] = character


    return a_grid

sea_monster_grid = create_grid(sea_monster)
actual_image_grid = create_grid(actual_image)


def detect_seamonster(pixel):
    for sea_monster_pixel in sea_monster_grid:
        if sea_monster_grid[sea_monster_pixel] == "#":
            try:
                if "#" != actual_image_grid[(pixel[0]+sea_monster_pixel[0], pixel[1]+sea_monster_pixel[1])]:
                    return False
            except:
                return False
    return True

seamonsters = 0

for i in range(5):

    actual_image = rotate90(actual_image)
    actual_image_grid = create_grid(actual_image)

    seamonsters = len([True for pixel in actual_image_grid if detect_seamonster(pixel)])
    if seamonsters > 0:
        break

    actual_image = flip_horizontal(actual_image)
    actual_image_grid = create_grid(actual_image)

    seamonsters = len([True for pixel in actual_image_grid if detect_seamonster(pixel)])
    if seamonsters > 0:
        break

    actual_image = flip_horizontal(actual_image)

print (str(seamonsters) + " seamonsters found!")

print(len([pixel for pixel in actual_image_grid.values() if pixel == "#"]) - seamonsters * len([pixel for pixel in sea_monster_grid.values() if pixel == "#"]))










import sys

def rotate(tile):
    return list(''.join(x[::-1]) for x in zip(*tile))

def flip(tile):
    return list(reversed(tile.copy()))

def build_tile_transformations(tile):
    tile90 = rotate(tile)
    tile180 = rotate(tile90)
    tile270 = rotate(tile180)
    return [tile, tile90, tile180, tile270, flip(tile), flip(tile90), flip(tile180), flip(tile270)]

def get_monster_indexes():
    monster_pattern = [
        '                  # ',
        '#    ##    ##    ###',
        ' #  #  #  #  #  #   '
    ]
    return [(r, c) for r in range(len(monster_pattern)) for c in range(len(monster_pattern[r])) if monster_pattern[r][c] == '#']

def assemble_tiles(tile_transformations):
    n = int(len(tile_transformations)**0.5)
    assembled = [[(0, 0)] * n for _ in range(n)]
    remaining = set(tile_transformations.keys())

    def _assemble_tiles(rowcolumn):
        if rowcolumn == n * n:
            return True
        r, c = rowcolumn // n, rowcolumn % n
        for tileid in list(remaining):
            for i, transformation in enumerate(tile_transformations[tileid]):
                up_ok = left_ok = True
                if r > 0:
                    up_tileid, up_transformation = assembled[r - 1][c]
                    up_tile = tile_transformations[up_tileid][up_transformation]
                    up_ok = all(transformation[0][i] == up_tile[9][i] for i in range(10))
                if c > 0:
                    left_tileid, left_transformation = assembled[r][c - 1]
                    left_tile = tile_transformations[left_tileid][left_transformation]
                    left_ok = all(transformation[i][0] == left_tile[i][9] for i in range(10))
                if up_ok and left_ok:
                    assembled[r][c] = (tileid, i)
                    remaining.remove(tileid)
                    if _assemble_tiles(rowcolumn + 1):
                        return True
                    remaining.add(tileid)
        return False
    _assemble_tiles(0)
    
    return assembled

def part1(tile_matrix):
    return tile_matrix[0][0][0] * tile_matrix[0][-1][0] * tile_matrix[-1][0][0] * tile_matrix[-1][-1][0]

def part2(tile_matrix, tile_transformations):
    n = int(len(tile_transformations)**0.5)
    image = [['.'] * (n * 8) for _ in range(n * 8)]

    for r in range(n):
        for c in range(n):
            tileid, transformation = tile_matrix[r][c]
            tile = tile_transformations[tileid][transformation]
            for i in range(1, 9):
                for j in range(1, 9):
                    image[8 * r + i - 1][8 * c + j - 1] = tile[i][j]

    for image in build_tile_transformations(image):

        monster = 0
        for r in range(len(image) - 3):
            for c in range(len(image) - 20):
                if all(image[r + dr][c + dc] == '#' for dr, dc in get_monster_indexes()):
                    monster += 1
        if monster > 0:
            total = sum(row.count('#') for row in image)
            return total - monster * len(get_monster_indexes())

lines = data

tiles = {}
tileid, matrix = 0, []
for line in lines:
    if not line:
        tiles[tileid] = matrix
        tileid, matrix = 0, []
    elif line.startswith('Tile'):
        tileid = int(line.replace(':', '').split()[1])
    else:
        matrix.append(line)

tile_transformations = {tileid: build_tile_transformations(tile) for tileid, tile in tiles.items()}
tile_matrix = assemble_tiles(tile_transformations)

print(f'Part 1: {part1(tile_matrix)}, Part 2: {part2(tile_matrix, tile_transformations)}')















