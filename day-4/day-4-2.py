import os
import fileinput
import copy

os.chdir('./day-4/')

ADJACENT_COORDS: list[tuple[int, int]] = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]

def remove_accessible_rolls(grid: list[list[str]], clutter_point: int):

    found_grid: list[list[str]] = copy.deepcopy(grid)
    removed_rolls: int = 0

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            clutter: int = 0
            
            if cell == '@':
                # check 8 adjacent cells for clutter
                for check_coord in ADJACENT_COORDS:
                    if (y + check_coord[1] >= 0) and (y + check_coord[1] < len(grid)):
                        if (x + check_coord[0] >= 0) and (x + check_coord[0] < len(row)):
                            clutter += roll_value(grid[y + check_coord[1]][x + check_coord[0]])

                if clutter < clutter_point:
                    found_grid[y][x] = '.'
                    removed_rolls += 1

    return (found_grid, removed_rolls)

# returns 1 if roll == '@', else returns 0
def roll_value(roll: str):
    return int(roll == '@')

def main():
    
    input_file: str = 'input.txt'
    grid: list[list[str]] = []
    removed_rolls: int = 0
    removed_round: int = 99

    # parse file
    for line in fileinput.input(input_file):
        grid.append(list(line.strip()))

    # remove accessible rolls
    while removed_round > 0:
        grid, removed_round = remove_accessible_rolls(grid, 4)
        removed_rolls += removed_round
    
    print(grid)
    print('Removed rolls:',removed_rolls)

if __name__ == '__main__':
    main()