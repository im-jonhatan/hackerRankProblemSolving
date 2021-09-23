# Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine(if any). The fee structure is as follows:
# 1. If the book is returned on or before the expected return date, no fine will be charged(i.e.: fine = 0).
# 2. If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, fine = 15 hackos x (the number of days late).
# 3. If the book is returned after the expected return month but still within the same calendar year as the expected return date, the fine = 500 hackos x(the number of months late).
# 4. If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000 hackos.
# Charges are based only on the least precise measure of lateness. For example, whether a book is due January 1, 2017 or December 31, 2017, if it is returned January 1, 2018, that is a year late and the fine would be 10.000 hackos.

# Example
# d1, m1, y1 = 14, 7, 2018
# d2, m2, y2 = 5, 7, 2018
# The first values are the return date and the second are the due date. The years are the same and the months are the same. The book is 14-5=9 days late. Return 9*15=135.

# Function Description
# Complete the libraryFine function in the editor below.

# libraryFine has the following parameter(s):
# - d1, m1, y1: returned date day, month and year, each an integer
# - d2, m2, y2: due date day, month and year, each an integer

# Returns
# int: the amount of the fine or if there is none

# Input Format
# The first line contains 3 space-separated integers, d1, m1, y1, denoting the respective, day, month and year on which the book was returned.
# The second line contains 3 space-separated integers, d2, m2, y2, denoting the respective, day, month and year on which the book was due to be returned.

# Constraints
# 1 ≤ d1,d2 ≤ 31
# 1 ≤ m1,m2 ≤ 12
# 1 ≤ y1,y2 ≤ 3000
# it is guaranteed that the dates will be valid Gregorian calendar dates.

# Sample Input
#     9 6 2015
#     6 6 2015

# Sample Output
#     45

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'libraryFine' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d1
#  2. INTEGER m1
#  3. INTEGER y1
#  4. INTEGER d2
#  5. INTEGER m2
#  6. INTEGER y2
#


def libraryFine(d1: int, m1: int, y1: int, d2: int, m2: int, y2: int) -> int:
    # Write your code here
    if y1 < y2:
        return 0
    if y1 > y2:
        return 10000
    if m1 < m2:
        return 0
    if m1 > m2:
        return 500 * (m1 - m2)
    if d1 < d2:
        return 0
    if d1 > d2:
        return 15 * (d1 - d2)
    return 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    d1 = int(first_multiple_input[0])

    m1 = int(first_multiple_input[1])

    y1 = int(first_multiple_input[2])

    second_multiple_input = input().rstrip().split()

    d2 = int(second_multiple_input[0])

    m2 = int(second_multiple_input[1])

    y2 = int(second_multiple_input[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()
