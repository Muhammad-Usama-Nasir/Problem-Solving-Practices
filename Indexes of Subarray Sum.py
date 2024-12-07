class IndexesOfSubarraySum:
    def main():
        arr = [12, 18, 5, 11, 30, 5, 69]
        # arr = [19, 23, 15, 6, 6, 2, 28, 2, 2]
        target = 69

        for i in range(len(arr) - 1):
            sum = 0
            for num in arr[i:]:
                sum = sum + num
                if sum == target:
                    print(f"The sum of elements from {i+1} to {arr.index(num)+1} is: {sum}")
                    return i+1, arr.index(num)+1
                else:
                    continue


IndexesOfSubarraySum.main()
