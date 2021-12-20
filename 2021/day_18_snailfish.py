import os
path = os.path.dirname(os.path.realpath(__file__)) + "/" + "day_18_input.txt"
data = [line.strip() for line in open(path)]

# data= [
# "[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]",
# "[[[5,[2,8]],4],[5,[[9,9],0]]]",
# "[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]",
# "[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]",
# "[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]",
# "[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]",
# "[[[[5,4],[7,7]],8],[[8,3],8]]",
# "[[9,3],[[9,9],[6,[4,9]]]]",
# "[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]",
# "[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]",
# ]


data = [eval(line) for line in data]



Is_list_with_ints_only = lambda pair : all([False for i in pair if not isinstance(i, int)] + [True])


import math
def Reduce_Recursion(pair, mode, nested=0):
    global has_exploded_already ## also marks splits
    if nested == 0:
        has_exploded_already = False

    #### explode
    explode_conditions = [mode == "explode", not has_exploded_already, nested == 4, isinstance(pair, list) and Is_list_with_ints_only(pair)]
    if all(explode_conditions):
        has_exploded_already = True 
        return "explosion:" + str(pair[0]) + ":" + str(pair[1])  + ">"  

    if isinstance(pair, int):
        #### split
        if pair >= 10 and not has_exploded_already and mode == "split":
            has_exploded_already = True
            pair = [ int(pair*0.5), int(math.ceil(pair*0.5))  ]
        return pair

    return  [Reduce_Recursion(pair[0], mode, nested+1), Reduce_Recursion(pair[1], mode, nested+1)]

def Reduce(expression):
    s = str(Reduce_Recursion(expression, "explode"))
    if "explosion" in s:
        start, end = s.find("explosion"), s.find(">")
        explosion = s[start:end].split(":")[1:]
        left, right = int(explosion[0]), int(explosion[1])
        s = s[:start-1] + "0" + s[end+2:]

        ### distribute explosive remnants to the left and right
        def Search_Int_in_String(s, i, side, remnant):
            nums = [str(i) for i in range(10)]
            if s[i] in nums:
                if s[i+1] in nums and side == "right":
                    return s[:i] + str(remnant + int(s[i:i+2])) + s[i+2:]
                elif s[i-1] in nums and side == "left":
                    return s[:i-1] + str(remnant + int(s[i-1:i+1])) + s[i+1:]
                else:
                    return s[:i] + str(remnant + int(s[i])) + s[i+1:]

        for i in range(start, len(s)):
            if Search_Int_in_String(s, i, "right", right):
                s = Search_Int_in_String(s, i, "right", right)
                break

        for i in range(start-2, -1, -1):
            if Search_Int_in_String(s, i, "left", left):
                s = Search_Int_in_String(s, i, "left", left)
                break
    else:
        s = str(Reduce_Recursion(expression, "split"))

    return eval(s)


def Reduce_Until_Done(previous_reduce):
    new_reduce = None
    while True:
        new_reduce = Reduce(previous_reduce)
        if previous_reduce == new_reduce:
            return new_reduce
        previous_reduce = new_reduce
    
    


def Magnitude(list_of_lists):
    get_sum = []
    for i in list_of_lists:
        if isinstance(i, int):
            get_sum.append(i)
        if isinstance(i, list):
            get_sum.append(Magnitude(i) )

    get_sum[0] *= 3
    get_sum[1] *= 2
    return sum(get_sum)
            




def Final_Sum(list_of_additions):
    first = list_of_additions[0]
    for addition in list_of_additions[1:]:
        first = Reduce_Until_Done(  [first, addition]  )
    return first



print("Part 1:", Magnitude(Final_Sum(data)))

from itertools import combinations, permutations
print("Part 2:", max([Magnitude(Reduce_Until_Done(  [x, y]  )) for x,y in list(permutations(data,2))]))
    



