import os
import fileinput

os.chdir('./day-3/')

def find_highest_joltage(bank: str, digits: int):

    batteries: str = ''
    battery_pos: int = -1
    digit: int = 0

    while digit < digits:
        batteries += max(bank[battery_pos+1:-digits+digit])
        battery_pos: int = bank.index(batteries[-1],battery_pos+1)
        digit += 1
    
    return int(batteries)

def main():
    
    banks: list[str] = []
    joltage: list[int] = []
    input_file: str = 'input.txt'

    # parse file
    for line in fileinput.input(input_file):
        banks.append(str(line))
    
    for bank in banks:
        joltage.append(find_highest_joltage(bank, 12))

    print("Sum of maximum joltages:",sum(joltage))

if __name__ == '__main__':
    main()