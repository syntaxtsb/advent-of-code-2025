import os
import fileinput
import csv

os.chdir('./day-2/')

def find_invalid_ids(id_range: tuple[int, int]):
    
    # IDs represented by *a sequence of digits repeated twice* are invalid
    invalid_ids = []

    for id in range(id_range[0], id_range[1] + 1):
        if int(len(str(id)) % 2) == 0:
            seq_length: int = len(str(id)) // 2
            if str(id)[:seq_length] == str(id)[seq_length:]:
                invalid_ids.append(id)
                
    return invalid_ids

def main():
    
    invalid_ids: list[int] = []
    ranges: list[tuple] = []
    input_file: str = 'input.txt'

    # parse file
    for line in csv.reader(fileinput.input(input_file), delimiter=','):
        for item in line:
            low, high = map(int, item.split('-', maxsplit=1))
            ranges.append((low, high))

    for range in ranges:
        invalid_ids.extend(find_invalid_ids(range))
    
    print(invalid_ids)
    print('Sum of IDs: %d' % sum(invalid_ids))

if __name__ == '__main__':
    main()