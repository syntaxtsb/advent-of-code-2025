import os
import fileinput

os.chdir('./day-7/')

# bottom-up acccumulation approach in O(n^2)

def count_timelines(manifold: list[str]) -> int:

    timelines: list[int] = [0] * len(manifold[0])
    prev_timelines: list[int] = [0] * len(manifold[0])

    for row in manifold:

        prev_timelines = timelines.copy()
        for x, cell in enumerate(row):

            if cell == '^':
                timelines[x] = aggregate_timelines(prev_timelines, x)
            elif cell == 'S':
                return aggregate_timelines(prev_timelines, x)
        
    # no entry point found; there is only one timeline
    return 1

def aggregate_timelines(timelines: list[int], x: int) -> int:

    left: int = timelines[x-1] if timelines[x-1] > 0 else 1
    right: int = timelines[x+1] if timelines[x+1] > 0 else 1
    return left + right
    
def main():
    
    input_file: str = 'input.txt'
    timelines: list[int] = []
    depth: int = 0

    # parse file
    manifold: list[str] = [line.strip('\n') for line in fileinput.input(input_file)]

    manifold.reverse() # bottom-up calculation
    print(f'Tachyon timelines: {count_timelines(manifold)}')

if __name__ == '__main__':
    main()