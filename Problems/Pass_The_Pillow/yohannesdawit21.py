def passThePillow(n, time):
    cycle = 2 * (n - 1)
    time = time % cycle

    if time < n:
        return 1 + time
    else:
        return 2 * n - 1 - time
