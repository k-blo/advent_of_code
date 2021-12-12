

data= [
"2238518614",
"4552388553",
"2562121143",
"2666685337",
"7575518784",
"3572534871",
"8411718283",
"7742668385",
"1235133231",
"2546165345",
]

# data=[
# "5483143223",
# "2745854711",
# "5264556173",
# "6141336146",
# "6357385478",
# "4167524645",
# "2176841721",
# "6882881134",
# "4846848554",
# "5283751526",
# ]

# data=[
# "11111",
# "19991",
# "19191",
# "19991",
# "11111",
# ]


from itertools import product
cartesian_product = list(product([0,1,-1],[1,-1,0])) 
cartesian_product.remove((0,0))

def Adjacent(x,y):
    return [(xd+x,yd+y) for xd, yd in cartesian_product
            if not -1 in [xd+x,yd+y] 
            and xd+x < len(data[0]) 
            and yd+y < len(data)]

def Energize(x,y):
    global count_flashes
    grid[x][y] += 1
    if grid[x][y] == 10:
        count_flashes += 1
        Flash(x,y)

def Flash(x,y):
    for xa,ya in Adjacent(x,y):
        Energize(xa,ya)

coordinates = [ (x,y) for x in range(len(data[0])) for y in range(len(data))]
def Discharge():
    for x,y in coordinates:
        if grid[x][y] > 9:
            grid[x][y] = 0

def part1():
    global count_flashes
    global grid
    count_flashes = 0
    grid = [list(map(int, row)) for row in data]

    for i in range(100):
        for x,y in coordinates:
            Energize(x,y)
        Discharge()

    print("Solution 1: ")
    print (count_flashes)

def part2():
    global grid
    grid = [list(map(int, row)) for row in data]

    for i in range(2000):
        for x,y in coordinates:
            Energize(x,y)
        Discharge()

        if (sum([grid[x][y] for x,y in coordinates])) == 0:
            print("Solution 2: ")
            print (i+1)
            return

part1()
part2()