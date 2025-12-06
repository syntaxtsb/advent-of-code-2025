import os
import fileinput

os.chdir('./day-1/')

DIAL_RANGE: list[int] = [0, 100]

def main():
    
    dial: int = 50
    password: int = 0
    instructions: list[tuple] = []
    input_file: str = 'input.txt'
	
    # parse instruction file
    for line in fileinput.input(input_file):
        instructions.append((line[0], int(line[1:])))
    
    # process instructions
    for rotation in instructions:

        if rotation[0] == 'L':
            dial -= rotation[1]
        elif rotation[0] == 'R':
            dial += rotation[1]
        else:
            print('Bad rotation',rotation)

        while dial < DIAL_RANGE[0]:
            dial += DIAL_RANGE[1] - DIAL_RANGE[0]
        while dial >= DIAL_RANGE[1]:
            dial -= DIAL_RANGE[1] - DIAL_RANGE[0]

        if dial == 0:
            password += 1
    
    # display password
    print('Password: %d' % password)


if __name__ == '__main__':
    main()