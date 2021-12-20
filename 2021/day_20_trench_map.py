import os
path = os.path.dirname(os.path.realpath(__file__)) + "/" + "day_20_input.txt"
data = [line.strip() for line in open(path)]

# data= [
# "..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#",
# "",
# "#..#.",
# "#....",
# "##..#",
# "..#..",
# "..###",
# ]


image_enhancement = data[0]
input_image = data[2:]

from itertools import product
cartesian_product = list(product([-1,0,1],[-1,0,1])) 


def Coords(image):
    return [ (x,y) for x in range(len(image[0])) for y in range(len(image))]

def Adjacent(x,y):
    return [(xd+x,yd+y) for xd, yd in cartesian_product]

def Enlarge(input_image, how_much, s="."):
    enlarge = s*how_much
    enlarge_line = s*(len(input_image[0])+how_much*2)
    input_image = [enlarge + i + enlarge for i in input_image]
    return [enlarge_line]*how_much + input_image + [enlarge_line]*how_much

from copy import deepcopy
def Enhance(input_image):
    # buffer_size = 8
    # enlarge_size = 1
    # buffer = Enlarge(input_image, buffer_size, "h")
    input_image = Enlarge(input_image, 4)
    # input_image = Enlarge(input_image, 7, "h")
    # buffer_size -= enlarge_size

    # for i in input_image:
    #     print(i)
    # input_image = buffer

    coordinates = Coords(input_image)

    output_image = []
    for x, y in coordinates:
        pixels = ""
        for pixelx, pixely in Adjacent(x,y):
            #pixels += buffer[pixelx+buffer_size][pixely+buffer_size]
            try:
                pixels += input_image[pixelx][pixely]
            except:
                pixels += "h"
        output_image += [pixels]

    new_image_pixels = []
    for px in output_image:
        binary = px.replace("#", "1").replace(".","0")
        if "h" in binary:
            new_pixel = "h"
        else:
            value = int(binary,2)
            new_pixel = image_enhancement[value]
        new_image_pixels.append(new_pixel)

    input_image = [list(i) for i in input_image]
    for count, xy in enumerate(coordinates):
        x, y = xy[0], xy[1]
        input_image[x][y] = new_image_pixels[count]

    print("IMAGE:")
    for count, i in enumerate(input_image):
        input_image[count] = "".join(i)
        print(input_image[count])

    return input_image

input_image = Enhance(input_image)
input_image = Enhance(input_image)

input_image = input_image[6:-6]
input_image = [line[6:-6] for line in input_image]

print("PART 1: ", sum([1 for line in input_image for pixel in line if pixel == "#"]))

