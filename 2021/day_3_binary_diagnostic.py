import os, sys
path = os.path.dirname(os.path.realpath(__file__)) 
with open(path + '/day_3_input.txt', 'r') as text_file: 

    data = text_file.read().splitlines() 



# data = [
# "00100",
# "11110",
# "10110",
# "10111",
# "10101",
# "01111",
# "00111",
# "11100",
# "10000",
# "11001",
# "00010",
# "01010",
# ]



def Gamma_Epsilon(zero_one):
    rate = ""
    for i in range(len(data[0])):
        column = [bit_sequence[i] for bit_sequence in data]
        most_common_bit = Counter(column).most_common()[zero_one]
        rate += most_common_bit[0]
    return int(rate,2)

from collections import Counter
def part_1():
    print ("Part 1 solution: ")
    print(Gamma_Epsilon(0) * Gamma_Epsilon(1))
part_1()







def Oxygen_CO2(zero_one, if_equal_choose_this):
    new_data = list(data)

    for i in range(len(data[0])):

        column = [bit_sequence[i] for bit_sequence in new_data]
        count_bits = Counter(column).most_common()
        deciding_bit = count_bits[zero_one][0]

        if count_bits[0] == count_bits[1]: 
            deciding_bit = if_equal_choose_this

        new_data = [number for number in new_data if number[i] == deciding_bit]
        if len(new_data) == 1:
            return int(new_data[0],2)


def part_2():

    print ("Part 2 solution: ")
    print(Oxygen_CO2(0, "1") * Oxygen_CO2(1, "0"))

part_2()