


import os, sys
path = os.path.dirname(os.path.realpath(__file__)) 

with open(path + '/day_13_input.txt', 'r') as text_file: 
    data = text_file.read().splitlines()

    # data = ["939","7,13,x,x,59,x,31,19"]
    timestamp = int(data[0])
    buslines_raw = data[1].split(",")
    buslines = [int(bus) for bus in buslines_raw if bus != "x"]




def part1(timestamp, buslines):
    waited = 0
    while True:
        for bus in buslines:
            if (timestamp % bus) == 0:
                print (waited * bus)
                return
        timestamp += 1
        waited += 1
        
part1(timestamp, buslines)

def part2(data, buslines, buslines_raw): ### this works but will take forever
    timestamp = 0
    while True:
        if all([(timestamp + buslines_raw.index(str(bus))) % bus == 0 for bus in buslines]):
            print (timestamp)
            return
        timestamp += 1
        if timestamp % 1000 == 0:
            print ("still running...")
            print (timestamp)

from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
 
if __name__ == '__main__':
    a = [-buslines_raw.index(str(bus)) % bus for bus in buslines]
    n = buslines

    print ("chinese remainder")
    print (chinese_remainder(n, a))





###### pro way

# from functools import reduce
# def part_1(data):
#     target = int(data[0])
#     for time in range(target, target+100):
#         for id in data[1].split(","):
#             if id == "x":
#                 continue
#             id = int(id)
#             if time % id == 0:
#                 return id * (time - target)


# def part_2(data):
#     # https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
#     def chinese_remainder(n, a):
#         sum = 0
#         prod = reduce(lambda a, b: a*b, n)
#         for n_i, a_i in zip(n, a):
#             p = prod // n_i
#             sum += a_i * mul_inv(p, n_i) * p
#         return sum % prod

#     def mul_inv(a, b):
#         b0 = b
#         x0, x1 = 0, 1
#         if b == 1:
#             return 1
#         while a > 1:
#             q = a // b
#             a, b = b, a % b
#             x0, x1 = x1 - q * x0, x0
#         if x1 < 0:
#             x1 += b0
#         return x1

#     n = [int(c) for c in data[1].split(",") if c != "x"]
#     a = [(-i) % int(c) for i, c in enumerate(data[1].split(",")) if c != "x"]
#     return chinese_remainder(n, a)


# if __name__ == '__main__':
#     with open('/Users/kevin/Documents/code/advent of code/day_13_input.txt', 'r') as f:
#         inp = f.readlines()
#         print("Part 1 answer: " + str(part_1(inp)))
#         print("Part 2 answer: " + str(part_2(inp)))

