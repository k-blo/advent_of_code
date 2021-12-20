import os
path = os.path.dirname(os.path.realpath(__file__)) + "/" + "day_15_input.txt"
data = [line.strip() for line in open(path)]

data= [
"1163751742",
"1381373672",
"2136511328",
"3694931569",
"7463417111",
"1319128137",
"1359912421",
"3125421639",
"1293138521",
"2311944581",
]


cavern = list(map(list, data))
cavern = [list(map(int, row)) for row in cavern]
coordinates = [ (x,y) for x in range(len(data[0])) for y in range(len(data))]
edge = (len(data[0])-1, len(data)-1)

from itertools import product

def Add_Tuples(tuple1, tuple2):
    return tuple(sum(x) for x in zip(tuple1, tuple2))


def Paths(how_far):
    down_or_right = [(0,1), (1,0)] 
    cartesian_product = list(product(down_or_right, repeat=how_far))
    paths = []
    for path in cartesian_product:
        added_tuples = []
        previous = (0,0)
        for tuple in path:
            added_tuples += [Add_Tuples(previous, tuple)]
            previous = Add_Tuples(previous, tuple)
        paths += [added_tuples]
    return paths


def Scan(x,y, how_far):
    risks = []
    for path in path_lib[how_far]:
        this_risk = 0
        this_way = []
        try:
            for xg, yg in path:
                this_risk += cavern[yg+y][xg+x]
                this_way += [(xg+x, yg+y)]
            risks.append( (this_way, this_risk) )

        except Exception as e: 
            pass
            
    if risks:
        return min(risks, key=lambda i:i[1])

from collections import defaultdict
Ants = defaultdict(int)

lib_max = 3
path_lib = {}
for i in range(1,lib_max):
    path_lib[i] = Paths(i)

coord_lib = {}
for x, y in coordinates:
    coord_lib[(x,y)] = [Scan(x,y, i) for i in range(1,lib_max)]
print ("lib created")



def Find_Path(x,y, risk=0, chosen_paths=[], chosen_risks=[]):
    chosen_path_selection = coord_lib[(x,y)]
    
    remember = "default"

    for chosen_path in chosen_path_selection:
        if chosen_path:

            new_position = chosen_path[0][0]
            if remember != new_position:
                remember = new_position
                x, y = new_position[0], new_position[1]
                risk2 = risk + cavern[y][x]
                chosen_paths2 = chosen_paths + [new_position]
                chosen_risks2 = chosen_risks + [cavern[y][x]]
                
                if risk2 < 400:
                    if new_position != edge:
                        #if len(Ants) < 150: #130 = 413 #120 with scan3 = 409
                        Find_Path(x, y, risk=risk2, chosen_paths=chosen_paths2, chosen_risks=chosen_risks2)
                    else:
                        if risk2 not in Ants:
                            Ants[risk2] = chosen_risks2
                            print("new: ", risk2)

Find_Path(0,0)
print(min(Ants.keys()))


