# =============================  PROBLEM DESCRIPTION  =================================
# Given an unsorted array arr containing only non-negative integers, your task is to find a continuous subarray
# (a contiguous sequence of elements) whose sum equals a specified value target. You need to return the 1-based indices
# of the leftmost and rightmost elements of this subarray.


def subArraySum(arr, target):

    # Outer loop to iterate over the whole array
    for i in range(len(arr)):
        sum = 0
        # Inner loop to get each number for sum
        for j in range(i, len(arr)):
            # Adding all the previous values in the sum until finding the target value
            sum += arr[j]
            if sum == target:
                return i + 1, j + 1

            # Breaking Early if the sum becomes greater than the target
            # Solves Time Comlexity Issue 
            if sum > target:
                break
    # In case of No Result, returning -1,'' to ot get any errors 
    return -1, ''


# =============================  DUMMY VALUES TO TEST FOR  =================================

# arr = [12, 18, 5, 11, 30, 5, 69]
# arr = [19, 23, 15, 6, 6, 2, 28, 2, 2]
# arr = [12, 18, 5, 11, 30, 5]
arr = [26, 3, 28, 7]
target = 52

subArraySum(arr, target)
