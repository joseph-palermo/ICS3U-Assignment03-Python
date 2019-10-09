#!/usr/bin/env python3

# Created by: Joseph Palermo
# Created on: October 2019
# This program calculates the roots of a quadratic function

import math

def main():
    # This function calculates the roots of a quadratic function

    # input
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    c = float(input("Enter the value of c: "))
    # discriminant
    d = (b**2) - (4*a*c)

    # process and output
    if d > 0:
        x1 = ((-b) + (math.sqrt(d))) / (2*a)
        x2 = ((-b) - (math.sqrt(d))) / (2*a)
        print("")
        print("The two roots are: \n x1 = {:,.2f} \n and \n x2 = {:,.2f}"
        .format(x1, x2))
    elif d == 0:
        x3 = (-b) / (2*a)
        print("The root is {:,.2f}"
              .format(x3))
    elif d < 0:
        print("There are no roots")
    else:
        print("Please put in numerical values")


if __name__ == "__main__":
    main()
