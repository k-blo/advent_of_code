data = [
"L.LL.LL.LL",
"LLLLLLL.LL",
"L.L.L..L..",
"LLLL.LL.LL",
"L.LL.LL.LL",
"L.LLLLL.LL",
"..L.L.....",
"LLLLLLLLLL",
"L.LLLLLL.L",
"L.LLLLL.LL",
]

with open('/Users/kevin/Documents/code/advent of code/day_11_input.txt', 'r') as text_file: 
    data = text_file.read().splitlines()

row_max = len(data) -1 
seat_max = len(data[0]) -1    

def get_adjacent(row_num, seat_num, seat_order): 
    return [seat_order[row_num+row_][seat_num+seat_] 
            for row_,seat_ in [(0,-1), (0,1),    (-1,0), (-1,1), (-1,-1) ,  (1,0), (1,1), (1,-1)] 
            if 0 <= row_num+row_ <= row_max and 0 <= seat_num+seat_ <= seat_max]


def get_adjacent_or_view(which_one, row_num, seat_num, seat_order):
    if which_one == "adjacent":
        return get_adjacent(row_num,seat_num, seat_order)
    if which_one == "view":
        return get_view(row_num, seat_num, seat_order)

def occupy(seat_order,criteria):
    seat_max = 4
    if criteria == "view":
        seat_max = 5
    new_order = [list(row) for row in seat_order]  # list(seat_order)   # shallow vs deep copy 
    for row_num, row in enumerate(seat_order):        
        for seat_num, seat in enumerate(row):
            if seat == "L" and not "#" in get_adjacent_or_view(criteria, row_num, seat_num, seat_order):
                new_order[row_num][seat_num] = "#"
            elif seat == "#" and get_adjacent_or_view(criteria, row_num, seat_num, seat_order).count("#") >= seat_max:
                new_order[row_num][seat_num] = "L"
    return new_order

def find_seating(seat_order, criteria):
    while True:
        previous_order = list(seat_order)
        seat_order = occupy(seat_order, criteria)
        if previous_order == seat_order:
            return seat_order

def part_1():
    return sum([row.count("#") for row in find_seating(data, "adjacent") ])
    
print (part_1())







def get_view(row_num, seat_num, seat_order):
    seats = [   see(x,y, row_num, seat_num,  seat_order) 
                    for x in [-1,0,1]
                    for y in [-1,0,1]
                    if not (x==0 and y==0)
            ] 
    return [x for x in seats if x != None]

def see(x,y, row_num, seat_num,  seat_order):
    for distance in range(1,seat_max+row_max):
        cx = x*distance
        cy = y*distance
        cx += seat_num
        cy += row_num
        if 0 <= cy  <= row_max and 0 <= cx  <= seat_max: 
            if seat_order[cy][cx] != ".":
                return seat_order[cy][cx]
            else:
                continue

def part_2():
    return sum([row.count("#") for row in find_seating(data, "view") ])


print (part_2())

# from itertools import permutations, combinations, combinations_with_replacement
# print ( list(permutations([0,1,-1],2)) )
# print ( list(combinations([0,1,-1],2)) )
# print ( list(combinations_with_replacement([0,1,-1],2)) )









### pro way

# import itertools


# def part_1(data):
#     seats = [[c for c in line.strip()] for line in data]
#     w = len(seats[0])
#     h = len(seats)

#     def neighbours(x, y):
#         return [(x + dx, y + dy)
#                 for dx in range(-1, 2)
#                 for dy in range(-1, 2)
#                 if (dx, dy) != (0, 0) and 0 <= (x+dx) < w and 0 <= (y+dy) < h]

#     while True:
#         new_seats = [row[:] for row in seats]
#         for y, row in enumerate(seats):
#             for x, c in enumerate(row):
#                 if c == ".":
#                     continue

#                 count = sum(seats[ny][nx] == "#" for nx, ny in neighbours(x, y))
#                 if c == "L" and count == 0:
#                     new_seats[y][x] = "#"
#                 elif c == "#" and count >= 4:
#                     new_seats[y][x] = "L"

#         if seats == new_seats:
#             return sum(c == "#" for row in seats for c in row)
#         seats = new_seats


# def part_2(data):
#     seats = [[c for c in line.strip()] for line in data]
#     w = len(seats[0])
#     h = len(seats)

#     def visible_from(x, y):
#         for dx in range(-1, 2):
#             for dy in range(-1, 2):
#                 if (dx, dy) == (0, 0):
#                     continue
                
#                 distance = 1
#                 while 0 <= x+(dx*distance) < w and 0 <= y+(dy*distance) < h:
#                     c = seats[y+dy*distance][x+dx*distance]
#                     if c != ".":
#                         yield c
#                         break
#                     distance += 1 

#     while True:
#         new_seats = [row[:] for row in seats]
#         for y, row in enumerate(seats):
#             for x, c in enumerate(row):
#                 if c == ".":
#                     continue

#                 count = sum(c == "#" for c in visible_from(x, y))
#                 if c == "L" and count == 0:
#                     new_seats[y][x] = "#"
#                 elif c == "#" and count >= 5:
#                     new_seats[y][x] = "L"

#         if seats == new_seats:
#             return sum(c == "#" for row in seats for c in row)
#         seats = [row[:] for row in new_seats]


# if __name__ == '__main__':
#     with open('/Users/kevin/Documents/code/advent of code/day_11_input.txt', 'r') as f:
#         inp = f.readlines()
#         print("Part 1 answer: " + str(part_1(inp)))
#         print("Part 2 answer: " + str(part_2(inp)))