

with open('/Users/kevin/PycharmProjects/advent of code/day_6_input.txt', 'r') as text_document:
    data = text_document.read().split("\n\n")


def part_1():
    sum_counts = 0
    for group in data:
        answer_list = []
        for person in group.splitlines():
            answer_list.extend(x for x in person if x not in answer_list)

        sum_counts += len(answer_list)

    return sum_counts


def part_1_alternative():
    return sum(len(set(  "".join(group.splitlines()) ))
                for group in data)



def part_2():
    sum_counts = 0
    for group in data:
        sum_counts += len(set.intersection(*[ set(x) for x in group.splitlines()]     ) )
    return sum_counts


print("solution part 1: " + str(part_1()))
print("solution part 2: " + str(part_2()))



##### schnappischnap
# def part_1(data):
#     return sum(len(set(group.replace("\n", "") ))
#                for group in data.split("\n\n"))


# def part_2(data):
#     return sum(len(set.intersection(*map(set, group.splitlines())))
#                for group in data.split("\n\n"))


# if __name__ == '__main__':
#     with open('day_06_input.txt', 'r') as f:
#         inp = f.read()
#         print("Part 1 answer: " + str(part_1(inp)))
#         print("Part 2 answer: " + str(part_2(inp)))