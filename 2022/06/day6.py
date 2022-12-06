with open('input.txt') as f:
    line = f.read()

def check_unique_characters_in_string(string):
    return len(set(string)) == len(string)

for index, char in enumerate(line):
    if check_unique_characters_in_string(line[index:index + 4]):
        print(f'Part I: {index + 4}')
        break

for index, char in enumerate(line):
    if check_unique_characters_in_string(line[index:index + 14]):
        print(f'Part II: {index + 14}')
        break
