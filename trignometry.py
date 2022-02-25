"""The Module is a file that contains related Functions and classes"""


import math 
from math import sqrt as sq

from pyrsistent import b

def area_of_triangle(length, width,  unit = "meters"):
    area = (length*width)/2
    #return f"{area} {unit}"
    return area, unit

def check_right_triangle(a,b,c): # per , base , hypt
    # Pthogorous Theorem
    # H2 = B2 + P2
    # c2 = a2 + b2

    if (sq(c) == (sq(a) + sq(b))):
        print("Right Triangle")
    else:
        return ("The Triangle is not a Right Triangle")

print("Print Function")