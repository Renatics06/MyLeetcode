def maxSumOfThreeSubarrays(nums, k):
    n = len(nums)
    window_sum = [0] * (n - k + 1)
    current_sum = sum(nums[:k])
    window_sum[0] = current_sum

    for i in range(1, n - k + 1):
        current_sum += nums[i + k - 1] - nums[i - 1]
        window_sum[i] = current_sum

    left_max = [0] * len(window_sum)
    right_max = [0] * len(window_sum)

    best_left = 0
    for i in range(len(window_sum)):
        if window_sum[i] > window_sum[best_left]:
            best_left = i
        left_max[i] = best_left

    best_right = len(window_sum) - 1
    for i in range(len(window_sum) - 1, -1, -1):
        if window_sum[i] >= window_sum[best_right]:
            best_right = i
        right_max[i] = best_right

    max_sum = 0
    result = []
    for mid in range(k, n - 2 * k + 1):
        left = left_max[mid - k]
        right = right_max[mid + k]
        total = window_sum[left] + window_sum[mid] + window_sum[right]
        if total > max_sum:
            max_sum = total
            result = [left, mid, right]

    return result

print(maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1], k = 2))