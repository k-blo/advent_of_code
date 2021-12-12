with open('/Users/kevin/Documents/code/advent of code/day_7_input.txt', 'r') as text_document:
    data = text_document.read().splitlines()


# def part_1():
#     bags_containing_gold = []
#     while True:
#         remember_bag_count_after_each_iteration = len(bags_containing_gold)
#         for rule in data:
#             for bag in bags_containing_gold + ["shiny gold"]:
#                 if bag in rule.split("contain")[1]:
#                     if rule.split("bag")[0] not in bags_containing_gold:
#                         bags_containing_gold.append(rule.split("bag")[0])

#         if remember_bag_count_after_each_iteration == len(bags_containing_gold):
#             break
    
#     return len(set(bags_containing_gold))

# print ("part 1 solution: " +  str(part_1())  )

from collections import defaultdict

def part_1_improved():
    all_bags = [rule.split("bags contain")[0] for rule in data]
    
    bag_homes_catalogue = defaultdict(list)
    for rule in data:
        for bag in all_bags:
            if bag in rule.split("bags contain")[1]:
                bag_homes_catalogue[bag].append(rule.split("bags contain")[0])

    bags_containing = set()
    def recursive_homes(bag):
        for bag in bag_homes_catalogue[bag]:
            bags_containing.add(bag)
            recursive_homes(bag)
    recursive_homes("shiny gold ")
    return len(bags_containing)

print (part_1_improved())



def part2():
    bag_contains_what = defaultdict(list)
    for rule in data:
        outer = rule.split(" bags contain")[0]
        contains = rule.split(" bags contain")[1]
        if not "no other" in contains:
            for bag in contains.split(","):
                bag_contains_what[outer].append( (bag[3:].split(" bag")[0], int(bag[1]))  )




    def recursive_bag_count(bag, count, total_count=0):
        total_count += count
        for inner_bag, inner_count in bag_contains_what[bag]:
            total_count += recursive_bag_count(inner_bag, inner_count*count)
        return total_count
    return recursive_bag_count("shiny gold",1) - 1

    ###### above is equivalent to:
    # global total_count
    # total_count = 0
    # def recursive_bag_count(bag, count=0):
    #     global total_count
    #     for inner_bag, inner_count in bag_contains_what[bag]:
    #         total_count -= inner_count * count
    #         recursive_bag_count(inner_bag, inner_count*count) 
    # recursive_bag_count("shiny gold", 1) 
    # return total_count          


print (part2())








from collections import defaultdict
import re


def part_1(data):
    contained_in = defaultdict(list)
    for line in data:
        match = re.findall(r"(\w+ \w+) bag", line)
        for bag in match[1:]:
            contained_in[bag].append(match[0])

    answer = set()
    def r(bag):
        for outer_bag in contained_in[bag]:
            answer.add(outer_bag)
            r(outer_bag)
    r("shiny gold")

    return len(answer)


def part_2(data):
    contains = defaultdict(list)
    for line in data:
        match = re.findall(r"(\d )?(\w+ \w+) bag", line)
        for count, bag in match[1:]:
            if bag != "no other":
                contains[match[0][1]].append((int(count), bag))

    def r(count, bag, total=0):
        total += count
        for inner_count, inner_bag in contains[bag]:
            total += r(inner_count*count, inner_bag)
        return total

    return r(1, "shiny gold") - 1  # Account for the original shiny gold bag


if __name__ == '__main__':
    with open('/Users/kevin/Documents/code/advent of code/day_7_input.txt', 'r') as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))