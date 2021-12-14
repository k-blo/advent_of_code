import os, sys
path = os.path.dirname(os.path.realpath(__file__)) 
with open(path + '/day_13_input.txt', 'r') as text_file: 

    data = text_file.read().splitlines() 

# data= [
# "6,10",
# "0,14",
# "9,10",
# "0,3",
# "10,4",
# "4,11",
# "6,0",
# "6,12",
# "4,1",
# "0,13",
# "10,12",
# "3,4",
# "3,0",
# "8,4",
# "1,10",
# "2,14",
# "8,10",
# "9,0",
# "",
# "fold along y=7",
# "fold along x=5",
# ]

dots = []
folds = []
for dot in data:
    if "," in dot:
        dot = dot.split(",")
        dot = tuple(map(int,dot))
        dots.append( dot )
    if "fold" in dot:
        fold = dot.split("=")
        folds += [ (fold[0][-1], int(fold[1])) ]

x = max(dots, key=lambda i:i[0])[0]
y = max(dots, key=lambda i:i[1])[1]

paper = [list("."*(x+1)) for yy in range(y+1) ]

for x,y in dots:
    paper[y][x] = "#"



def flip_horizontal(tile_list):
    return [tile_line[::-1] for tile_line in tile_list]

def flip_vertical(tile_list):
    return [tile_line for tile_line in tile_list[::-1]]


def Fold(along, where, paper):
    if along == "x":
        stays = [line[:where] for line in paper]
        folds = [line[where:] for line in paper]
        folds = flip_horizontal(folds)
    elif along == "y":
        stays = paper[:where]
        folds = paper[where:]
        folds = flip_vertical(folds)
    
    coordinates = [ (x,y) for x in range(len(folds[0])) for y in range(len(folds))]
    for x,y in coordinates:
        if folds[y][x] == "#":
            stays[y][x] = "#"
    return stays


dot_counter = []
for along, where in folds:
    paper = Fold(along, where, paper)
    dot_counter += [sum(line.count("#") for line in paper) ]

print("Part 1 solution: ")
print(dot_counter[0])

print("Part 2 solution: ")
for i in paper:
    print("".join(i))



