import os
path = os.path.dirname(os.path.realpath(__file__)) + "/" + "day_25_input.txt"
data = [line.strip() for line in open(path)]


# data = [
# "v...>>.vv>",
# ".vv>>.vv..",
# ">>.>v>...v",
# ">>v>>.>.v.",
# "v>v.vv.v..",
# ">.>>..v...",
# ".vv..>.>v.",
# "v.v..>>v.v",
# "....v..v.>",
# ]

# data = [
# "...>...",
# ".......",
# "......>",
# "v.....>",
# "......>",
# ".......",
# "..vvv..",
# ]



def Coords(data):
    return [ (x,y) for x in range(len(data[0])) for y in range(len(data))]

def Adjacent_Cucumbers(x,y, cucumber):
    herd_directions = {">": (1,0), "v": (0,1)}
    target = herd_directions[cucumber]
    if target[0]+x > len(data[0])-1:
        target = (0,y)
    elif target[1]+y > len(data)-1:
        target = (x,0)
    else:
        target = (target[0]+x, target[1]+y)
    return target[0], target[1]



from copy import deepcopy
herd = [list(line) for line in data]
herd_new_positions = deepcopy(herd)
# for line in herd_new_positions:
#     print("".join(line))

previous_herd_positions = None

for i in range(1000):

        
    for herd_moves_first in [">", "v"]:
        herd = deepcopy(herd_new_positions)
        for x,y in Coords(herd):
            if herd[y][x] in herd_moves_first:
                new_x, new_y = Adjacent_Cucumbers(x,y, herd_moves_first)
                if herd[new_y][new_x] == ".":
                    herd_new_positions[y][x] = "." 
                    herd_new_positions[new_y][new_x] = herd_moves_first

    if previous_herd_positions == herd_new_positions:
        print(i+1)
        break

    previous_herd_positions = deepcopy(herd_new_positions)
    print ("Sea cucumbers still moving", i+1)

    # print ("new herd positions: ", i+1,)    
    # for line in herd_new_positions:
    #     print("".join(line))

        
            