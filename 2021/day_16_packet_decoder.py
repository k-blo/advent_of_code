import os

path = os.path.dirname(os.path.realpath(__file__)) + "/" + "day_16_input.txt"
data = [line.strip() for line in open(path)]


def hxbin(hex_string):  # hex to binary
    return bin(int(hex_string, 16))[2:].zfill(
        len(hex_string) * 4)  # zfill makes sure the left trailing 0s are not cut off


def dez(bin_input):  # binary to decimal
    return int(bin_input, 2)


def Type4(remaining_bits, binary_str=""):
    bits4 = remaining_bits[1:5]
    if remaining_bits[0] == "1":  # 1 means the package continues
        remaining_bits = remaining_bits[5:]
        alibistring = Type4(remaining_bits, binary_str=binary_str + bits4)
        return alibistring  # this is apparently required for the recursive function to return not None
    else:  # 0 means the package ends
        return dez(binary_str + bits4), remaining_bits[5:]


import math


def calc_values(id, values):
    if id == 0:
        return sum(values)
    if id == 1:
        return math.prod(values)
    if id == 2:
        return min(values)
    if id == 3:
        return max(values)
    if id == 5:
        if values[0] > values[1]:
            return 1
        else:
            return 0
    if id == 6:
        if values[0] < values[1]:
            return 1
        else:
            return 0
    if id == 7:
        if values[0] == values[1]:
            return 1
        else:
            return 0


def Decode(binary):  # a long binary string
    global versions

    packet_version = dez(binary[:3])  # first 3 bits are packet version
    packet_type_id = dez(binary[3:6])  # next 3 bits are packet type

    remaining_bits = binary[6:]  # packet info can be discarded

    versions.append(packet_version)  # required for part 1: summing up packet versions contained in binary

    if packet_type_id == 4:  # type 4s contain literal values, encoded in 4 bits
        return Type4(remaining_bits)

    else:
        length_type_ID = remaining_bits[0]  # length is encoded in bit-length (0) or number of packages (1)
        remaining_bits = remaining_bits[1:]  # can be cut off

        if length_type_ID == "0":  # here we know the length of the binary string containing the sub-packets
            length = 15  # length of the binary saying how many subpackets we get
            sub_packet_size = dez(remaining_bits[:length])
            remaining_bits = remaining_bits[length:]
            sub_packet = remaining_bits[:sub_packet_size]

            remaining_bits = remaining_bits[sub_packet_size:]

            values = []
            while len(sub_packet):
                value, sub_packet = Decode(sub_packet)
                values.append(value)

        elif length_type_ID == "1":
            length = 11
            sub_packet_count = dez(remaining_bits[:length])

            values = []
            remaining_bits = remaining_bits[length:]
            for i in range(sub_packet_count):
                value, remaining_bits = Decode(remaining_bits)
                values += [value]

        return calc_values(packet_type_id, values), remaining_bits


def part1_2(hex_string):
    global versions
    versions = []
    binary = hxbin(hex_string)
    value, remaining_bits = Decode(binary)

    print("PART 1:", sum(versions))
    print("PART 2:", value)


part1_2(data[0])

# binary = hxbin("C200B40A82")
# print(binary)
# print(Decode(binary))
