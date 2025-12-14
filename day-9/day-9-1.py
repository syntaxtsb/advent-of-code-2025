import os
import fileinput
import math

os.chdir('./day-9/')

class Vector2i:

    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x: int = x
        self.y: int = y
    
    def __str__(self):
        return f'({self.x},{self.y})'

    def __repr__(self):
        return self.__str__()
    
    def distance_to(self, v: Vector2i) -> float:
        dx: int = v.x - self.x
        dy: int = v.y - self.y
        return math.sqrt((dx ** 2) + (dy ** 2))

class Rect:

    def __init__(self, a: Vector2i = Vector2i(0, 0), b: Vector2i = Vector2i(0, 0)):
        self.a = a
        self.b = b
    
    def __str__(self) -> str:
        return f'[{self.a} {self.b}]'
    
    def __repr__(self):
        return self.__str__()
    
    def width(self) -> int:
        return abs(self.b.x - self.a.x) + 1
    
    def height(self) -> int:
        return abs(self.b.y - self.a.y) + 1
    
    def area(self) -> int:
        return self.width() * self.height()
    
def main(): 
    
    input_file: str = 'input.txt'

    # parse file
    lines: list[str] = [line.strip('\n') for line in fileinput.input(input_file)]
    positions: list[Vector2i] = [Vector2i(*map(int, line.split(','))) for line in lines]

    rect: Rect = Rect()
    for pos_1 in positions:
        for pos_2 in positions:
            check_rect: Rect = Rect(pos_1, pos_2)
            print(check_rect.area())
            if (pos_1 != pos_2) and (check_rect.area() > rect.area()):
                rect = check_rect
    
    print(rect, rect.width(), rect.height(), rect.area())

if __name__ == '__main__':
    main()
