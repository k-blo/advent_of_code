import os
input = "day_14_input.txt"
path = os.path.dirname(os.path.realpath(__file__)) + "/" + input
data = [line.strip() for line in open(path)]
# data= [
# "NNCB",
# "",
# "CH -> B",
# "HH -> N",
# "CB -> H",
# "NH -> C",
# "HB -> C",
# "HC -> B",
# "HN -> C",
# "NN -> C",
# "BH -> H",
# "NC -> B",
# "NB -> B",
# "BN -> B",
# "BB -> N",
# "BC -> B",
# "CC -> N",
# "CN -> C",
# ]





def part1():
    rules = {}
    for rule in data[2:]:
        pair, insert = rule.split(" -> ")
        rules[pair] = insert

    polymer = data[0]
    for i in range(10):
        to_insert = {}
        for m in range(len(polymer)):
            slice = polymer[m:m+2]
            if slice in rules:
                to_insert[m] = rules[slice]
        last_first = list(to_insert.keys())
        last_first.sort(reverse=True)

        for insert in last_first:
            polymer = polymer[:insert+1] + to_insert[insert] + polymer[insert+1:]

    from collections import Counter

    count = Counter(polymer).most_common()
    most, least = count[0][1], count[-1][1]
    print ("Part 1 solution: ")
    print (most-least)

part1()








def DEI(dict, key, value=1):
    if key in dict:
        dict[key] += value
    else:
        dict[key] = value

def part2():
    rules = { pair: pair[0] + insert + pair[1] 
            for rule in data[2:] 
            for pair, insert in [tuple(rule.split(" -> "))] }

    polymer = data[0]
    molecule_counter = { molecule:polymer.count(molecule) for molecule in polymer }

    pairs = [polymer[m:m+2] for m in range(len(polymer))]
    pair_counter = { pair:polymer.count(pair) for pair in pairs if pair in rules }

    for i in range(40):
        previous_pair_counter = dict(pair_counter)
        for pair, how_many in previous_pair_counter.items():
            new_3 = rules[pair]

            DEI(molecule_counter, new_3[1], how_many)
            DEI(pair_counter, new_3[1:] , how_many)
            DEI(pair_counter, new_3[:2] , how_many)
            pair_counter[pair] -= how_many

    most, least = max(molecule_counter.values()), min(molecule_counter.values())
    print ("Part 2 solution: ")
    print (most-least)

part2()




# some guy on reddit:
# https://old.reddit.com/user/Derp_Derps
#L = open(sys.argv[1]).read().splitlines()
L = data
T = [ L[0][i:i+2] for i in range(len(L[0])-1)]
P = { k:(k[0]+v,v+k[1]) for k,v in [ p.split(' -> ') for p in L[2:]]}
N = { k:T.count(k) for k in P}

def l(I,N,P):
    for i in range(I): N = {c:sum(N[j] for j in P if c in P[j]) for c in P}
    M = [(sum(v*k.count(c[0]) for k,v in N.items())+1)//2 for c in N]
    return max(M)-min(M)

print("Part 1: {:d}".format(l(10,N,P)))
print("Part 2: {:d}".format(l(40,N,P)))
