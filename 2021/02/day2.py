forward_count = 0
down_count = 0
up_count = 0
with open('input.txt') as f:
    for line in f:
        (key, val) = line.split()
        val = int(val)
        if key == 'forward':
            forward_count += val
        elif key == 'down':
            down_count += val
        elif key == 'up':
            up_count += val

depth = down_count - up_count
print(f'Answer part I: {depth * forward_count}')

depth = 0
horizontal = 0
aim = 0
with open('input.txt') as f:
    for line in f:
        (key, val) = line.split()
        val = int(val)
        if key == 'forward':
            horizontal += val
            depth += (val * aim)
        elif key == 'down':
            aim += val
        elif key == 'up':
            aim -= val

print(f'Answer part II: {horizontal * depth}')
