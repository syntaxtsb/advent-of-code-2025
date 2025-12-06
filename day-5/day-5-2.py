import os
import fileinput
from enum import Enum

os.chdir('./day-5/')

class ReadMode(Enum):
    FRESH_RANGE = 1
    INGREDIENT = 2

def simplify_fresh_ranges(fresh_ranges: list[tuple[int, int]]):
    
    new_ranges: list[tuple[int, int]] = []

    for fresh_range in fresh_ranges:

        new_range: tuple[int, int] = fresh_range
        remove_ranges: list[int] = []
        is_redundant: bool = False

        for j, join_range in enumerate(new_ranges):
            # new_range is subset of join_range
            if (new_range[0] >= join_range[0]) and (new_range[1] <= join_range[1]):
                is_redundant = True
            # new_range contains join_range
            elif (new_range[0] <= join_range[0]) and (new_range[1] >= join_range[1]):
                remove_ranges.append(j)
            # new_range prefixes join_range
            elif (new_range[0] < join_range[0]) and (new_range[1] >= join_range[0] - 1):
                new_range = (new_range[0], join_range[1])
                remove_ranges.append(j)
            # new_range suffixes join_range
            elif (new_range[0] <= join_range[1] + 1) and (new_range[1] > join_range[1]):
                new_range = (join_range[0], new_range[1])
                remove_ranges.append(j)
            # new_range is not connected to join_range
            else:
                pass

        remove_ranges.sort(reverse = True)
        for remove in remove_ranges:
            new_ranges.pop(remove)
        if not is_redundant:
            new_ranges.append(new_range)
    
    return new_ranges

def main():
    
    input_file: str = 'input.txt'
    fresh_ranges: list[tuple[int, int]] = []
    fresh_count: int = 0
    read_mode = ReadMode.FRESH_RANGE

    # parse file
    for line in fileinput.input(input_file):
        if len(line.strip()) == 0:
            read_mode = ReadMode.INGREDIENT
        elif read_mode == ReadMode.FRESH_RANGE:
            low, high = map(int, line.strip().split('-', maxsplit=1))
            fresh_ranges.append((low, high))
        else:
            break
    
    # simplify ID ranges
    fresh_ranges = simplify_fresh_ranges(fresh_ranges)
    print(fresh_ranges)

    # count fresh IDs
    for fresh_range in fresh_ranges:
        fresh_count += fresh_range[1] - fresh_range[0] + 1

    print('# of fresh ingredient IDs:',fresh_count)

if __name__ == '__main__':
    main()