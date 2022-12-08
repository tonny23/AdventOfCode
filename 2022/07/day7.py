import re

with open('input.txt') as f:
    lines = f.read().splitlines()

def replace_last(string, old, new):
    return new.join(string.rsplit(old, 1))

dirs = {}
dirname = ''
for index, line in enumerate(lines):
    dir = []
    if line.startswith('$ cd') and not line.startswith('$ cd ..'):
        if not line[5:] == '/':
            dirname += line[5:] + '/'
        else:
            dirname += line[5:]
        next_line = index + 2  # first line is $ ls so skip that one
        while next_line < len(lines) and not lines[next_line].startswith('$'):
            # replace dir with the full path
            if lines[next_line].startswith('dir'):
                name = dirname + lines[next_line].split()[1] + '/'
                lines[next_line] = replace_last(lines[next_line], lines[next_line].split()[1], name)
            # add the file or dir to the dir
            dir.append(lines[next_line])
            next_line += 1
        dirs[dirname] = dir
    elif line.startswith('$ cd ..'):
        # remove the last dir from the dirname
        dirname = re.sub('[^\/]+\/?$', '', dirname)

def dir_replace_dir_with_contents(dir):
    # when all dirs are replaced with their contents, return the dir
    if len([s for s in dir if "dir" in s]) == 0:
        return dir
    else:
        for dir_in_dir in [s for s in dir if "dir" in s]:
            dir.extend(dirs[dir_in_dir.split()[1]])
            dir.remove(dir_in_dir)
        dir_replace_dir_with_contents(dir)


for dir in dirs:
    dir_replace_dir_with_contents(dirs[dir])

for dir in dirs:
    for index, item in enumerate(dirs[dir]):
        dirs[dir][index] = int(item.split(' ')[0])

size = 0
# find the directories which are at most 100k total summed size
for dir in dirs:
    if sum(dirs[dir]) <= 100000:
        size += sum(dirs[dir])
print(f'Part I: {size}')


sum_list = []
for dir in dirs:
    sum_list.append(sum(dirs[dir]))
print(f"Part II: {min([i for i in sum_list if (30000000 - (70000000 - sum(dirs['/']))) < i])}")