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
    if index < (len(numbers) - 3):
        if sum(number for number in numbers[index:index+3]) < sum(number for number in numbers[index+1:index+4]):
            count += 1

print(f'Answer part II: {count}')