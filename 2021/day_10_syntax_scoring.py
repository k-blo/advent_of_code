import os, sys
path = os.path.dirname(os.path.realpath(__file__)) 
with open(path + '/day_10_input.txt', 'r') as text_file: 

    data = text_file.read().splitlines() 



# data= [
# "[({(<(())[]>[[{[]{<()<>>",
# "[(()[<>])]({[<{<<[]>>(",
# "{([(<{}[<>[]}>{[]{[(<()>",
# "(((({<>}<{<{<>}{[]{[]{}",
# "[[<[([]))<([[{}[[()]]]",
# "[{[{({}]{}}([{[{{{}}([]",
# "{<[[]]>}<{[{[{[]{()[[[]",
# "[<(<(<(<{}))><([]([]()",
# "<{([([[(<>()){}]>(<<{{",
# "<{([{{}}[<[[[<>{}]]]>[]]",
# ]


minichunks = ["()", "[]", "<>", "{}"]
openers = [c[0] for c in minichunks]
closers = [c[1] for c in minichunks]
matching = {c[1]:c[0] for c in minichunks}
matching_closers = {c[0]:c[1] for c in minichunks}


def Find_Closers(line):
    for index, char in enumerate(line):
        if char in closers:
            find_opener = matching[char]
            if line[index-1] != find_opener:
                return [char]
    return []

def Kill_Microchunks(line):
    minichunks = ["()", "[]", "<>", "{}"]
    while any(chunk in line for chunk in minichunks):
        for minichunk in minichunks:
            line = line.replace(minichunk, "")
    return line

def part1():
    points = {")": 3,"]": 57,"}": 1197,">": 25137}
    bad_syntax = []
    for line in data:
        line = Kill_Microchunks(line)
        bad_syntax += Find_Closers(line)
    print ("Part 1: ")
    print (sum([points[char] for char in bad_syntax]))
part1()





def Auto_Complete(line):
    auto_complete = ""
    for char in line[::-1]:
        auto_complete += matching_closers[char]
    return auto_complete

def Score(completion):
    points = {")": 1,"]": 2,"}": 3,">": 4}
    total_score = 0
    for char in completion:
        total_score *= 5
        total_score += points[char]
    return total_score

def part2():
    autocomplete = []
    for line in data:
        line = Kill_Microchunks(line)
        if not Find_Closers(line):
            autocomplete += [Auto_Complete(line)]
    print ("Part 2: ")
    scores = [Score(comp) for comp in autocomplete]
    scores.sort()
    middle_score = scores[int(len(scores)*0.5)]
    print(middle_score)
part2()





