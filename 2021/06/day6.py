with open('input.txt') as f:
    fishies = [int(x) for x in f.read().split(',')]

def get_fishies(days):
    for i in range(days + 1):
        new_fishies = []
        for index in range(len(fishies)):
            fishies[index] -= 1
            if fishies[index] < 0:
                new_fishies.append(8)
                fishies[index] = 6
        if i == days:
            break
        elif i > 0:
            fishies.extend(new_fishies)
    return fishies

print(f'Answer part I: {len(get_fishies(80))}')


from collections import Counter, deque
with open('input.txt') as f:
    fishies = [int(x) for x in f.read().split(',')]

occ_list = {-1:0, 0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0} | Counter(fishies)
days = 256
for day in range(days):
    rotated_values = deque(occ_list.values())
    rotated_values.rotate(-1)
    occ_list = {k:v for k,v in zip(occ_list, rotated_values)}
    for i in range(len(occ_list) - 1):
        if occ_list[-1] > 0:
            occ_list[6] += occ_list[-1]
            occ_list[8] += occ_list[-1]
            occ_list[-1] = 0

print(f'Answer part II: {sum(occ_list.values())}')