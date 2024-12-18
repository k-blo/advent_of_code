import re
import os, sys
path = os.path.dirname(os.path.realpath(__file__)) 
with open(path + '/day_2_input', 'r') as text_file: 
    DATA = text_file.read().splitlines() 

EXAMPLE = [
"7 6 4 2 1",
"1 2 7 8 9",
"9 7 6 2 1",
"1 3 2 4 5",
"8 6 4 4 1",
"1 3 6 7 9",
]


def parse_nums(data):
    return [[int(num) for num in numbers.split()] for numbers in data]

print(parse_nums(EXAMPLE))


def part_1(data):
    safe = 0
    for numbers in parse_nums(data):
        if _is_safe(numbers):
            safe += 1
    return safe


def _is_safe(numbers):
    differences = [numbers[i+1] - numbers[i] for i in range(len(numbers) - 1)]
    valid_gaps_pos = all([(1 <= diff <= 3) for diff in differences])
    valid_gaps_neg = all([(-3 <= diff <= -1) for diff in differences])
    if valid_gaps_pos or valid_gaps_neg:
        return True
                
    

print(part_1(EXAMPLE))
print(part_1(DATA))


def part_2(data):
    safe = 0
    for numbers in parse_nums(data):
        differences = [numbers[i+1] - numbers[i] for i in range(len(numbers) - 1)]
        valid_gaps_pos = [(1 <= diff <= 3) for diff in differences]#.count(False) < 2
        valid_gaps_neg = [(-3 <= diff <= -1) for diff in differences]#.count(False) < 2
        #print(valid_gaps_pos, valid_gaps_neg)
        
        # previous case 1: all are ok
        if all(valid_gaps_pos) or all(valid_gaps_neg):
            safe += 1
            
        # new case: all except one are ok:
        candidate = None
        if valid_gaps_pos.count(False) == 1:
            candidate = valid_gaps_pos
        if valid_gaps_neg.count(False) == 1:
            candidate = valid_gaps_neg
        if candidate:
            index_false = candidate.index(False)
            #print("INDEX", index_false)
            new_numbers = numbers
            del new_numbers[index_false]
            if _is_safe(new_numbers):
                safe += 1
                continue

            new_numbers = numbers
            del new_numbers[index_false+1]
            if _is_safe(new_numbers):
                print(new_numbers)
                safe += 1
  
    return safe


print(part_2(EXAMPLE))
print(part_2(DATA))