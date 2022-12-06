import re

with open('input.txt') as f:
    lines = f.read().split('\n\n')

stacks_tracker = {}
#processing text into arrays
stacks = lines[0].splitlines()
number_stacks = stacks[len(stacks) - 1]

# get indices of the integers for the columns to get
index_stacks = re.finditer(pattern='\d{1}', string=number_stacks)
indices = [index.start() for index in index_stacks]

stacks.pop()
lines.pop(0)

# create arrays of the stacks
for index in indices:
    stack_list = []
    for stack in stacks:
        if stack[index] != ' ':
            stack_list.append(stack[index])
    stacks_tracker[number_stacks[index]] = stack_list

# reverse the order of the stacks
def reverse_stacks(stacks_tracker):
    for stack in stacks_tracker:
        stacks_tracker[stack].reverse()
    return stacks_tracker

reverse_stacks(stacks_tracker)
moving_lines = lines[0].splitlines()

for line in moving_lines:
    moving_ints = [int(s) for s in line.split() if s.isdigit()]
    for i in range(moving_ints[0]):
        stacks_tracker[str(moving_ints[2])].append(stacks_tracker[str(moving_ints[1])].pop())

reverse_stacks(stacks_tracker)
result = ""
for stack in stacks_tracker.values():
  result += stack[0]
  
print(f'Part I: {result}')

stacks_tracker = {}
moving_lines = lines[0].splitlines()

# create arrays of the stacks
for index in indices:
    stack_list = []
    for stack in stacks:
        if stack[index] != ' ':
            stack_list.append(stack[index])
    stacks_tracker[number_stacks[index]] = stack_list

for line in moving_lines:
    moving_ints = [int(s) for s in line.split() if s.isdigit()]
    stacks_tracker[str(moving_ints[2])] = stacks_tracker[str(moving_ints[1])][0:moving_ints[0]] + stacks_tracker[str(moving_ints[2])]
    stacks_tracker[str(moving_ints[1])] = stacks_tracker[str(moving_ints[1])][moving_ints[0]:len(stacks_tracker[str(moving_ints[1])])]

result = ""
for stack in stacks_tracker.values():
  result += stack[0]
  
print(f'Part II: {result}')