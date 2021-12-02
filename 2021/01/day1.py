with open('input.txt') as f:
    numbers = [int(x) for x in f.read().splitlines()]

count = 0
for index, number in enumerate(numbers):
    if index != 0:
        if number > numbers[index-1]:
            count += 1

print(f'Answer part I: {count}')

count = 0
for index, number in enumerate(numbers):
    if sum(numbers[index:index+3]) < sum(numbers[index+1:index+4]):
        count += 1

print(f'Answer part II: {count}')