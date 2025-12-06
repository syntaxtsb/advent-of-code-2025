import os
import fileinput
from enum import Enum

os.chdir('./day-6/')

class Problem:
    
    def __init__(self, operands: list[int], operator: str) -> None:
        
        if len(operands) < 2:
            raise ValueError("Requires at least two operands.")
        
        self.operands = operands
        self.operator = operator
    
    def result(self) -> int:
        
        result: int = self.operands[0]

        for operand in self.operands[1:]:
            match self.operator:
                case '+':
                    result += operand
                case '-':
                    result -= operand
                case '*':
                    result *= operand
                case '/':
                    result //= operand
                case _:
                    result += operand

        return result

def generate_worksheet(lines: list[str]) -> list[Problem]:

    problems: list[Problem] = []
    tokens: list[str] = [''] * len(lines)

    for col_index in range(len(lines[0])):
        for line_num, line in enumerate(lines):
            tokens[line_num] += (line[col_index])
        if is_end_of_problem(tokens):
            problems.append(generate_problem(tokens))
            tokens = [''] * len(lines)

    if len(tokens[0]) > 0:
        problems.append(generate_problem(tokens))

    return problems

def is_end_of_problem(tokens: list[str]) -> bool:

    return all([token[-1] == ' ' for token in tokens])

def generate_problem(tokens: list[str]) -> Problem:
    
    # transpose and reverse tokens (cephalopod math format)
    operands: list[str] = [''.join([row[col_index] for row in tokens[:-1]]) for col_index in range(len(tokens[0]))]
    operands = [operand.strip() for operand in operands if operand.strip() != '']
    # Only addition and multiplication were in this cephalopod's homework, so reversing
    # operands doesn't actually matter. But we do it for completeness, since cephalopods
    # read the problem right-to-left and it would matter if non-commutative operations
    # were present in the input.
    operands.reverse()
    operator: str = tokens[-1].strip()
    print(operands, operator)
    return Problem([int(operand) for operand in operands], operator)

def main() -> None:
    
    input_file: str = 'input.txt'

    # parse file
    worksheet_lines: list[str] = [line.strip('\n') for line in fileinput.input(input_file)]
    
    # identify problems
    worksheet: list[Problem] = generate_worksheet(worksheet_lines)

    print('Sum of problem answers:', sum([problem.result() for problem in worksheet]))

if __name__ == '__main__':
    main()