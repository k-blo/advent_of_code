import os, sys
path = os.path.dirname(os.path.realpath(__file__)) 
with open(path + '/day_9_input.txt', 'r') as text_file: 

    data = text_file.read().splitlines() 



data= [
"2199943210",
"3987894921",
"9856789892",
"8767896789",
"9899965678",
]


def Get_Adjacent(row,index):
    adjacent = {"up": (-1,0), "down": (1,0), "left": (0,-1), "right": (0,1)}
    neighbours = []
    for row_n, index_n in adjacent.values():
        if not -1 in [index+index_n, row+row_n]:
            try:
                neighbours += data[row+row_n][index+index_n]
            except:
                pass
    return neighbours

def is_lowpoint(row,index):
    for neighbor in Get_Adjacent(row,index):
        if data[row][index] >= neighbor:
            return False
    return True

def part_1():
    low_points = []
    for row, string in enumerate(data):
        for index, number in enumerate(string):
            if is_lowpoint(row,index):
                low_points += [int(number)]
    print("part 1 solution: ")
    print(sum([risk_level +1 for risk_level in low_points]))

part_1()





def Get_Adjacent_Coordinates(row,index):
    adjacent = {"up": (-1,0), "down": (1,0), "left": (0,-1), "right": (0,1)}
    neighbours = []
    for row_n, index_n in adjacent.values():
        if not -1 in [index+index_n, row+row_n]:
            try:
                neighbours += [(row+row_n,index+index_n, int(data[row+row_n][index+index_n]))]
            except:
                pass
    return neighbours


def Find_Basin(basin):
    expand_basin = []
    for row0, index0, number0 in basin:
        for row, index, number in Get_Adjacent_Coordinates(row0,index0):
            if number != 9 and (row, index, number) not in basin:
                expand_basin.append((row,index,number))
    if expand_basin: ##### go recursive
        basin = Find_Basin(basin+expand_basin)

    return set(basin)
    

import math
def part_2():
    basin_sizes = []
    for row, string in enumerate(data):
        for index, number in enumerate(string):
            if is_lowpoint(row,index):
                start_basin = [(row, index, int(number))]
                expanded_basin = Find_Basin(start_basin)
                basin_sizes += [len(expanded_basin)]

    basin_sizes.sort(reverse=True)
    print("part 2 solution: ")
    print(math.prod(basin_sizes[:3]))

part_2()



