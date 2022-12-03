with open('input.txt') as f:
    rucksacks = f.readlines()

def split_str(string):
    half = int(len(string)/2)
    return string[:half], string[half:]

def get_common(compartment1, compartment2):
    common = set(compartment1).intersection(compartment2)
    return common

def calculate_priority(items):
    priority = 0
    for item in items:
        if item.islower():
            priority += ord(item) - 96
        elif item.isupper():
            priority += ord(item) - 38
    return priority

result = 0
for rucksack in rucksacks:
    compartment1, compartment2 = split_str(rucksack.strip())
    common = get_common(compartment1, compartment2)
    result += calculate_priority(get_common(compartment1, compartment2))
    
print(f'Part 1: {result}')

def get_common_from_3_lists(lst1, lst2, lst3):
    return list(set(lst1) & set(lst2) & set(lst3))

result = 0
groups = iter(rucksacks)
for rucksack1, rucksack2, rucksack3 in zip(*[groups, groups, groups]):
    result += calculate_priority(get_common_from_3_lists(rucksack1.strip(), rucksack2.strip(), rucksack3.strip()))

print(f'Part 2: {result}')