import os, sys
path = os.path.dirname(os.path.realpath(__file__)) 
with open(path + '/day_2_input.txt', 'r') as text_file: 

    data = text_file.read().splitlines() 



data = [
"forward 5",
"down 5",
"forward 8",
"up 3",
"down 8",
"forward 2",
]





def read_command(command):
    how_much = int(command.split()[1])
    command = command.split()[0]
    rules = {"forward": (how_much,0), "up": (0, -how_much), "down": (0, how_much)}
    return rules[command]


def part_1():
    instructions = [read_command(command) for command in data]
    print ("Part 1 solution: ")
    print(sum([instruction[0] for instruction in instructions]) * sum([instruction[1] for instruction in instructions]))

part_1()





def read_command_aim(command):
    global aim
    how_much = int(command.split()[1])
    command = command.split()[0]
    rules = {"forward": (how_much, how_much * aim, 0), "up": (0, 0, -how_much), "down": (0,0, how_much)}
    aim += rules[command][2]
    return (rules[command][0], rules[command][1])

def part_2():
    global aim
    aim = 0
    instructions = [read_command_aim(command) for command in data]
    print ("Part 2 solution: ")
    print(sum([instruction[0] for instruction in instructions]) * sum([instruction[1] for instruction in instructions]))

part_2()