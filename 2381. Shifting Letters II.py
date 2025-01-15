def shiftingLetters(s, shifts):
    n = len(s)
    delta = [0] * (n + 1)

    for start, end, direction in shifts:
        if direction == 1:
            delta[start] += 1
            delta[end + 1] -= 1
        else:
            delta[start] -= 1
            delta[end + 1] += 1

    current_shift = 0
    result = []
    for i in range(n):
        current_shift += delta[i]
        shift = current_shift % 26

        new_char = chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a'))
        result.append(new_char)

    return ''.join(result)

s = "abc"
shifts = [[0, 1, 0], [1, 2, 1], [0, 2, 1]]
print(shiftingLetters(s, shifts))