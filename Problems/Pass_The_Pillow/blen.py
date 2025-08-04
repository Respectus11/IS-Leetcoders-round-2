def passThePillow(n: int, time: int) -> int:
    be = []
    while len(be) <= time:
        for i in range(1, n + 1):
            if len(be) <= time:
                be.append(i)
            else:
                break
        for j in range(n - 1, 0, -1):
            if len(be) <= time:
                be.append(j)
            else:
                break
    return be[time]

print(passThePillow(4, 5))  # Output: 2 ✅

