with open('example.txt') as f:
    lines = f.read().splitlines()
    
coords = {
    'x': None,
    'y': None,
}

coords_list = []

for line_index, line in enumerate(lines):
    for index, coords in enumerate(line.split(' -> ')):
        coords_list.append(coords)
        for coord in coords.split(','):
            print(coord)