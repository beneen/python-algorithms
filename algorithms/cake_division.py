#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'largestPiece' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER_ARRAY radii
#  2. INTEGER numberOfGuests
#

def check_midpoint(midpoint, areas, number_of_guests):
    sum = 0
    for elem in areas:
        sum += elem / midpoint
    if int(sum) >= number_of_guests:
        return 1
    else:
        return 0


def binary_search(areas, number_of_guests, largest_area):
    first = 0
    last = largest_area
    mid_volume = 0
    while first <= last:
        midpoint = (first + last)/2
        check = check_midpoint(midpoint, areas, number_of_guests)
        mid_volume = midpoint
        if check == 0:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return mid_volume

def largest_piece(radii, number_of_guests):
    # Write your code here
    # to calculate radii
    pi = 3.14159265359
    areas = sorted([elem * elem * pi for elem in radii])
    largest_area = max(sorted(areas))
    remainder = [x for x in areas if x != largest_area]
    segment = largest_area / float(number_of_guests)
    remainder = [elem for elem in remainder if elem > segment]
    #areas_remove_lower_than_segment = [elem for elem in areas if elem > segment]
    if len(remainder) == 0:
        return segment
    else:
        k = binary_search(sorted(areas), number_of_guests, largest_area)
    return k


    # first intermediate solution - dividing the largest cake among all people


    #segments_larger_than_max_radius = [elem for elem in remainder if largest_area / float(numberOfGuests) < elem]
def main():
    radii_count = int(input("how many cakes").strip())

    radii = []

    for _ in range(radii_count):
        radii_item = int(input("radius of cake").strip())
        radii.append(radii_item)

    numberOfGuests = int(input("number of guests").strip())

    print(largest_piece(radii, numberOfGuests))

if __name__ == '__main__':
    main()




# #!/bin/python3
#
# import math
# import os
# import random
# import re
# import sys
#
#
#
# #
# # Complete the 'largestPiece' function below.
# #
# # The function is expected to return a STRING.
# # The function accepts following parameters:
# #  1. INTEGER_ARRAY radii
# #  2. INTEGER numberOfGuests
# #
#
# def largestPiece(radii, numberOfGuests):
#
#
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     radii_count = int(input().strip())
#
#     radii = []
#
#     for _ in range(radii_count):
#         radii_item = int(input().strip())
#         radii.append(radii_item)
#
#     numberOfGuests = int(input().strip())
#
#     result = largestPiece(radii, numberOfGuests)
#
#     fptr.write(result + '\n')
#
#     fptr.close()