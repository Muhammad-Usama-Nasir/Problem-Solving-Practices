# =============================  PROBLEM DESCRIPTION  =================================
# You are given an array arr of size n - 1 that contains distinct integers in the range from 1 to n (inclusive).
# This array represents a permutation of the integers from 1 to n with one element missing. Your task is to identify and
# return the missing element.

# =============================  EXAMPLES  =================================

# Input: arr[] = [1, 2, 3, 5]
# Output: 4
# Explanation: All the numbers from 1 to 5 are present except 4.

# Input: arr[] = [8, 2, 4, 5, 3, 7, 1]
# Output: 6
# Explanation: All the numbers from 1 to 8 are present except 6.

# Input: arr[] = [1]
# Output: 2
# Explanation: Only 1 is present so the missing element is 2.


def missingNumber(arr):

    # Converting Array into set for optimal performance
    arr_set = set(arr)

    # max(arr) + 1 => used for an additional number to guess if missing
    for i in range(1, max(arr) + 1):
        # To check if specific number [i] is in the set or not
        if i not in arr_set:
            print(f"this missing number is: {i}")
            return i
    # If no number is found then Index of Last num + 1 is returned (for some rare cases)
    print(max(arr) + 1)
    return max(arr) + 1


# =============================  DUMMY DATA TO TEST FOR  =================================
# arr = [1, 2, 3, 5]
# arr = [8, 2, 4, 5, 3, 7, 1]
# arr = [1]
arr = [2, 3]

missingNumber(arr)
