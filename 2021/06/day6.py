import gc
with open('input.txt') as f:
    fishies = [int(x) for x in f.read().split(',')]

days = 80
def get_fishies(days):
    for i in range(days + 1):
        new_fishies = []
        print(f'day {i}/{days} {len(fishies)}')
        for index, fish in enumerate(fishies):
            fishies[index] -= 1
            if fishies[index] < 0:
                new_fishies.append(8)
                fishies[index] = 6
        if i == days:
            break
        elif i > 0:
            gc.disable()
            fishies.extend(new_fishies)
            gc.enable()
    return fishies


print(f'Answer part I: {len(get_fishies(days))}')
# print(f'Answer part II: {len(get_fishies(days))}')



