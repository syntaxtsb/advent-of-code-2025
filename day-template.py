import os
import fileinput

os.chdir('./day-x/')

def main():
    
    input_file: str = 'input.txt'

    # parse file
    lines: list[str] = [line.strip('\n') for line in fileinput.input(input_file)]

if __name__ == '__main__':
    main()