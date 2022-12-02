input = open('input.txt', 'r').read().strip()

rps_list = ['rock', 'paper', 'scissors']

# rock paper scissors, a win is 6 points, loss 0 points, draw 3 points, win with rock is extra 1 point, win with scissors is extra 2 points, win with paper is extra 3 points
def rps(elf_opponent, me):
    points = 0
    if me == rps_list[0]: # rock
        points += 1
    elif me == rps_list[1]: # paper:
        points += 2
    elif me == rps_list[2]: # scissors:
        points += 3
    # draw
    if elf_opponent == me: # draw
        points += 3
    elif elf_opponent == rps_list[0]: # rock
        if me == rps_list[1]: # paper
            # i won
            points += 6
    elif elf_opponent == rps_list[1]: # paper
        if me == rps_list[2]: # scissors
            # i won
            points += 6
    elif elf_opponent == rps_list[2]: # scissors
        if me == rps_list[0]: # rock
            points += 6
    return points
        
score = 0
decryption_rps = str.maketrans({'A': rps_list[0], 'B': rps_list[1], 'C': rps_list[2], 'X': rps_list[0], 'Y': rps_list[1], 'Z': rps_list[2]})

for line in input.splitlines():
    elf_opponent, me = line.translate(decryption_rps).split(' ')
    score += rps(elf_opponent, me)
    
print(f"Part 1: {score}")

result_list = ['lose', 'draw', 'win']
decryption_result = str.maketrans({'A': rps_list[0], 'B': rps_list[1], 'C': rps_list[2], 'X': result_list[0], 'Y': result_list[1], 'Z': result_list[2]})

def rps2(elf_opponent, result):
    if elf_opponent == rps_list[0]: # rock
        if result == result_list[2]: #win
            me = rps_list[1] #paper
            return rps(elf_opponent, me)
        elif result == result_list[0]: #lose
            me = rps_list[2] #scissors
            return rps(elf_opponent, me)
        elif result == result_list[1]: #draw
            me = elf_opponent #rock
            return rps(elf_opponent, me)
    elif elf_opponent == rps_list[1]: #paper
        if result == result_list[2]: #win
            me = rps_list[2] #scissors
            return rps(elf_opponent, me)
        elif result == result_list[0]: #lose
            me = rps_list[0] #rock
            return rps(elf_opponent, me)
        elif result == result_list[1]: #draw
            me = elf_opponent #paper
            return rps(elf_opponent, me)
    elif elf_opponent == rps_list[2]: #scissors
        if result == result_list[2]: #win
            me = rps_list[0] #rock
            return rps(elf_opponent, me)
        elif result == result_list[0]: #lose
            me = rps_list[1] #paper
            return rps(elf_opponent, me)
        elif result == result_list[1]: #draw
            me = elf_opponent #scissors
            return rps(elf_opponent, me)

score = 0
for line in input.splitlines():
    elf_opponent, me = line.translate(decryption_result).split(' ')
    score += rps2(elf_opponent, me)
print(f"Part 2: {score}")

