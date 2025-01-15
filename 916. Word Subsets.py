from collections import Counter

def wordSubsets(words1, words2):
    max_count = Counter()
    print(max_count)
    for word in words2:
        count = Counter(word)
        for char, freq in count.items():
            max_count[char] = max(max_count[char], freq)
    result = []
    for word in words1:
        count = Counter(word)
        print(count)
        if all(count[char] >= freq for char, freq in max_count.items()):
            result.append(word)
        print(max_count.items())
    return result

print(wordSubsets(["amazon","apple","facebook","google","leetcode"], words2 = ["e","oo"]))