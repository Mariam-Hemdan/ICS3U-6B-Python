#!/usr/bin/env python3

# Created by : Mariam Hemdan
# Created on : November 2019
# This function calculate perimeter of circle

import math


def calculate_perimeter(radius):
    # calculate perimeter of circle

    # process
    perimeter = 2 * math.pi * radius
    return perimeter


def main():
    # this function gets the radius

    # input
    radius = (input("Enter the radius:"))
    print("")

    # process
    try:
        radius_as_int = int(radius)
        solution = calculate_perimeter(radius=radius_as_int)
        print("The perimeter is {0}cm".format(solution))
    except Exception:
        print("Try again")


if __name__ == "__main__":
    main()
