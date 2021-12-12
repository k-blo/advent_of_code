#with open('/Users/kevin/PycharmProjects/advent of code/day_10_input.txt', 'r') as text_file:
with open('/Users/kevin/Documents/code/advent of code/day_10_input.txt', 'r') as text_file: 
    data = text_file.read().splitlines()
    data = sorted(map(int, data))

def part1(data):
    data = [0] + data + [max(data)+3]
    jolt_spaces = ([data[count+1]-adapter for count, adapter in enumerate(data[:-1])])
    print (jolt_spaces.count(1) * jolt_spaces.count(3))

part1(data)


from collections import defaultdict

def part2(data):
    combinations = defaultdict(int)
    combinations[0] = 1 ### the zero adapter allows exactly 1 combination // this is the ur-accumulation
    for jolts in data:
        for i in [1,2,3]:
            combinations[jolts] += combinations[jolts-i] 
    
    print (combinations)

part2(data)


## pro way
from collections import defaultdict


def part_1(data):
    data = sorted(map(int, data))
    data = [0] + data + [max(data)+3]

    return (sum(data[i] - data[i-1] == 1 for i in range(1, len(data))) *
            sum(data[i] - data[i-1] == 3 for i in range(1, len(data))))


def part_2(data):
    data = sorted(map(int, data))

    combinations = defaultdict(int)
    combinations[0] = 1
    for jolts in data:
        combinations[jolts] = sum(combinations[jolts-i] for i in range(1, 4))
    return combinations[data[-1]]


if __name__ == '__main__':
    with open('/Users/kevin/Documents/code/advent of code/day_10_input.txt', 'r') as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))