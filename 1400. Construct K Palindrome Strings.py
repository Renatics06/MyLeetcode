from collections import Counter


def canConstruct(s, k):
    # Count the frequency of each character
    char_count = Counter(s)

    # Count how many characters have an odd frequency
    odd_count = sum(1 for count in char_count.values() if count % 2 != 0)

    # We can form at most (odd_count + 1) // 2 palindromes, so check if we can form k
    return odd_count <= k and len(s) >= k


# Example usage
s = "cr"
k = 7
print(canConstruct(s, k))