with open('input.txt') as f:
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

o2_str = ""
co2_str = ""
lines_part2 = lines
for index in range(len(lines_part2[0])):
    count_0 = 0
    count_1 = 0
    for line in lines_part2:
        bit = line[index]
        if bit == "0":
            count_0 += 1
        elif bit == "1":
            count_1 += 1
    if len(lines_part2) == 1:
        o2_str += lines_part2[0][index]
    elif count_0 > count_1:
        o2_str += "0"
    elif count_0 == count_1:
        o2_str += "1"
    else:
        o2_str += "1"
    lines_part2 = [x for x in lines_part2 if x.startswith(o2_str)]

lines_part2 = lines

for index in range(len(lines_part2[0])):
    count_0 = 0
    count_1 = 0
    for line in lines_part2:
        bit = line[index]
        if bit == "0":
            count_0 += 1
        elif bit == "1":
            count_1 += 1
    if len(lines_part2) == 1:
        co2_str += lines_part2[0][index]
    elif count_0 < count_1:
        co2_str += "0"
    elif count_0 == count_1:
        co2_str += "0"
    else:
        co2_str += "1"
    lines_part2 = [x for x in lines_part2 if x.startswith(co2_str)]

result = int(o2_str, 2) * int(co2_str, 2)
print(f'Answer part II: {result}')