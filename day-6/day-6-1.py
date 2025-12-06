import os
import fileinput

os.chdir('./day-6/')

def main():
    
    input_file: str = 'input.txt'

    # parse file
    for line in fileinput.input(input_file):
        pass

if __name__ == '__main__':
    main()