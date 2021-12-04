import numpy as np

numbers_to_be_called = []
bingo_cards = []
with open('input.txt') as f:
    lines = f.read().split('\n\n')

numbers_to_be_called = lines[0].split(',')
lines.pop(0)
for index, line in enumerate(lines):
    bingo_lines = line.split('\n')
    bingo_card = []
    for bingo_line in  bingo_lines:
        bingo_card.append(bingo_line.split())
    bingo_cards.append(bingo_card)

def get_winning_card():
    numbers = []
    for i, number in enumerate(numbers_to_be_called):
        numbers.append(number)
        for index, bingo_card in enumerate(bingo_cards):
            if i >= len(bingo_card[0]):
                rows = np.array(bingo_card)
                cols = np.array(bingo_cards[index]).transpose()
                for row, col in zip(rows, cols):
                    if (set(row).issubset(set(numbers))):
                        return numbers, rows, number
                    if (set(col).issubset(set(numbers))):
                        return numbers, rows, number

called_numbers, card, winning_number = get_winning_card()
# print(f'Winning row: {called_numbers}')
# print(f'Winning card: {card}')
# print(f'Winning number: {winning_number}')

flat_list = [int(item) for sublist in card for item in sublist]
called_numbers = [int(i) for i in called_numbers]
print(f'Answer part I: {sum(list(set(flat_list) - set(called_numbers))) * int(winning_number)}')

def get_last_winning_card():
    numbers = []
    bingo_cards_won = [False] * len(bingo_cards)
    for i, number in enumerate(numbers_to_be_called):
        numbers.append(number)
        for index, bingo_card in enumerate(bingo_cards):
            if i >= len(bingo_card[0]):
                rows = np.array(bingo_card)
                cols = np.array(bingo_cards[index]).transpose()
                for row, col in zip(rows, cols):
                    if (set(row).issubset(set(numbers))):
                        bingo_cards_won[index] = True
                        if all(bingo_cards_won):
                            return numbers, rows, number
                    if (set(col).issubset(set(numbers))):
                        bingo_cards_won[index] = True
                        if all(bingo_cards_won):
                            return numbers, rows, number

called_numbers, card, winning_number = get_last_winning_card()
# print(f'Winning row: {called_numbers}')
# print(f'Winning card: {card}')
# print(f'Winning number: {winning_number}')

flat_list = [int(item) for sublist in card for item in sublist]
called_numbers = [int(i) for i in called_numbers]
print(f'Answer part II: {sum(list(set(flat_list) - set(called_numbers))) * int(winning_number)}')