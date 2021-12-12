

data = [
"F10",
"N3",
"F7",
"R90",
"F11",
]


with open('/Users/kevin/Documents/code/advent of code/day_12_input.txt', 'r') as text_file: 
    data = text_file.read().splitlines()



compass = ["N", "E", "S", "W"]



def part1(data):
    ship = {
        "F": "E",
        "E":0,
        "W":0,
        "S":0,
        "N":0,
    }

    for instruction in data:
        direction = instruction[0]
        distance = int(instruction[1:])

        if direction == "F":
            ship[ship["F"]] += distance
        elif "R" in direction or "L" in direction:
            if "L" in direction:
                distance *= -1
            change_course = compass.index(ship["F"]) + int(distance/90)
            ship["F"] = compass[(change_course ) % len(compass)] 
        else:
            ship[direction] += distance
    print (abs(ship["N"] - ship["S"]) + abs(ship["E"] - ship["W"]))
part1(data)




def part2(data):
    ship = {
        "E":0,
        "W":0,
        "S":0,
        "N":0,
    }
    waypoint = {"N":1, "E":10, "S": 0, "W": 0}

    for instruction in data:
        direction = instruction[0]
        distance = int(instruction[1:])

        if direction == "F":
            for direction in waypoint:
                ship[direction] += distance * waypoint[direction]

        elif "R" in direction or "L" in direction:
            if "L" in direction:
                distance *= -1

            new_waypoint = {"N":0, "E":0, "S": 0, "W": 0}
            for heading in waypoint:
                change_course = compass.index(heading) + int(distance/90)
                new_waypoint[compass[(change_course ) % len(compass)] ] = waypoint[heading]
            waypoint = new_waypoint
        else:
            waypoint[direction] += distance
    print (abs(ship["N"] - ship["S"]) + abs(ship["E"] - ship["W"]))

part2(data)




# pro way
from collections import namedtuple


Point = namedtuple("Point", "x y")


def part_1(data):
    directions = {"N": Point(0, -1), "E": Point(1, 0),
                  "S": Point(0, 1), "W": Point(-1, 0)}

    position = Point(0, 0)
    heading = Point(1, 0)

    for line in data:
        instruction, amount = line[0], int(line[1:])
        if instruction in directions:
            position = Point(position.x + directions[instruction].x * amount,
                             position.y + directions[instruction].y * amount)
        elif instruction == "F":
            position = Point(position.x + heading.x * amount,
                             position.y + heading.y * amount)
        else:
            if instruction == "L":
                amount = 360 - amount

            if amount == 90:
                heading = Point(-heading.y, heading.x)
            elif amount == 270:
                heading = Point(heading.y, -heading.x)
            elif amount == 180:
                heading = Point(-heading.x, -heading.y)

    return abs(position.x) + abs(position.y)


def part_2(data):
    directions = {"N": Point(0, -1), "E": Point(1, 0),
                  "S": Point(0, 1), "W": Point(-1, 0)}
    
    position = Point(0, 0)
    waypoint = Point(10, -1)

    for line in data:
        instruction, amount = line[0], int(line[1:])

        if instruction in directions:
            waypoint = Point(waypoint.x + directions[instruction].x * amount,
                             waypoint.y + directions[instruction].y * amount)
        elif instruction == "F":
            position = Point(position.x + waypoint.x * amount,
                             position.y + waypoint.y * amount)
        else:
            if instruction == "L":
                amount = 360 - amount

            if amount == 90:
                waypoint = Point(-waypoint.y, waypoint.x)
            elif amount == 270:
                waypoint = Point(waypoint.y, -waypoint.x)
            elif amount == 180:
                waypoint = Point(-waypoint.x, -waypoint.y)

    return abs(position.x) + abs(position.y)


if __name__ == '__main__':
    with open('/Users/kevin/Documents/code/advent of code/day_12_input.txt', 'r') as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))


