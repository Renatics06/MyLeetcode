def countPalindromicSubsequence(s):
    count = ""
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                count += s[i:j] + " "
    return ???

print(countPalindromicSubsequence("bbcbaba"))