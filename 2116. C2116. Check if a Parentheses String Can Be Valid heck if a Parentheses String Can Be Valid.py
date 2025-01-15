def canBeValid(s: str, locked: str) -> bool:
    if len(s) % 2 != 0:
        return False

    n = len(s)
    minOpen, maxOpen = 0, 0

    for i in range(n):
        if locked[i] == '1':
            if s[i] == '(':
                minOpen += 1
                maxOpen += 1
            else:
                minOpen -= 1
                maxOpen -= 1
        else:
            minOpen -= 1
            maxOpen += 1

        minOpen = max(minOpen, 0)

        if maxOpen < 0:
            return False

    minOpen, maxOpen = 0, 0
    for i in range(n - 1, -1, -1):
        if locked[i] == '1':
            if s[i] == ')':
                minOpen += 1
                maxOpen += 1
            else:
                minOpen -= 1
                maxOpen -= 1
        else:

            minOpen -= 1
            maxOpen += 1

        minOpen = max(minOpen, 0)

        if maxOpen < 0:
            return False

    return minOpen == 0

print(canBeValid("))()))", "010100"))  # Output: True