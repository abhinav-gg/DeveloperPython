import math

UNIT = "#"

def get_distance(point_1, point_2):
    x1, y1 = point_1
    x2, y2 = point_2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def print_square(side_length):
    for _ in range(side_length):
        print(UNIT * side_length)

def print_rectangle(width, height):
    for _ in range(height):
        print(UNIT * width)

def print_circle(radius):
    for y in range(2 * radius + 1):
        for x in range(2 * radius + 1):
            if get_distance((x, y), (radius, radius)) <= radius:
                print(UNIT, end="")
            else:
                print(" ", end="")
        print()

def print_triangle(height):
    for y in range(height):
        for x in range(y + 1):
            print(UNIT, end="")
        print()

has_quit = False
while not has_quit:
    choice = input("""Enter a number to choose:
    1) Square
    2) Rectangle
    3) Circle
    4) Triangle
    5) Quit
    """)
    if choice == "1":
        side_length = int(input("Enter side length: "))
        print_square(side_length)
    elif choice == "2":
        width = int(input("Enter width: "))
        height = int(input("Enter height: "))
        print_rectangle(width, height)
    elif choice == "3":
        radius = int(input("Enter radius: "))
        print_circle(radius)
    elif choice == "4":
        height = int(input("Enter height: "))
        print_triangle(height)
    elif choice == "5":
        has_quit = True
    else:
        print("Invalid choice")