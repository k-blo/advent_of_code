




with open('/Users/kevin/Documents/code/advent of code/day_14_input.txt', 'r') as text_file: 
    data = text_file.read().splitlines()


# data = ["mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
# "mem[8] = 11",
# "mem[7] = 101",
# "mem[8] = 0",]


def binary_to_decimal(binary_string):
    return int(binary_string,2)

def decimal_to_binary(integer):
    return bin(integer)[2:].zfill(36)

def part1(data):
    mem = {}
    for line in data:
        if "mask" in line:
            mask = line.split("= ")[1]
        else:
            exec(line)
            adress = int(line.split("[")[1].split("]")[0])
            value = list(decimal_to_binary(mem[adress]))
            for count, bit in enumerate(mask):
                if bit != "X":
                    value[count] = bit
            value = "".join(value)
            mem[adress] = binary_to_decimal(value)

    print(sum([mem[adress] for adress in mem]))

part1(data)


# data = [
# "mask = 000000000000000000000000000000X1001X",
# "mem[42] = 100",
# "mask = 00000000000000000000000000000000X0XX",
# "mem[26] = 1",]

from itertools import product
def part2(data):
    mem = {}
    for line in data:
        if "mask" in line:
            mask = line.split("= ")[1]
        else:
            adress = int(line.split("[")[1].split("]")[0])
            value = int(line.split(" = ")[1])

            adress = list(decimal_to_binary(adress))
            for count, bit in enumerate(mask):
                if bit != "0":
                    adress[count] = bit
            adress = "".join(adress)
            floatables_count = adress.count("X")

            for floatable_combination in product("01", repeat=floatables_count):
                count = 0
                adress_variation = []
                for bit in adress:
                    if bit == "X":
                        adress_variation.append(floatable_combination[count])
                        count += 1
                    else:
                        adress_variation.append(bit)
                adress_variation = "".join(adress_variation)
                mem[binary_to_decimal(adress_variation)] = value
                    
    print(sum([mem[adress] for adress in mem]))

part2(data)



# cartesian_product = product("01", repeat=2)
# for i in list(cartesian_product): 
#     print (i) 



### pro way

import itertools
import re
def part_1(data):
    values = dict()
    for line in data:
        if line.startswith("mask"):
            mask = line.rstrip()[7:]
        else:
            address, value = re.findall(r"(\d+)", line)
            value = bin(int(value))[2:].zfill(36)
            result = "".join(m_bit if m_bit != "X" else v_bit
                             for m_bit, v_bit in zip(mask, value))
            values[address] = int(result, 2)

    return sum(v for v in values.values())


def part_2(data):
    values = dict()
    for line in data:
        if line.startswith("mask"):
            mask = line.rstrip()[7:]
        else:
            address, value = re.findall(r"(\d+)", line)
            address = bin(int(address))[2:].zfill(36)

            result = "".join(m_bit if m_bit != "0" else a_bit
                             for m_bit, a_bit in zip(mask, address)).split("X")

            for floating in itertools.product("01", repeat=len(result)-1):
                address = ""
                for r_bit, f_bit in itertools.zip_longest(result, floating, fillvalue=""):
                    address += r_bit + f_bit
                values[address] = int(value)

    return sum(v for v in values.values())


if __name__ == '__main__':
    with open('/Users/kevin/Documents/code/advent of code/day_14_input.txt', 'r') as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))