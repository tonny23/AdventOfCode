with open('input.txt') as f:
    elves = f.read().split('\n\n')

def sum_list_of_list_of_strings(list_of_list):
    list_of_sum_of_list_of_strings = []
    for list_of_strings in list_of_list:
        list_of_sum_of_list_of_strings.append(
            sum([int(i.strip()) for i in list_of_strings.split('\n')]))
    return list_of_sum_of_list_of_strings

sum_list = sum_list_of_list_of_strings(elves)
print(f'Part I: {max(sum_list_of_list_of_strings(elves))}')

#sum of top 3 numbers of list
def sum_top_3(list_of_numbers):
    list_of_numbers.sort(reverse=True)
    return sum(list_of_numbers[:3])

print(f'Part II: {sum_top_3(sum_list)}')
