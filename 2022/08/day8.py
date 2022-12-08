with open('input.txt', 'r') as f:
    matrix = [[int(num) for num in line.strip()] for line in f]


def get_column(matrix, i):
    return [row[i] for row in matrix]

def get_row(matrix, i):
    return matrix[i]

def compare_to_list_left_and_right(list, int, index):
    return all(i < int for i in list[:index]) or all(i < int for i in list[index + 1:])


col_len = len(matrix[0])
row_len = len(matrix)
print(col_len, row_len)
count = col_len 
# traverse through each row of matrix one by one
visible = (col_len + row_len) * 2 - 4
for row in range(row_len):
    # traverse through each column of matrix one by one
    if row > 0 and row < row_len - 1:
        for col in range(col_len):
            if col > 0 and col < col_len - 1:
                if compare_to_list_left_and_right(get_column(matrix, col), matrix[row][col], row) or compare_to_list_left_and_right(get_row(matrix, row), matrix[row][col], col):
                    visible += 1

print(f'Part I: {visible}')

def find_visible_trees(trees, int, index):
    trees_visible = []
    # look up/left
    direction_trees_visible = 0
    for tree in list(reversed(trees[:index])):
        if tree >= int:
            direction_trees_visible += 1
            break
        else:
            direction_trees_visible += 1
    trees_visible.append(direction_trees_visible)
    # look down/right
    direction_trees_visible = 0
    for tree in trees[index + 1:]:
        if tree >= int:
            direction_trees_visible += 1
            break
        else:
            direction_trees_visible += 1
    trees_visible.append(direction_trees_visible)
    return trees_visible

def get_scenic_score(visible_trees):
    score = 1
    for tree in visible_trees:
        score = score * tree
    return score
    
scores = []
for row in range(row_len):
    if row > 0 and row < row_len - 1:
        for col in range(col_len):
            if col > 0 and col < col_len - 1:
                visible_col = (find_visible_trees(get_column(matrix, col), matrix[row][col], row))
                visible_row = (find_visible_trees(get_row(matrix, row), matrix[row][col], col))
                all_visible = visible_col + visible_row
                scores.append(get_scenic_score(all_visible))

print(f'Part II: {max(scores)}')

