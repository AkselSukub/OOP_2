import math

class Pair:
    def __init__(self, first, second):
        if not isinstance(first, (int, float)) or not isinstance(second, (int, float)):
            raise ValueError("Katety должны быть числами.")
        if first <= 0 or second <= 0:
            raise ValueError("Katety должны быть положительными числами.")
        self.first = first
        self.second = second

    def hypotenuse(self):
        return math.sqrt(self.first ** 2 + self.second ** 2)

    def read(self):
        self.first = float(input("Введите длину первого катета (позитивное дробное число): "))
        self.second = float(input("Введите длину второго катета (позитивное дробное число): "))
        if self.first <= 0 or self.second <= 0:
            raise ValueError("Katety должны быть положительными числами.")

    def display(self):
        print(f"Katety: {self.first}, {self.second}. Гипотенуза: {self.hypotenuse()}")

def make_pair(first, second):
    try:
        return Pair(first, second)
    except ValueError as ve:
        print(ve)
        exit()

if __name__ == '__main__':
    try:
        katet1 = float(input("Введите длину первого катета: "))
        katet2 = float(input("Введите длину второго катета: "))
        pair = make_pair(katet1, katet2)
        pair.display()

        print("\nСейчас вы можете ввести новые значения катетов:")
        pair.read()
        pair.display()
    except ValueError as e:
        print(e)