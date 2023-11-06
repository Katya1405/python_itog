class Rectangle:

    def __init__(self, length, width):

        self.length = length

        self.width = width

    def __add__(self, other):

        perimeter = self.length + self.width + other.length + other.width

        return Rectangle(perimeter // 2, perimeter // 4)

    def __sub__(self, other):

        if self.length + self.width < other.length + other.width:
            raise ValueError("Cannot subtract a larger rectangle from a smaller one.")

        perimeter = (self.length + self.width - other.length - other.width) // 2

        return Rectangle(perimeter // 2, perimeter // 4)

    def __eq__(self, other):

        return self.length * self.width == other.length * other.width

    def __ne__(self, other):

        return self.length * self.width != other.length * other.width

    def __lt__(self, other):

        return self.length * self.width < other.length * other.width

    def __le__(self, other):

        return self.length * self.width <= other.length * other.width

    def __gt__(self, other):

        return self.length * self.width > other.length * other.width

    def __ge__(self, other):

        return self.length * self.width >= other.length * other.width

    if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(description='Program for working with rectangles.')

    parser.add_argument('length1', type=int, help='length of the first rectangle')

    parser.add_argument('width1', type=int, help='width of the first rectangle')

    parser.add_argument('length2', type=int, help='length of the second rectangle')

    parser.add_argument('width2', type=int, help='width of the second rectangle')

    args = parser.parse_args()

    rectangle1 = Rectangle(args.length1, args.width1)

    rectangle2 = Rectangle(args.length2, args.width2)

    print("Rectangle 1:", rectangle1.length, "x", rectangle1.width)

    print("Rectangle 2:", rectangle2.length, "x", rectangle2.width)

    print("Sum:", rectangle1 + rectangle2)

    print("Difference:", rectangle1 - rectangle2)

    print("Equal:", rectangle1 == rectangle2)

    print("Not equal:", rectangle1 != rectangle2)

    print("Less than:", rectangle1 < rectangle2)

    print("Less than or equal:", rectangle1 <= rectangle2)

    print("Greater than:", rectangle1 > rectangle2)

    print("Greater than or equal:", rectangle1 >= rectangle2)