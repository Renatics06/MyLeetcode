def findThePrefixCommonArray(A, B):
    n = len(A)
    C = [0] * n
    seenA = set()
    seenB = set()

    for i in range(n):
        seenA.add(A[i])
        seenB.add(B[i])
        C[i] = len(seenA & seenB)

    return C