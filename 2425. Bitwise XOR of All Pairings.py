def xorAllNums(nums1, nums2):
    xor1 = 0
    xor2 = 0

    for num in nums1:
        xor1 ^= num

    for num in nums2:
        xor2 ^= num

    result = 0
    if len(nums2) % 2 == 1:
        result ^= xor1
    if len(nums1) % 2 == 1:
        result ^= xor2

    return result

nums1 = [2, 1, 3]
nums2 = [10, 2, 5, 0]
print(xorAllNums(nums1, nums2))