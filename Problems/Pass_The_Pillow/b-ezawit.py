class Solution(object):
    def passThePillow(self, n, time):
        x = 1
        d = 1
        for _ in range(time):
            x += d
            if x == n:
                d = -1
            elif x == 1:
                d = 1
        return x
