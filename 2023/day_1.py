
import re
import os, sys
path = os.path.dirname(os.path.realpath(__file__)) 
with open(path + '/day_1_input.txt', 'r') as text_file: 
    DATA = text_file.read().splitlines() 


EXAMPLE = [
"1abc2",
"pqr3stu8vwx",
"a1b2c3d4e5f",
"treb7uchet",
]


def parse_first_last_digit(elf_writing):
    digits = re.findall(r'\d', elf_writing)
    number = digits[0]+digits[-1]
    return int(number)
    

def get_elf_calibration(input):
    return sum([parse_first_last_digit(elf_writing) for elf_writing in input])

print (f"Example: {get_elf_calibration(EXAMPLE)}")
print (f"part 1: {get_elf_calibration(DATA)}")



EXAMPLE2 = [
"two1nine",
"eightwothree",
"abcone2threexyz",
"xtwone3four",
"4nineeightseven2",
"zoneight234",
"7pqrstsixteen",
]


LETTER_NUMS = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
]


def convert_if_spelled(digit_or_letter_num):
    if digit_or_letter_num in LETTER_NUMS:
        return str(LETTER_NUMS.index(digit_or_letter_num) + 1)
    else:
        return digit_or_letter_num


def convert_spelled_digits(elf_writing):
    regex_pattern = r'(?=(\d|'+'|'.join(LETTER_NUMS) +'))'
    find_digits_spelled_and_real = re.findall(regex_pattern, elf_writing)
    converted_digits = [convert_if_spelled(spelled_digit) for spelled_digit in find_digits_spelled_and_real]
    return ''.join(converted_digits)


def part2(input):
    converted_elf_writing = [convert_spelled_digits(elf_writing) for elf_writing in input]
    return get_elf_calibration(converted_elf_writing)


print(part2(EXAMPLE2))
print(part2(DATA))