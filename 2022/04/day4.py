with open('input.txt') as f:
    lines = f.read().splitlines()

def create_list_of_numbers(start_end_list):
    return list(range(int(start_end_list[0]), int(start_end_list[1]) + 1))

def check_common_assignment(assignment1, assignment2):
    if set(assignment1).issubset(set(assignment2)) or set(assignment2).issubset(set(assignment1)):
        return True
    else:
        return False
        
count_common_pairs = 0
pairs = []
for line in lines:
    pair = []
    for assignments in line.split(','):
        pair.append(create_list_of_numbers(assignments.split('-')))
    if check_common_assignment(pair[0], pair[1]):
        count_common_pairs += 1
    pairs.append(pair)
    
print(f'Part I: {count_common_pairs}')

def check_common_assignment_all(assignment1, assignment2):
    if set(assignment1) & set(assignment2):
        return True
    else:
        return False

count_common_assignments = 0
for line in lines:
    pair = []
    for assignments in line.split(','):
        pair.append(create_list_of_numbers(assignments.split('-')))
    if check_common_assignment_all(pair[0], pair[1]):
        count_common_assignments += 1

print(f'Part II: {count_common_assignments}')

