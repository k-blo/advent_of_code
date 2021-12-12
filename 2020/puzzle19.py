
    
# def Rulecheck(message, rule_number=0):
#     if message == "":
#         return False

#     rule = rules[rule_number]
#     if '"' in rule:
#         rule = rule[1]

#         if message == rule:
#             return True
#         elif message[0] == rule:
#             return message[1:]
#         return False

#     else:
#         or_rules = rule.split('|')
#         any_list = []
#         store_message = message

#         for rule in or_rules:
#             message = store_message
#             rule = rule.split()
            
#             for number in rule:
#                 message = Rulecheck(message, rule_number=int(number))

#                 if message == False or message == True:
#                     break

#             if isinstance(message, str):
#                 return message

#             any_list.append(message)

#         return any(any_list)



import os, sys
path = os.path.dirname(os.path.realpath(__file__)) 
with open(path + '/day_19_input.txt', 'r') as text_file: 

    data = text_file.read().splitlines()





messages = []
from collections import defaultdict
rules = defaultdict(int)

for line in data:
    if ("a" or "b") and not ":" in line:
        messages.append(line)

    if ":" in line:
        splitted = line.split(": ")
        number = int(splitted[0])
        rule = splitted[1]
        rules[number] = rule


def Rulecheck2(message, rule_number=0):
    global recursion_killer
    if message == "":
        return False

    rule = rules[rule_number]
    if '"' in rule:
        rule = rule[1]

        if message == rule:
            return "LAST"
        elif message[0] == rule:
            return message[1:]
        return False

    else:
        or_rules = rule.split('|')
        any_list = []
        store_message = message

        for rule in or_rules:
            message = store_message
            rule = rule.split()
            
            for number in rule:
                if message == "RECURSION":
                    return False
                message = Rulecheck2(message, rule_number=int(number))

                if message == False or message == True:
                    break
                if message == "LAST":
                    message = True
                    recursion_killer += 1
                    if recursion_killer > 1:
                        return "RECURSION"
                    break

            if isinstance(message, str):
                return message
                

            any_list.append(message)
        return any(any_list)

recursion_killer = -999999
print("PART 1:")
print(sum([1 for message in messages if Rulecheck2(message) == True]))

def part_2():
    rules[8] = "42 | 42 8"
    rules[11] = "42 31 | 42 11 31"
    global recursion_killer
    count = 0
    for message in messages:
        recursion_killer = 0
        if Rulecheck2(message) == True:
            recursion_killer = 0
            count += 1

    print("PART 2:")
    print (count)

part_2()



### a more elegant solution (same direction though, without regex) found on reddit:

#given string s and list of rules seq is there a way to produce s using seq?
def test(s,seq):
    if s == '' or seq == []:
        return s == '' and seq == [] # if both are empty, True. If only one, False.
    
    r = rules[seq[0]]
    if '"' in r:
        if s[0] in r:
            return test(s[1:], seq[1:]) # strip first character
        else:
            return False # wrong first character
    else:
        return any(test(s, t + seq[1:]) for t in r) # expand first term

def parse_rule(s):
    n,e = s.split(": ")
    if '"' not in e:
        e = [[int(r) for r in t.split()] for t in e.split("|")]
    return (int(n),e)

rule_text, messages = [x.splitlines() for x in open(path + '/day_19_input.txt', 'r').read().split("\n\n")]
rules = dict(parse_rule(s) for s in rule_text)            
print("Part 1:", sum(test(m,[0]) for m in messages))       

rule_text += ["8: 42 | 42 8","11: 42 31 | 42 11 31"]
rules = dict(parse_rule(s) for s in rule_text)
print("Part 2:", sum(test(m,[0]) for m in messages)) 