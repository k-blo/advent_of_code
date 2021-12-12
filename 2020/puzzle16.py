

import os, sys
path = os.path.dirname(os.path.realpath(__file__)) 
with open(path + '/day_16_input.txt', 'r') as text_file: 

    data = text_file.read().splitlines()







def is_ticket_valid(ticket):
    fields= ticket.split(",")
    for field in fields:
        if int(field) not in valid_numbers:
            return (False, field)
    return (True,ticket)

def rulebook():
    rule_book = {}
    for rule in rules:
        rule_numbers = []
        ranges = rule.split(": ")[1].split(" or ")
        for rang in ranges:
            int_strings = rang.split("-")
            for integer1, integer2 in [(int(int_strings[0]), int(int_strings[1]))]:
                rule_numbers += [i for i in range(integer1,integer2+1)]

        rule_book[rule.split(": ")[0]] = rule_numbers
    return rule_book

rules = data[:data.index("your ticket:")-1]
nearby_tickets = data[data.index("nearby tickets:")+1:]
rule_book = rulebook()
valid_numbers = [item for sublist in rule_book.values() for item in sublist]
my_ticket = "191,89,73,139,71,103,109,53,97,179,59,67,79,101,113,157,61,107,181,137"

def part1():
    invalid_fields = []
    for ticket in nearby_tickets:
        if not is_ticket_valid(ticket)[0]:
            invalid_fields.append(int(is_ticket_valid(ticket)[1]))
    print (sum(invalid_fields))



part1()


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def subtraction(x,y):
    return [item for item in x if item not in y]

def part2():
    valid_tickets = [my_ticket]
    for ticket in nearby_tickets:
        if is_ticket_valid(ticket)[0]:
            valid_tickets.append(is_ticket_valid(ticket)[1])

    rule_finder_dict = {}
    for i in range(len(rule_book.keys()) ):
        rule_finder_dict[i] = list(rule_book.keys())

    ###### eliminate rules from not fitting fields
    for ticket in valid_tickets:
        fields= ticket.split(",")
        for count, field in enumerate(fields):
            for rule,rule_range in rule_book.items():
                if int(field) not in rule_range and rule in rule_finder_dict[count]:
                    rule_finder_dict[count].remove(rule)

    ##### then eliminate,starting from rules that only have one possible fields
    eliminated_fields = []
    for ordered_by_length_key in sorted(rule_finder_dict, key=lambda k: len(rule_finder_dict[k])):
        only_possible_field = subtraction(rule_finder_dict[ordered_by_length_key], eliminated_fields)
        eliminated_fields.append(only_possible_field[0])
        rule_finder_dict[ordered_by_length_key] = only_possible_field[0]

    #invert keys values
    rule_finder_dict = {value:key for key,value in rule_finder_dict.items()}
    
    departure_fields = []
    for key in rule_finder_dict:
        if "departure" in key:
            field_position = rule_finder_dict[key]
            departure_fields.append( int(my_ticket.split(",")[field_position]) )

    import math
    print(math.prod(departure_fields))


part2()


