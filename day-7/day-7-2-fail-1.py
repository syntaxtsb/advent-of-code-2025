import os
import fileinput

os.chdir('./day-7/')

# top-down recursive simulation is too slow to compute this...O(2^n)

class Manifold:

    def __init__(self, rows: list[str]) -> None:

        self.rows: list[str] = rows
    

    def count_timelines(self) -> int:

        depth, beam = self.locate_beam_entry()

        if depth < 0 or depth > len(self.rows) - 1:
            return 1
        else:
            return self.simulate_timelines(depth + 1, beam)

    def locate_beam_entry(self) -> tuple[int, int]:
        
        depth: int = 0

        while depth < len(self.rows) and self.rows[depth].find('S') == -1:
            depth += 1
        
        if depth < len(self.rows) - 1:
            return (depth, self.rows[depth].find('S'))
        else:
            return (-1, 0)

    def simulate_timelines(self, depth: int, beam: int) -> int:
    
        # beam reaches end of manifold
        if depth + 1 >= len(self.rows):
            return 1
        else:
            row: str = self.rows[depth]
            # beam hits wall of manifold
            #if beam < 0 or beam >= len(row):
            #    return 0
            # beam hits spltiter
            if row[beam] == '^':
                return self.simulate_timelines(depth + 1, beam - 1) + self.simulate_timelines(depth + 1, beam + 1)
            # beam continues through empty space
            else:
                return self.simulate_timelines(depth + 1, beam)

def main():
    
    input_file: str = 'input.txt'
    splits: int = 0
    active_manifold: list[str] = []
    prev_line: str = ''

    # parse file
    lines: list[str] = [line.strip('\n') for line in fileinput.input(input_file)]

    manifold = Manifold(lines)
    
    print(f'Tachyon timelines: {manifold.count_timelines()}')

if __name__ == '__main__':
    main()