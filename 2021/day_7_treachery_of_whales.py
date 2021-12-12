import os, sys
path = os.path.dirname(os.path.realpath(__file__)) 
with open(path + '/day_7_input.txt', 'r') as text_file: 

    data = text_file.read().splitlines() 

data = list(map(int,data[0].split(",")))




# data = [16,1,2,0,4,2,7,1,2,14]

print(sum(range(1,4)))

def part1():
    fuel_experiments = []
    for i in range(len(data)):
        fuel = 0
        for crab in data:
            fuel += abs(crab - i)
        fuel_experiments += [(i, fuel)]

    sorted_by_second_value = sorted(fuel_experiments, key=lambda tup: tup[1])
    print("part 1 solution: ")
    print(sorted_by_second_value[0][1])

part1()


def part2():
    fuel_experiments = []
    for i in range(len(data)):
        fuel = 0
        for crab in data:
            distance = abs(crab - i)
            fuel += sum(range(1,distance+1))
        fuel_experiments += [(i, fuel)]

    sorted_by_second_value = sorted(fuel_experiments, key=lambda tup: tup[1])
    print("part 2 solution: ")
    print(sorted_by_second_value[0][1])

part2()