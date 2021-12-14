

data= [
"start-A",
"start-b",
"A-c",
"A-b",
"b-d",
"A-end",
"b-end",
]

# data= [
# "dc-end",
# "HN-start",
# "start-kj",
# "dc-start",
# "dc-HN",
# "LN-dc",
# "HN-end",
# "kj-sa",
# "kj-HN",
# "kj-dc",
# ]

# data= [
# "fs-end",
# "he-DX",
# "fs-he",
# "start-DX",
# "pj-DX",
# "end-zg",
# "zg-sl",
# "zg-pj",
# "pj-he",
# "RW-he",
# "fs-DX",
# "pj-RW",
# "zg-RW",
# "start-pj",
# "he-WI",
# "zg-he",
# "pj-fs",
# "start-RW",
# ]

# data= [
# "ax-end",
# "xq-GF",
# "end-xq",
# "im-wg",
# "ax-ie",
# "start-ws",
# "ie-ws",
# "CV-start",
# "ng-wg",
# "ng-ie",
# "GF-ng",
# "ng-av",
# "CV-end",
# "ie-GF",
# "CV-ie",
# "im-xq",
# "start-GF",
# "GF-ws",
# "wg-LY",
# "CV-ws",
# "im-CV",
# "CV-wg",
# ]

from collections import defaultdict

cave_map = defaultdict(set)
for path in data:
    cave1, cave2 = path.split("-")
    cave_map[cave2].add(cave1)
    cave_map[cave1].add(cave2)


######### most readable solution without globals
def Finder(cave, path=[]):
    path = path + [cave]
    if cave == "end":
        return [path]
    else:        
        more_paths = []
        for next_cave in cave_map[cave]:
            if next_cave != "start" and not (next_cave.islower() and next_cave in path):
                more_paths += Finder(next_cave, path)
        return more_paths

print("No Globals/ Part1: ")
print(len( [path for path in Finder("start")] ))





def Visit_Check(next_cave, path):
    if next_cave.isupper():
        return True 
    else:
        if next_cave not in path:
            return True
        else:
            for small_cave in path:
                if small_cave.islower() and small_cave not in ["start", "end"]:
                    if path.count(small_cave) > 1:
                        return False
            return True

def Finder2(cave, path=[]):
    path = path + [cave]
    if cave == "end":
        return [path]
    else:        
        more_paths = []
        for next_cave in cave_map[cave]:
            if next_cave != "start" and Visit_Check(next_cave, path):
                more_paths += Finder2(next_cave, path)
        return more_paths

print("No Globals/ Part2: ")
print(len( [path for path in Finder2("start")] ))



######### ALTERNATIVE short but less readable solution with list comprehension/flatten
def flatten(nested_list):
    return [val for sublist in nested_list for val in sublist]

def Finder3(cave, path=[]):
    path = path + [cave]
    if cave == "end":
        return [path]
    else:
        return flatten(Finder3(next_cave, path) for next_cave in cave_map[cave] 
                    if next_cave != "start" 
                    and not (next_cave.islower() and next_cave in path))
                    
print("Generator/flatten Part1: ")
print(len( [path for path in Finder3("start")] ))






## ugly first&fast solution with globals

# def Find_Path(cave, path):
#     global remember_paths
#     remember_paths[path].append(cave)

#     if cave != "end":
#         path_options = cave_map[cave]

#         for i, next_cave in enumerate(path_options):

#             if next_cave != "start" and not (next_cave.islower() and next_cave in remember_paths[path]):
#                 this_path = len(remember_paths)+1
#                 remember_paths[this_path] = list(remember_paths[path]) ### duplicate
#                 Find_Path(next_cave, this_path)

# def part1():
#     global remember_paths
#     remember_paths = defaultdict(list)
#     Find_Path("start",0)
#     print ("part 1: ")
#     print(len( [path for path in remember_paths.values() if "end" in path] ))

# part1()