from collections import Counter

def minimumLength(s):
    count = list(Counter(s).values())
    sum_ = 0
    for i in range(len(count)):
        count[i] %= 2
        if count[i] == 0:
            count[i] = 2
        sum_+=count[i]
    return sum_
print(minimumLength("abaacbcbb"))