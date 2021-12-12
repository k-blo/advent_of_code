with open('/Users/kevin/PycharmProjects/advent of code/day_9_input.txt', 'r') as text_file:
    data = text_file.read().splitlines()

from itertools import combinations


data = list(map(int, data))

def part_1():
    valid_numbers = []
    invalid_numbers = []

    for count, number in enumerate(data[25:],25) :
        preambel = data[count-25:count]
        for pre_number in combinations(preambel,2 ):
            if sum(pre_number) == number:
                valid_numbers.append(number)
        
        if number not in valid_numbers:
            invalid_numbers.append(number)
                
    return invalid_numbers[0]




def part_2():
    for i in range(2, len(data)):
        for count, number in enumerate(data):
            if sum(data[count:count+i]) == 14144619:
                return max(data[count:count+i]) + min(data[count:count+i])







print ("part 1 solution: " + str(part_1()))

print ("part 2 solution: " + str(part_2()))

