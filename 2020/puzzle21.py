import os, sys
path = os.path.dirname(os.path.realpath(__file__)) 
with open(path + '/day_21_input.txt', 'r') as text_file: 

    data = text_file.read().splitlines()



# data = [
# "mxmxvkd kfcds sqjhc nhms (contains dairy, fish)",
# "trh fvjkl sbzzf mxmxvkd (contains dairy)",
# "sqjhc fvjkl (contains soy)",
# "sqjhc mxmxvkd sbzzf (contains fish)",
# ]

from collections import defaultdict
possibilities = defaultdict(list)
all_ingredients = []
ingredient_counter = []

for line in data:
    ingredients = line.split(" (")[0].split()
    #print (ingredients)
    for ingredient in ingredients:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)
        ingredient_counter.append(ingredient)

    allergens = line.split("(contains ")[1][:-1].split(", ")
    #print (allergens)

    for allergen in allergens:
        possibilities[allergen].append(ingredients)

for allergen, ingredients in possibilities.items():
    possibilities[allergen] = list(set.intersection(*map(set,possibilities[allergen])))

for i in range(10):
    for allergen, ingredients in possibilities.items():
        if len(ingredients) == 1:
            defined_ingredient = ingredients[0]
            for other_allergen, other_ingredients in possibilities.items():
                if other_allergen != allergen and defined_ingredient in other_ingredients:
                    possibilities[other_allergen].remove(defined_ingredient)

ingredients_with_allergens = [ingredient[0] for ingredient in possibilities.values()]

ingredients_without_allergens = ([ingredient for ingredient in all_ingredients if ingredient not in ingredients_with_allergens])

print ("PART 1")
print(sum([1 for ingredient in ingredient_counter if ingredient in ingredients_without_allergens]))



alphabetical_order = sorted(possibilities.keys())

print ("PART 2")
print("".join([possibilities[key][0]+"," for key in alphabetical_order])[:-1])

