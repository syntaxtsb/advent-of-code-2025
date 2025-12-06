import os
import fileinput
from enum import Enum

os.chdir('./day-5/')

class ReadMode(Enum):
    FRESH_RANGE = 1
    INGREDIENT = 2

def main():
    
    input_file: str = 'input.txt'
    fresh_ranges: list[tuple[int, int]] = []
    ingredients: list[int] = []
    fresh_sum: int = 0
    read_mode = ReadMode.FRESH_RANGE

    # parse file
    for line in fileinput.input(input_file):
        if len(line.strip()) == 0:
            read_mode = ReadMode.INGREDIENT
        elif read_mode == ReadMode.FRESH_RANGE:
            low, high = map(int, line.strip().split('-', maxsplit=1))
            fresh_ranges.append((low, high))
        else:
            ingredients.append(int(line))
    
    # check freshness
    for ingredient in ingredients:

        for fresh_range in fresh_ranges:
            if (ingredient >= fresh_range[0]) and (ingredient <= fresh_range[1]):
                fresh_sum += 1
                break

    print('Ranges:',fresh_ranges)
    print('Ingredients:',ingredients)

    print('# of fresh ingredients:',fresh_sum)

if __name__ == '__main__':
    main()