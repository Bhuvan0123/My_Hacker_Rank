# Given two arrays of integers, find which elements in the second array are missing from the first array.

# Example


# The  array is the orginal list. The numbers missing are .

# Notes

# If a number occurs multiple times in the lists, you must ensure that the frequency of that number in both lists is the same. If that is not the case, then it is also a missing number.
# Return the missing numbers sorted ascending.
# Only include a missing number once, even if it is missing multiple times.
# The difference between the maximum and minimum numbers in the original list is less than or equal to .
from collections import Counter
def missingNumbers(arr, brr):
    return sorted((Counter(brr)-Counter(arr)).keys())