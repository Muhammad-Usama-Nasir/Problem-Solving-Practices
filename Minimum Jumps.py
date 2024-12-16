# =============================  PROBLEM DESCRIPTION  =================================
# Given an array arr[] of non-negative integers. Each array element represents the maximum length of the jumps that can be
# made forward from that element. This means if arr[i] = x, then we can jump any distance y such that y ≤ x.
# Find the minimum number of jumps to reach the end of the array starting from the first element. If an element is 0,
# then you cannot move through that element.

# Note:  Return -1 if you can't reach the end of the array.


def minimum_jumps(arr):

    length = len(arr)
    i = 0
    count = 0
    if arr[i] == 0:
        return -1

    max_reach = arr[0]
    steps = arr[0]

    for i in range(1, length):

        max_reach = max(max_reach, i + arr[i])
        steps -= 1

        if steps == 0:
            count += 1
            if i >= max_reach:
                return -1
            steps = max_reach - i

        if max_reach >= length - 1:
            print(count + 1)
            return count + 1

    return -1


arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
minimum_jumps(arr)
