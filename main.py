# This is a sample Python script.
import math


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Point:
    def move(self, x, y):
        self.x = x
        self.y = y
    def reset(self):
        self.move(0, 0)
    def calculate_distance(self, other_point):
        return math.sqrt(
            (self.x - other_point.x) ** 2
                + (self.y - other_point.y) ** 2

        )

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    point1 = Point()
    point2 = Point()

    point1.reset()
    point2.move(5, 0)
    print(point2.calculate_distance(point1))

    point1.move(3, 4)
    print(point1.calculate_distance(point2))
    print(point1.calculate_distance(point1))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
