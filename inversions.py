def maxInversions(arr):
    n = len(arr)
    count = 0

    # Create arrays to store the number of elements greater than arr[i] to the left
    # and the number of elements smaller than arr[i] to the right
    greater_left = [0] * n
    smaller_right = [0] * n

    # Fill the greater_left array
    for i in range(1, n):
        for j in range(i):
            if arr[j] > arr[i]:
                greater_left[i] += 1

    # Fill the smaller_right array
    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                smaller_right[i] += 1

    # Calculate the number of inversions
    for i in range(n):
        count += greater_left[i] * smaller_right[i]

    return count

arr = [5,3,4,2,1]
print("Maximum number of inversions:", maxInversions(arr))

arr = [4,2,2,1]
print("Maximum number of inversions:", maxInversions(arr))

arr = [4,2, 3, 2,1]
print("Maximum number of inversions:", maxInversions(arr))