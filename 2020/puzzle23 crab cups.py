





def part1(cups, moves=100):

    cups = [int(cup) for cup in cups] 
        
    for i in range(moves):
        three_cups = cups[1:4]
        cups = [cups[0]] + cups[4:]
        destination_cup = cups[0] - 1

        while destination_cup not in cups:
            destination_cup -= 1
            if destination_cup < min(cups):
                destination_cup = max(cups)
  

        position = cups.index(destination_cup)
        cups = cups[1:position] + [destination_cup] + three_cups + cups[position+1:] + [cups[0]]

    one_position = cups.index(1)

    cups = cups[one_position+1:] + cups[:one_position]
    print ( "PART 1: " + "".join([str(cup) for cup in cups]))

part1("962713854")




def part2(cups, moves=10_000_000):
    cups = [int(cup) for cup in cups] + list(range(10, 1_000_001))
    largest, smallest = max(cups), min(cups)
    next_item_dict = dict(zip(cups, cups[1:] + [cups[0]]))
    current = cups[0]
    
    for i in range(moves):
        destination_cup = current - 1
        three_cups = [next_item_dict[current]]
        three_cups.append(next_item_dict[three_cups[0]])
        three_cups.append(next_item_dict[three_cups[-1]])

        while destination_cup in three_cups +[0]:
            destination_cup -= 1
            if destination_cup < smallest:
                destination_cup = largest
  
        next_item_dict[current] = next_item_dict[three_cups[-1]]
        next_item_dict[three_cups[-1]] = next_item_dict[destination_cup]
        next_item_dict[destination_cup] = three_cups[0]
        current = next_item_dict[current]

        if i % 1_000_000 == 0:
            print (i)

    after_one = next_item_dict[1]
    and_next = next_item_dict[after_one]
    print ( "PART 2: " + str(after_one * and_next))

part2("962713854")



# def fast_dic(cups, steps):  # non-rotated dictionary:  {cup: nextcup, ... }
#     current = cups[0]
#     mn, mx = min(cups), max(cups)
#     carousel = dict(zip(cups, cups[1:] + [cups[0]]))

#     for _ in range(steps):
#         xyz = [carousel[current]]
#         xyz.append(carousel[xyz[0]])
#         xyz.append(carousel[xyz[-1]])
#         dest = current - 1
#         while dest < mn or dest in xyz:
#             dest -= 1
#             if dest < mn:
#                 dest = mx
#         carousel[current] = carousel[xyz[-1]]
#         carousel[xyz[-1]] = carousel[dest]
#         carousel[dest] = xyz[0]
#         current = carousel[current]
#     return carousel


# cups = fast_dic(list(map(int, (list("962713854")))) + list(range(9+1, 1_000_001)), 10_000_000)
# c1 = cups[1]
# c2 = cups[c1]
# print('Part Two:', c1 * c2)