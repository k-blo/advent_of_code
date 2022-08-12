import os
path = os.path.dirname(os.path.realpath(__file__)) + "/" + "day_22_input.txt"
data = [line.strip() for line in open(path)]


data = [
"on x=10..12,y=10..12,z=10..12",
"on x=11..13,y=11..13,z=11..13",
"off x=9..11,y=9..11,z=9..11",
"on x=10..10,y=10..10,z=10..10",
]

# data = [
# "on x=-20..26,y=-36..17,z=-47..7",
# "on x=-20..33,y=-21..23,z=-26..28",
# "on x=-22..28,y=-29..23,z=-38..16",
# "on x=-46..7,y=-6..46,z=-50..-1",
# "on x=-49..1,y=-3..46,z=-24..28",
# "on x=2..47,y=-22..22,z=-23..27",
# "on x=-27..23,y=-28..26,z=-21..29",
# "on x=-39..5,y=-6..47,z=-3..44",
# "on x=-30..21,y=-8..43,z=-13..34",
# "on x=-22..26,y=-27..20,z=-29..19",
# "off x=-48..-32,y=26..41,z=-47..-37",
# "on x=-12..35,y=6..50,z=-50..-2",
# "off x=-48..-32,y=-32..-16,z=-15..-5",
# "on x=-18..26,y=-33..15,z=-7..46",
# "off x=-40..-22,y=-38..-28,z=23..41",
# "on x=-16..35,y=-41..10,z=-47..6",
# "off x=-32..-23,y=11..30,z=-14..3",
# "on x=-49..-5,y=-3..45,z=-29..18",
# "off x=18..30,y=-20..-8,z=-3..13",
# "on x=-41..9,y=-7..43,z=-33..15",
# "on x=-54112..-39298,y=-85059..-49293,z=-27449..7877",
# "on x=967..23432,y=45373..81175,z=27513..53682",
# ]

def flatten(nested_list):
    return [val for sublist in nested_list for val in sublist]

Flatten = lambda nested_list : [val for sublist in nested_list for val in sublist]


from itertools import product

def part_1():
    on_cubes = set()
    for reboot_step in data:
        on_or_off, cube_range = reboot_step.split()
        x,y,z = cube_range.split(",")

        ranges = [tuple(int(i) for i in range_str.split("=")[1].split("..")) for range_str in [x,y,z]]
        x,y,z = ranges[0], ranges[1], ranges[2]
        print(ranges)
        if not any([True for i in Flatten(ranges) if i > 50 or i < -50]):
            cubes = [[i for i in range(c[0],c[1]+1)] for c in [x,y,z]]
            c, *d = cubes
            cubes = list(product(c, *d))

            if "on" == on_or_off:
                on_cubes.update(cubes)
            elif "off" == on_or_off:
                on_cubes.difference_update(cubes)

    print("Part 1:", len(on_cubes))

part_1()



def Add_Cube_Data(ranger,c, cube_data):
    low_new, high_new = ranger[0], ranger[1]
    for count, ranger2 in enumerate(cube_data[c]):
        low, high = ranger2[0], ranger2[1]

        ### check if there is any overlap
        if low <= high_new <= high or low <= low_new <= high:
            ### if so, extend the range
            new_range = (min(low, low_new), max(high, high_new))
            cube_data[c][count] = new_range 
            return cube_data 
    cube_data[c].append(ranger)
    return cube_data 

def Remove_Cube_Data(ranger,c, cube_data):
    low_new, high_new = ranger[0], ranger[1]
    for count, ranger2 in enumerate(cube_data[c]):
        low, high = ranger2[0], ranger2[1]
        ### check if there is any overlap
        if low <= high_new <= high or low <= low_new <= high:
            ### if so, check if identical:
            if low == low_new and high == high_new:
                cube_data[c].remove(ranger2)

            ### or if within:
            if low < low_new and high > high_new:
                cube_data[c].remove(ranger2)
                cube_data[c].append(low,low_new-1)
                cube_data[c].append(high,high_new-1)

            ### or if lower overlap:
            if low > low_new and high > high_new:
                cube_data[c][count] = (high_new+1, high)
            ### or if higher overlap:
            if low < low_new and high < high_new:
                cube_data[c][count] = (low, low_new-1)

    return cube_data 


def part_2():
    cube_data = {
        "x":[], 
        "y":[],
        "z":[],
    }

    for reboot_step in data:
        on_or_off, cube_range = reboot_step.split()
        x,y,z = cube_range.split(",")

        ranges = [tuple(int(i) for i in range_str.split("=")[1].split("..")) for range_str in [x,y,z]]
        x,y,z = ranges[0], ranges[1], ranges[2]
        print(ranges)
        if not any([True for i in Flatten(ranges) if i > 50 or i < -50]):

            if "on" == on_or_off:
                cube_data = Add_Cube_Data(x,"x", cube_data)
                cube_data = Add_Cube_Data(y,"y", cube_data)
                cube_data = Add_Cube_Data(z,"z", cube_data)

            elif "off" == on_or_off:
                cube_data = Remove_Cube_Data(x,"x", cube_data)
                cube_data = Remove_Cube_Data(y,"y", cube_data)
                cube_data = Remove_Cube_Data(z,"z", cube_data)

        print(cube_data)
    print("Part 2:", cube_data)
    # [cubefor cube_ranges in cube_data.values()]

part_2()







            