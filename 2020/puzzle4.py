

with open('/Users/kevin/PycharmProjects/advent of code/day_4_input.txt', 'r') as text_file:
    data = text_file.read().split("\n\n")


required_fields = ["byr","iyr", "eyr", "hgt", "hcl", "ecl","pid",]
invalid_passports = 0
invalid_pw_list = []

for data_chunk in data:
    for field in required_fields:
        if field not in data_chunk:
            if data_chunk not in invalid_pw_list:
                invalid_pw_list.append(data_chunk)
            continue

print ("solution part 1: " + str(len(data) - len(invalid_pw_list)) )





valid_list = []
for passport in data:
    if passport not in invalid_pw_list:
        valid_list.append(passport)

invalid_part2 = []

def four_digits_pass(string, min, max):
    byr = passport.split(string)
    byr = byr[1][0:4]
    if min <= int(byr) <= max: # if 10000 <= number <= 30000:
        return True
    else:
        return False


def invalid(passport):
    if passport not in invalid_part2:
        invalid_part2.append(passport)

for passport in valid_list:
    if not (four_digits_pass("byr:", 1920, 2002) and four_digits_pass("iyr:", 2010, 2020) and four_digits_pass("eyr:", 2020, 2030)):
        invalid(passport)

    hgt = passport.split("hgt:")
    hgt_cm = hgt[1][0:5]
    hgt_in = hgt[1][0:4]

    if hgt_cm[-2:] == "cm":
        if not 150 <= int(hgt_cm.split("cm")[0]) <= 193:
            invalid(passport)
    
    elif hgt_in[-2:] == "in":
        if not 59 <= int(hgt_in.split("in")[0]) <= 76:
            invalid(passport)
    
    else:
        invalid(passport)



    hcl = passport.split("hcl:")
    hcl = hcl[1][0:7]


    if not hcl[0] == "#":
        invalid(passport)

    import string
    a_f = string.ascii_lowercase[0:6]
    allowed_numbers = list(map(str, range(0, 10)))

    for character in hcl[1:6]:
        if not (character in list(a_f) or character in allowed_numbers):
            invalid(passport)
    
    

    ecl = passport.split("ecl:")
    ecl = ecl[1][0:3]
    allowed_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth",]

    if ecl not in allowed_colors:
        invalid(passport)
    
    pid = passport.split("pid:")
    pid = pid[1].split()[0]

    if len(pid) != 9:
        invalid(passport)


    for character in pid:
        if not character in allowed_numbers:
            invalid(passport)

print  ("solution part 2: " + str(len(data) - len(invalid_pw_list)- len(invalid_part2))   ) 









##### aaand that's how the pros do it:
#### https://github.com/schnappischnap/advent_of_code_2020/blob/master/day_04_passport_processing.py

import re


def part_1(data):
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    return sum(all(field in passport for field in fields)
               for passport in data.split("\n\n"))


def part_2(data):
    def is_valid(passport):
        return (1920 <= int(passport.get("byr", 0)) <= 2002 and
                2010 <= int(passport.get("iyr", 0)) <= 2020 and
                2020 <= int(passport.get("eyr", 0)) <= 2030 and
                ((passport.get("hgt", "").endswith("cm") and
                  150 <= int(passport["hgt"][:-2]) <= 193) or
                 (passport.get("hgt", "").endswith("in") and
                  59 <= int(passport["hgt"][:-2]) <= 76)) and
                passport.get("hcl", "").startswith("#") and len(passport["hcl"]) == 7 and
                passport.get("ecl", "") in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"] and
                len(passport.get("pid", "")) == 9)

    passports = [dict(field.split(":") for field in re.split(r"\s", passport))
                 for passport in data.split("\n\n")]

    return sum(is_valid(passport) for passport in passports)
    

if __name__ == '__main__':
    with open('day_04_input.txt', 'r') as f:
        inp = f.read()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))


