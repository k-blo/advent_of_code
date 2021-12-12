

import os, sys
path = os.path.dirname(os.path.realpath(__file__)) 
with open(path + '/day_18_input.txt', 'r') as text_file: 

    data = text_file.read().splitlines()




def Get_Inner_Parenthesis(calc_string, part2=False):
    for count, character in enumerate(calc_string):
        if character == "(":
            start = count+1
        elif character == ")":
            end = count
            break    
    value = Solve_Prevalence(calc_string[start:end])
    if part2:
        value = Solve_Prevalence_2(calc_string[start:end])

    return calc_string[:start-1] + str(value) + calc_string[end+1:]

def Solve_Prevalence(calc_string):
    calc_list = calc_string.split()
    result = int(calc_list[0])
    for i, character in enumerate(calc_list[1:],1):
        if character == "+":
            result += int(calc_list[i+1])
        if character == "*":
            result *= int(calc_list[i+1])
    return result

def Calculate(calc_string, part2=False):
    while "(" in calc_string:
        calc_string = Get_Inner_Parenthesis(calc_string, part2)
    if part2:
        return Solve_Prevalence_2(calc_string)
    return Solve_Prevalence(calc_string)

print ("part 1: " + str( sum([Calculate(line) for line in data])  ))




from math import prod

def Solve_Prevalence_2(calc_string):
    calc_list = calc_string.split()
    while "+" in calc_list:
        i = calc_list.index("+")
        summe = int(calc_list[i-1]) + int(calc_list[i+1])
        del calc_list[i+1]
        del calc_list[i]
        del calc_list[i-1]
        calc_list.insert(i-1, summe)
    return prod([int(i) for i in calc_list if i != "*"])


print ("part 2: " + str( sum([Calculate(line, True) for line in data])  ))





## pro way
# from math import prod


# def part_1(data):
#     def calculate(expr):
#         while "(" in expr:
#             start = expr.index("(")
#             for i, c in enumerate(expr[start:], start=start):
#                 if c == "(":
#                     start = i
#                 elif c == ")":
#                     value = str(calculate(expr[start+1:i]))
#                     expr = expr[:start] + [value] + expr[i+1:]
#                     break
        
#         total = int(expr[0])
#         for op, i in zip(expr[1::2], expr[2::2]):
#             if op == "+":
#                 total += int(i)
#             elif op == "*":
#                 total *= int(i)
#         return total
    
#     return sum(calculate(line.replace("(", "( ").replace(")", " )").split())
#                for line in data) 


# def part_2(data):
#     def calculate(expr):
#         while "(" in expr:
#             start = expr.index("(")
#             for i, c in enumerate(expr[start:], start=start):
#                 if c == "(":
#                     start = i
#                 elif c == ")":
#                     value = str(calculate(expr[start+1:i]))
#                     expr = expr[:start] + [value] + expr[i+1:]
#                     break

#         while "+" in expr:
#             i = expr.index("+")
#             value = str(int(expr[i-1]) + int(expr[i+1]))
#             expr = expr[:i-1] + [value] + expr[i+2:]

#         return prod(int(c) for c in expr[::2])

#     return sum(calculate(line.replace("(", "( ").replace(")", " )").split())
#                for line in data)