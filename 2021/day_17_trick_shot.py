## real
data="target area: x=48..70, y=-189..-148"
## test
# data = "target area: x=20..30, y=-10..-5"


xy = data.split(": ")[1]
x,y = xy.split(",")[0], xy.split(",")[1]

def coords(c):
    c=c.split("=")[1].split("..")
    return tuple(map(int,c))
x,y = coords(x), coords(y)
print(x,y)


def part1():
    probe_velocities = [[xp,yp] for yp in range(1000) for xp in range(x[1])]
    print("velocities calculated: ", len(probe_velocities))
    probe_shots = []
    best_shot = 0

    for count, velocity in enumerate(probe_velocities):

        position = (0,0)
        trajectory = []
        for i in range(1000):
            position = tuple(sum(x) for x in zip(position, velocity))
            trajectory.append(position)
            velocity[1] -= 1
            if velocity[0] > 0:
                velocity[0] -= 1
            elif velocity[0] < 0:
                velocity[0] += 1

            if position[0] > x[1] or position[1] < y[0]:
                break

            if x[0] <= position[0] <= x[1] and y[0] <= position[1] <= y[1]:
                largest_tuple_by_second_value = max(trajectory, key=lambda i:i[1])
                probe_shots.append(largest_tuple_by_second_value[1])
                break
        
        if max(probe_shots+[0]) > best_shot:
            print(count, len(probe_velocities))
            best_shot = max(probe_shots)
            print(best_shot)


    print ("PART 1: ",max(probe_shots))

#part1()


def part2():
    probe_velocities = [[xp,yp] for yp in range(y[0],1000) for xp in range(x[1]+1)]
    print("velocities calculated: ", len(probe_velocities))
    probe_shots = []
    best_shot = 0

    for count, velocity in enumerate(probe_velocities):

        position = (0,0)
        trajectory = []
        for i in range(1000):
            position = tuple(sum(x) for x in zip(position, velocity))
            trajectory.append(position)
            velocity[1] -= 1
            if velocity[0] > 0:
                velocity[0] -= 1
            elif velocity[0] < 0:
                velocity[0] += 1

            if position[0] > x[1] or position[1] < y[0]:
                break

            if x[0] <= position[0] <= x[1] and y[0] <= position[1] <= y[1]:
                probe_shots.append(velocity)
                break
        
        # if max(probe_shots+[0]) > best_shot:
        #     print(count, len(probe_velocities))
        #     best_shot = max(probe_shots)
        #     print(best_shot)


    print ("PART 2: ",len(probe_shots))

part2()