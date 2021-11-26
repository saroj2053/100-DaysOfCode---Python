# Area Calc
import math
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5


def paint_calc(height, width, cover):
    num_of_cans = math.ceil((height * width) / cover)
    print(f"You will need {num_of_cans} cans of paint.")


paint_calc(height=test_h, width=test_w, cover=coverage)