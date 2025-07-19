class Solution:
    def passThePillow(self, n, time):
        cycle = time // (n - 1)
        index = time % (n - 1)
        
        if cycle % 2 == 0:
            return 1 + index
        else:
            return n - index
