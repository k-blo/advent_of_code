

data = [9093927,11001876]

def transform(subject_number, loops):
    value = 1
    for i in range(loops):
        value *= subject_number
        value = value % 20201227
    return value

value = 1
loop = 0
keys = set(data)
store = {}
while len(keys) > 0:
    loop += 1
    value = (value * 7) % 20201227
    if value in keys:
        keys.remove(value)
        store[value] = loop

encryption_key = [transform(key, loops) for key, loops in list(zip(store.keys(), reversed(list(store.values()))))][0]
print ("PART 1: " + str(encryption_key))


