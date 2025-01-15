def maxScore(s):
    lz = 0
    ro = s.count('1')
    mx = 0

    for i in range(len(s)-1):
        if s[i] == '0':
            lz += 1
        else:
            ro -= 1
        mx = max(mx, lz + ro)

    return mx

print(maxScore("1111"))