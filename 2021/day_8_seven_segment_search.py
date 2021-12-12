import os, sys
path = os.path.dirname(os.path.realpath(__file__)) 
with open(path + '/day_8_input.txt', 'r') as text_file: 

    data = text_file.read().splitlines() 



# data= [
# "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
# "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
# "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
# "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
# "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
# "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
# "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
# "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
# "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
# "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce",
# ]




def part_1():
    digits = {0:"abcefg", 1:"cf", 2:"acdeg", 3:"acdfg", 4:"bcdf", 5:"abdfg", 6:"abdefg", 7:"acf", 8:"abcdefg", 9:"abcdfg"}
    unique_length_digits = [1,4,7,8]
    unique_lengths = [len(digits[digit]) for digit in unique_length_digits]

    count_unique_digits = 0
    for entry in data:
        output = entry.split("|")[1]
        signals = output.split()
        count_unique_digits += len([signal for signal in signals if len(signal) in unique_lengths])
    print("part 1 solution: ")
    print(count_unique_digits)
part_1()








# 7 must be in 3 and 9,0
# 4,3 must be in 9
# => 9,3
# 5 must be in 6

def Pattern(signals):
    unique = {
        2:1,
        3:7,
        4:4,
        7:8,
    }
    signals = [set(signal) for signal in signals]
    pattern = {}
    for signal in signals:
        if len(signal) in unique:
            pattern[unique[len(signal)]] = set(signal)

    ### ALTERNATIVE
    # def Find_3(signal):
    #     return True if len(signal) == 5 and pattern[7].issubset(signal) else False
    # pattern[3] = list(filter(Find_3, signals))[0]

    for signal in signals:
        if len(signal) == 5 and pattern[7].issubset(signal):
            pattern[3] = signal

        ##### 9,0,6
    for signal in signals:
        if len(signal) == 6 and pattern[3].issubset(signal):
            pattern[9] = signal
    for signal in signals:
        if len(signal) == 6 and pattern[7].issubset(signal) and signal != pattern[9]:
            pattern[0] = signal
    for signal in signals:
        if len(signal) == 6 and signal not in pattern.values():
            pattern[6] = signal

        ### 5,2
    for signal in signals:
        if len(signal) == 5 and signal.issubset(pattern[6]):
            pattern[5] = signal  

    for signal in signals:
        if len(signal) == 5 and signal not in pattern.values():
            pattern[2] = signal

    pattern = {"".join(y):x for x,y in pattern.items()} ## dictionary comprehension to switch keys/values
    return pattern



def Decode(signal, patterns):
    for key in patterns:
        if len(signal) == len(key) == len([True for letter in key if letter in signal]):
            return patterns[key]


def part_2():
    output_values = []
    for entry in data:
        definitions = entry.split("|")[0].split()
        signals = entry.split("|")[1].split()

        pattern = Pattern(definitions)

        output_decoded = "".join([str(Decode(signal,pattern)) for signal in signals])
        output_values += [int(output_decoded)]

    print("part 2 solution: ")
    print (sum(output_values))
part_2()

