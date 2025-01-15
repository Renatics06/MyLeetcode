def minOperations(boxes):
    n = len(boxes)
    counter = [0] * n
    count = 0
    operations = 0
    for i in range(n):
        counter[i] += operations
        count += int(boxes[i])
        operations += count

    count = 0
    operations = 0
    for i in range(n - 1, -1, -1):
        counter[i] += operations
        count += int(boxes[i])
        operations += count

    return counter

print(minOperations("110"))  # Output: [1, 1, 3]
print(minOperations("001011"))  # Output: [11, 8, 5, 4, 3, 4]
