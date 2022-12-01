### use these functions more


#### sum of iterable
print(
    sum([1, 1, 1])
)

print(
    sum([1, 1, 1], 10)  ### start adding from 10
)

### prod of iterable
import math

print(
    math.prod([1, 5, 9, 1, 1, 1])
)  #### prod returns product multiple of a list

### all
print(
    all([True, 1, 1, 0, False])  ### returns true if all items in list are True
)

### any
print(
    any([True, 1, 1, 0, False])  ### returns true if one items in list is True
)

### enumerate
print(
    list(
        enumerate("milk", 10)  ### adds counter to an iterable
    )
)

#### string splitting
print("miau".split("i"))

#### get every xth character
print("abcdefgh"[::2])

### multipli string
print("a" * 4)

### until the last 2 characters
print("abcdefgh"[:-2])

### the last 2 characters
print("abcdefgh"[-2:])

### the first 2 characters
print("abcdefgh"[:2])

### after the first 2 characters
print("abcdefgh"[2:])

# insert
string = "this is a string"
# index_of_character 
i = string.index(" is ")

# cuts off the string BEFORE the word " is"
print(string[:i])

# cuts off the string BEFORE and WITH the word " is"
print(string[i:])

# inserts another string before " is"
string = string[:i] + "INSERT" + string[i:]
print(string)

### this also works for lists
print(list(range(0, 10)[2:]))

### modulo #
print(3 % 3)  ### returns zero because divisble and remainder is 0
print(3 % 2)  ### returns zero because not divisble and remainder is 1

### dictionaries

dict0 = {
    "height": "178cm"
}

print(dict0.get("height"))
print(dict0.get("height", "").startswith("1"))  ### return True if value starts with 1
print(dict0.get("height", "").endswith("cm"))  ### return True if value ends with cm

### find largest key
dict1 = {"a key": 19, "another": 299}
largest_key = max(dict1, key=dict1.get)

#### SETS! use sets to remove dublicates
print(set([1, 2, 3, 1, 2, 5]))

### string.join
print("string".join(["1", "b", "endless list of strings"]))
print("".join(["1", "b", "  endless list of strings"]))  #### start string can be empty


def Alternative_For_Loop_Writing():
    return list(number + 1
                for number in [1, 3, 6, 7, 8, 12])


print(Alternative_For_Loop_Writing())

#### the sum of an empty list is 0
print(sum([]))

### no iteritems necessary if you don't need the value
for i in {"it": 1}:
    print(i)

###### map: apply function for each element

print(list(map(float, [0, 1, 2])))


def myfunction(number):
    return number * 3


print(list(map(myfunction, [0, 1, 2])))

#### you can include conditionals in list comprehensions
print([i == 1 for i in range(9)])

#### sum will also add truthy values as 1
print(sum([True, 1, False, 99]))

from collections import namedtuple

Classlike = namedtuple("somestring", "x y z")
instance = Classlike(99, 9, 9999)
print(instance.z)
print(instance[0])

from itertools import permutations, combinations, combinations_with_replacement

### pays attention to order, generates more results
print("PERMUTATIONS: ", list(permutations([1, 2, 3, 4, 5], 2)))
### doesn't add (5,1) if (1,5) is already in there
print("COMBINATIONS: ", list(combinations([1, 2, 3, 4, 5], 2)))
print("combinations_with_replacement: ", list(combinations_with_replacement([1, 2, 3, 4, 5], 2)))

### for coordinates
print("PERMUTATIONS: ", list(permutations([0, 1, -1], 2)))
print("COMBINATIONS: ", list(combinations([0, 1, -1], 2)))
print("combinations_with_replacement: ", list(combinations_with_replacement([0, 1, -1], 2)))

##### this is again different from permutations and combinations
from itertools import product

cartesian_product = list(product([0, 1], [1, 0]))
print(cartesian_product)

### can be used to get adjacent coordinates
from itertools import product

surrounding_coordinates = list(product([0, 1, -1], [1, -1, 0]))
surrounding_coordinates.remove((0, 0))
print(surrounding_coordinates)


### returns surrounding coordinates, cuts off those going outside the grid (below 0 or above max)
def Adjacent(x, y, xmax, ymax):
    return [(xd + x, yd + y) for xd, yd in surrounding_coordinates
            if not -1 in [xd + x, yd + y]
            and xd + x <= xmax
            and yd + y <= ymax]


print("ADJACENT: ", Adjacent(2, 2, 4, 2))  ### will cut off coordinates below y=2
print("ADJACENT: ", Adjacent(2, 2, 4, 3))  ### will cut off nothing and return all 8 surrounding coordinates

# delete list items by index
a_list = [1, "evil_value", 9]
del a_list[1]  # => [1,9]


# recursive_function
def recursive_function(input_rec):
    input_rec += 1
    if input_rec < 3:
        input_rec = recursive_function(input_rec)
        return input_rec

    return "RECURSION FINISHED: " + str(input_rec)


print(recursive_function(1))

# reverse the order of list elements
prime_numbers = [2, 3, 5, 7]
prime_numbers.reverse()

# reverse string or list
txt = "Hello World"[::-1]
reverse = [1, 2, 3][::-1]

# second to second last item
print([0, 1, 2, 4][1:-1])
print("string"[1:-1])

# range
# count from 0 to 9, 10 items
for i in range(10):
    print(i)

# countdown from 9 to 0, 10 items
for i in range(9, -1, -1):
    print(i)

if 9 in set([1, 2, 3, 9, 9]):  # function call / better use literal: {1, 2, 3, ...}
    print("SETS ARE EXTREMELY FASTER THAN LISTS WHEN CHECKING IF ITEM IS IN LIST/SET")
    print("but not when iterating")

# dictionary from tuples
dictionary = dict([("key1", "value1"), ("key2", "value2"), ])
print(dictionary)

# dictionary comprehension
dictionary = {x: x + 1 for x in [1, 2]}

# switch keys / values
dictionary = {y: x for x, y in dictionary.items()}  ## dictionary comprehension to switch keys/values

messy_list = [9, 6, 8, 33]
# sort ascending order
messy_list.sort()
# sort descending order
messy_list.sort(reverse=True)

# find substrings
string = "a long string 1 2 3 4 5 6 7 8 9"
if ("1" or "2") in string:
    substrings_found = True
# if you need to find many substrings
substrings_we_search = ["1", "2", "7", "9"]
if any(substring in string for substring in substrings_we_search):  # iterator that searches for substrings
    substrings_found = True

# https://www.pythonsheets.com/notes/python-generator.html
# generators empty themselves
gen = (i for i in "this_is_a_generator")
print(list(gen))
print(list(gen))

g = (x for x in range(6))
a, *c = g
print(c)

print(*(x for x in range(3)))


def Generator():
    yield from range(5)


print(list(Generator()))
print(*Generator())
for i in Generator():
    print(i)

# flatten lists
nested_list = [[1, 2], [3, 4]]
flatten_list = [val for sublist in nested_list for val in sublist]
print(flatten_list)

# find out how deeply nested a list is
depth = lambda L: isinstance(L, list) and max(map(depth, L)) + 1

# count element in list (also works for strings)
how_many_a = ["a", "list", "with", "a"].count("a")
print("string is this".count("string"))

# find largest tuple
tuple_list = [(1, 6), (99, 1)]
largest_tuple_by_first_value = max(tuple_list, key=lambda i: i[0])
largest_tuple_by_second_value = max(tuple_list, key=lambda i: i[1])
print("largest tuple", largest_tuple_by_second_value)


# add tuples together
def Add_Tuples(tuple1, tuple2):
    return tuple(sum(x) for x in zip(tuple1, tuple2))


# [::2] every other value, starting with the first
print([1, 2, 3, 4][::2])

# read file in one line: [line.strip() for line in open(path)]


# reduce
from functools import reduce


def my_return_function(a, b):
    print(a + b)
    return a + b


reduce(my_return_function, [1, 2, 3, 4, 5, 6, 7, 8])

# factorial
print("FACTORIAL: ")
factorial = lambda num: 1 if num <= 1 else num * factorial(num - 1)
print(factorial(5))

### forloop one liner
N = 1
for i in range(3): N += i
print(N)

### forloop one liner with conditions
N = 1
for i in range(3): N += i if i == 1 else 100  # N+1 if i == 1 otherwise i+100
print(N)

## lambda arguments : expression
x = lambda a: a + 1 if a == 5 else 100
print(x(5))
print(x(1))

# count iterables (works for lists, dicts, strings)
from collections import Counter

print(Counter("an iterable").most_common())
print(Counter("an iterable").most_common()[0])

# binaries to decimal
print(int("010101", 2))


def hxbin(hex_string):  # hex to binary
    return bin(int(hex_string, 16))[2:].zfill(
        len(hex_string) * 4)  # zfill makes sure the left trailing 0s are not cut off


# numpy
import numpy as np

a = np.arange(10).reshape(2, 5)
print(a)
print(a.shape)
print(a.ndim)
print(a.size)

## multidimensional splicing
# from both elements, return index 2:
print(a[0:2, 2])

## return the matrix from index 2 to 4
print(a[0:2, 2:4])


##### assert
def function_to_debug(input):
    return input + 1


test_input = 2
test_result = 3

assert function_to_debug(test_input) == test_result
