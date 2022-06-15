from cmath import pi
import math

r = float(input("Enter the radius of the circle: \t"))

def area (r): 
    area = float(pi*r*r)
    return area


A = area(r)
print (A)
