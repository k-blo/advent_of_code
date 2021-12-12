


data = [1,5,5,1,5,1,5,3,1,3,2,4,3,4,1,1,3,5,4,4,2,1,2,1,2,1,2,1,5,2,1,5,1,2,2,1,5,5,5,1,1,1,5,1,3,4,5,1,2,2,5,5,3,4,5,4,4,1,4,5,3,4,4,5,2,4,2,2,1,3,4,3,2,3,4,1,4,4,4,5,1,3,4,2,5,4,5,3,1,4,1,1,1,2,4,2,1,5,1,4,5,3,3,4,1,1,4,3,4,1,1,1,5,4,3,5,2,4,1,1,2,3,2,4,4,3,3,5,3,1,4,5,5,4,3,3,5,1,5,3,5,2,5,1,5,5,2,3,3,1,1,2,2,4,3,1,5,1,1,3,1,4,1,2,3,5,5,1,2,3,4,3,4,1,1,5,5,3,3,4,5,1,1,4,1,4,1,3,5,5,1,4,3,1,3,5,5,5,5,5,2,2,1,2,4,1,5,3,3,5,4,5,4,1,5,1,5,1,2,5,4,5,5,3,2,2,2,5,4,4,3,3,1,4,1,2,3,1,5,4,5,3,4,1,1,2,2,1,2,5,1,1,1,5,4,5,2,1,4,4,1,1,3,3,1,3,2,1,5,2,3,4,5,3,5,4,3,1,3,5,5,5,5,2,1,1,4,2,5,1,5,1,3,4,3,5,5,1,4,3]

# data = [3,4,3,1,2]





def part_1():
    swarm = list(data)
    for i in range(80):
        new_fish = []
        for index,fish in enumerate(swarm):
            if fish == 0:
                new_fish.append(8)
                swarm[index] = 6
            else:
                swarm[index] -= 1
        swarm += new_fish
    print ("Part 1 solution:")
    print (len(swarm))

part_1()





from collections import defaultdict

def part_2(): ### does the same as part 1, but extremely more performant
    swarm = {}
    for i in range(9):
        swarm[i]=0
    for fish in data:
        swarm[fish] += 1


    for i in range(256):

        reproducing_fish = swarm[0]
        for age_group in range(1,9):
            swarm[age_group-1] = int(swarm[age_group])
        swarm[6] += reproducing_fish
        swarm[8] = reproducing_fish


        print(i)
    print ("Part 2 solution:")
    print (sum(swarm.values()))

part_2()