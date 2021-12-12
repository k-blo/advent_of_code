import os, sys
path = os.path.dirname(os.path.realpath(__file__)) 
with open(path + '/day_5_input.txt', 'r') as text_file: 

    data = text_file.read().splitlines() 


data = [
"0,9 -> 5,9",
"8,0 -> 0,8",
"9,4 -> 3,4",
"2,2 -> 2,1",
"7,0 -> 7,4",
"6,4 -> 2,0",
"0,9 -> 2,9",
"3,4 -> 1,4",
"0,0 -> 8,8",
"5,5 -> 8,2",
]


from collections import defaultdict



def R_between(x1,x2):
    if x1<x2:
        between = list(range(x1+1,x2))
    elif x1==x2:
        between = [x1]
    else:
        between = list(range(x1-1,x2,-1))
    return between



def part_1():
    coordinates = defaultdict(int)

    for vector in data:
        endpoints = vector.split(" -> ")
        start = tuple(int(xy) for xy in endpoints[0].split(","))
        end = tuple(int(xy) for xy in endpoints[1].split(","))

        coordinates_between = []

        if start[0] == end[0]: 
            coordinates_between = [(start[0],coordinate) for coordinate in R_between(start[1],end[1])]
            
        if start[1] == end[1]:
            coordinates_between = [(coordinate, start[1]) for coordinate in R_between(start[0],end[0])]
        
        if coordinates_between:
            for vector_tuple in coordinates_between + [start, end]:
                coordinates[vector_tuple] += 1

    print("Solution Part 1:")
    print (len([vent for vent in coordinates.values() if vent > 1]))

part_1()


def part_2():
    coordinates = defaultdict(int)

    for vector in data:
        endpoints = vector.split(" -> ")
        start = tuple(int(xy) for xy in endpoints[0].split(","))
        end = tuple(int(xy) for xy in endpoints[1].split(","))

        coordinates_between = []

        if start[0] == end[0]: 
            coordinates_between = [(start[0],coordinate) for coordinate in R_between(start[1],end[1])]
            
        elif start[1] == end[1]:
            coordinates_between = [(coordinate, start[1]) for coordinate in R_between(start[0],end[0])]

        elif len(R_between(start[1],end[1])) == len(R_between(start[0],end[0])):
            coordinates_between = list(zip(R_between(start[0],end[0]), R_between(start[1],end[1]) ))


            # print ([start]+coordinates_between+[end])
        
        #if coordinates_between:
        for vector_tuple in coordinates_between + [start, end]:
            coordinates[vector_tuple] += 1

    print("Solution Part 2:")
    print (len([vent for vent in coordinates.values() if vent > 1]))

    for y in range(0,10):
        row = ""
        for x in range(0,10):
            if coordinates[x,y] == 0:
                row += "."
            else:
                row += str(coordinates[x,y])
        print (row)



part_2()

