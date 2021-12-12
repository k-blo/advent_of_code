with open('/Users/kevin/PycharmProjects/advent of code/day_8_input.txt', 'r') as text_file:
    data = text_file.read().splitlines()

def Change_Line(line_string):
    changed_line_string = "why do I need this?"
    if "jmp" in line_string:
        changed_line_string = line_string.replace("jmp", "nop")
    if "nop" in line_string:
        changed_line_string = line_string.replace("nop", "jmp")
        
    return changed_line_string



def execute(line_string, accumulator, line_number, change_line):

    if line_number == change_line:
        line_string = Change_Line(line_string)

    if "nop" in line_string:
        line_number += 1
    if "jmp" in line_string:
        line_number += int(line_string.split()[1])
    if "acc" in line_string:
        accumulator += int(line_string.split()[1])
        line_number += 1
    
    return line_string, accumulator, line_number

def one_loop(change_line = None):
    line_number = 0
    executed_lines = []
    accumulator = 0
    is_infinite = False

    while True:    
        if line_number in executed_lines:
            is_infinite = "is_infinite"
            break
        # if line_number == len(data)+1:
        #     is_infinite = "not_infinite!"
        #     break

        executed_lines.append(line_number)
        try:
            line_string, accumulator, line_number = execute(data[line_number], accumulator, line_number, change_line)
        except:
            is_infinite = "not_infinite!"
            break

    return is_infinite, accumulator

def part_1():
    infinite, accumulator = one_loop()
    return str(accumulator) +" "+ infinite
    

def part_2():
    for change_line in range(0, len(data)+1):
        infinite, accumulator = one_loop(change_line)
        if infinite == "not_infinite!":
            break

    return str(accumulator) + " " + infinite



print ("part 1 solution: " + part_1())

print ("part 2 solution: " + part_2())


