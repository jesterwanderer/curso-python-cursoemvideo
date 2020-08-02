#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'tipPercentage' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING rating as parameter.
#

def tipPercentage(rating):
    # Write your code here

    if rating == "Terrible" or "Porr":
        return 3
    elif rating == "Good" or "Great":
        return 10
    elif rating == "Exellent":
        return 20
    else:
        return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rating = input()

    result = tipPercentage(rating)

    fptr.write(str(result) + '\n')

    fptr.close()
