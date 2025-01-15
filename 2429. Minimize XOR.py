def minimizeXor(num1, num2):
    target_bits = bin(num2).count('1')

    x = 0

    for i in range(31, -1, -1):
        if target_bits == 0:
            break
        if num1 & (1 << i):
            x |= (1 << i)
            target_bits -= 1

    for i in range(32):
        if target_bits == 0:
            break
        if not (x & (1 << i)):
            x |= (1 << i)
            target_bits -= 1

    return x

print(minimizeXor(3, 5))