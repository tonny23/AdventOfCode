with open('example.txt') as f:
    lines = f.read().splitlines()

count_arr_0 = [0] * len(lines[0])
count_arr_1 = [0] * len(lines[0])

for line in lines:
    for index, bit in enumerate(list(line)):
        bit = int(bit)
        if bit == 0:
            count_arr_0[index] += 1
        elif bit == 1:
            count_arr_1[index] += 1
            
print(count_arr_0)
print(count_arr_1)

bit_string_gamma = ""
bit_string_epsilon = ""

for bit_0, bit_1 in zip(count_arr_0, count_arr_1):
    if bit_0 > bit_1:
        bit_string_gamma += "0"
        bit_string_epsilon += "1"
    else:
        bit_string_gamma += "1"
        bit_string_epsilon += "0"
result = int(bit_string_gamma, 2) * int(bit_string_epsilon, 2)

print(f'Answer part I: {result}')
