import os
import fileinput

os.chdir('./day-7/')

def main():
    
    input_file: str = 'input.txt'
    splits: int = 0
    active_manifold: list[str] = []
    prev_line: str = ''

    # parse file
    lines: list[str] = [line.strip('\n') for line in fileinput.input(input_file)]

    for y, line in enumerate(lines):

        active_line: str = line

        if len(active_manifold) > 0:
            for x, cell in enumerate(line):
                if prev_line[x] == 'S':
                    active_line = '|'.join([active_line[:x],active_line[x+1:]])
                if prev_line[x] == '|':
                    if cell == '^':
                        active_line = '|'.join([active_line[:x-1],'^',active_line[x+2:]])
                        splits += 1
                    else:
                        active_line = '|'.join([active_line[:x],active_line[x+1:]])
        
        active_manifold.append(active_line)
        prev_line = active_line
    
    print(active_manifold)
    print('Beam splits:',splits)

if __name__ == '__main__':
    main()