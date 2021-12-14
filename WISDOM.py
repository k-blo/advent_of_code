### use these functions more


#### sum of iterable
print(
    sum([1,1,1])
)

print(
    sum([1,1,1],10) ### start adding from 10
)


### prod of iterable
import math

print (
    math.prod([1,5,9,1,1,1])
    ) #### prod returns product multiple of a list

### all
print (
    all([True, 1, 1, 0, False]) ### returns true if all items in list are True
)


### any
print (
    any([True, 1, 1, 0, False]) ### returns true if one items in list is True
)



### enumerate
print (
    list(
    enumerate("milk", 10) ### adds counter to an iterable
    )
)



#### string splitting
print (   "miau".split("i")   )

#### get every xth character
print (   "abcdefgh"[::2]  ) 

### multipli string
print ("a" * 4)

### until the last 2 characters
print ("abcdefgh"[:-2])

### the last 2 characters
print ("abcdefgh"[-2:])

### the first 2 characters
print ("abcdefgh"[:2])

### after the first 2 characters
print ("abcdefgh"[2:])


### this also works for lists
print (list(range(0,10)[2:]))



### modulo #
print (3 % 3) ### returns zero because divisble and remainder is 0
print (3 % 2) ### returns zero because not divisble and remainder is 1



### dictionaries

dict0 = {
    "height": "178cm"
}

print(dict0.get("height") )
print(dict0.get("height", "").startswith("1") ) ### return True if value starts with 1
print(dict0.get("height", "").endswith("cm") ) ### return True if value ends with cm



#### SETS! use sets to remove dublicates
print ( set([1,2,3,1,2,5])  )

### string.join
print ("string".join(["1","b", "endless list of strings"]))
print ("".join(["1","b", "  endless list of strings"])) #### start string can be empty


def Alternative_For_Loop_Writing():
    return list(number + 1
        for number in [1,3,6,7,8,12])


print (Alternative_For_Loop_Writing())


#### the sum of an empty list is 0
print (sum([]))

### no iteritems necessary if you don't need the value
for i in {"it":1}:
    print (i)



###### map: apply function for each element

print (list(map(float,[0,1,2])))

def myfunction(number):
    return number * 3
print (list(map(myfunction,[0,1,2])))


#### you can include conditionals in list comprehensions
print([i == 1 for i in range(9)])

#### sum will also add truthy values as 1
print(  sum([True, 1, False, 99])  )



from collections import namedtuple
Classlike = namedtuple("somestring","x y z")
instance = Classlike(99,9,9999)
print (instance.z)
print (instance[0])



##### this is again different from permutations and combinations
from itertools import product
cartesian_product = list(product([0,1], [1,0])) 
print (cartesian_product)




### delete list items by index
a_list = [1, "evil_value", 9]
del a_list[1] # => [1,9]


### recursive_function
def recursive_function(input):
    input += 1
    if input < 3:
        input = recursive_function(input)
        return input
        
    return "RECURSION FINISHED: " + str(input)

print (recursive_function(1))



# reverse the order of list elements
prime_numbers = [2, 3, 5, 7]
prime_numbers.reverse()


# reverse string or list
txt = "Hello World"[::-1]
reverse = [1,2,3][::-1]


### second to second last item
print([0,1,2,4][1:-1])
print("string"[1:-1])


#### range
# count from 0 to 9, 10 items
for i in range(10):
    print(i)

# countdown from 9 to 0, 10 items
for i in range(9,-1,-1):
    print(i)


if 9 in set([1,2,3,9,9]):
    print ("SETS ARE EXTREMELY FASTER THAN LISTS WHEN CHECKING IF ITEM IS IN LIST/SET")
    print ("but not when iterating")



#### dictionary from tuples
dictionary = dict([("key1","value1"), ("key2","value2"), ])
print (dictionary)

#### dictionary comprehension
dictionary = {x:x+1 for x in [1,2]}
### switch keys / values
dictionary = {y:x for x,y in dictionary.items()} ## dictionary comprehension to switch keys/values


messy_list = [9, 6, 8, 33]
### sort ascending order
messy_list.sort()
### sort descending order
messy_list.sort(reverse=True)



## find substrings
string = "a long string 1 2 3 4 5 6 7 8 9"
if ("1" or "2") in string:
    substrings_found = True
#### if you need to find many substrings
substrings_we_search = ["1", "2", "7", "9"]
if any(substring in string for substring in substrings_we_search): #iterator that searches for substrings
    substrings_found = True



# https://www.pythonsheets.com/notes/python-generator.html
####### generators empty themselves
gen = (i for i in "this_is_a_generator")
print(list(gen))
print(list(gen))


g = (x for x in range(6))
a,*c = g
print(c)


print(*(x for x in range(3)))

def Generator():
    yield from range(5)

print (list(Generator()))
print(*Generator())
for i in Generator():
    print (i)




### flatten lists
nested_list = [[1,2],[3,4]]
flatten_list = [val for sublist in nested_list for val in sublist]
print (flatten_list)



### count element in list (also works for strings)
how_many_a = ["a", "list", "with", "a"].count("a")
print("string is this".count("string"))


## find largest tuple
tuple_list = [(1,6), (99,1) ]
largest_tuple_by_first_value = max(tuple_list, key=lambda i:i[0])
largest_tuple_by_second_value = max(tuple_list, key=lambda i:i[1])

### [::2] every other value, starting with the first
print([1,2,3,4][::2])


## read file in one line: [line.strip() for line in open(path)]



# REDUCE
from functools import reduce

def my_return_function(a,b):
    print(a + b )
    return a+b
reduce(my_return_function, [1,2,3,4,5,6,7,8])



######## factorial
print ("FACTORIAL: ")
factorial = lambda num : 1 if num <= 1 else num*factorial(num-1)
print (factorial(5))


### forloop one liner
N = 1
for i in range(3): N += i
print(N)


### forloop one liner with conditions
N = 1
for i in range(3): N += i if i == 1 else 100
print(N)


### lambda arguments : expression
x = lambda a : a + 1 if a == 5 else 100
print(x(5)) 
print(x(1)) 