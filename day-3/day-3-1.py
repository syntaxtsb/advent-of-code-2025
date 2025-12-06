import os
import fileinput

os.chdir('./day-3/')

def find_highest_joltage(bank: str):

    batteries: str = ''

    # get highest possible first digit
    batteries = max(bank[:-2])
    battery_pos: int = bank.index(batteries)
    # get highest possible second digit
    batteries += max(bank[battery_pos+1:])
    
    return int(batteries)

def main():
    
    banks: list[str] = []
    joltage: list[int] = []
    input_file: str = 'input.txt'

    # parse file
    for line in fileinput.input(input_file):
        banks.append(str(line))
    
    for bank in banks:
        joltage.append(find_highest_joltage(bank))

    print("Sum of maximum joltages:",sum(joltage))

if __name__ == '__main__':
    main()