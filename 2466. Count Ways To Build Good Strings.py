def task(low: int, high: int, zero: int, one: int):
    dp = [0] * (high + 1)
    dp[0] = 1

    for length in range(low, high + 1):
        if dp[length] > 0:
            if length + zero <= high:
                dp[length + zero] += dp[length]
            if length + one <= high:
                dp[length + one] += dp[length]

    return sum(dp[low:high + 1])

print(f"Количество хороших строк: {task(3, 3, 1, 1)}")