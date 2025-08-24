class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        ka = []
        xe = []

        for i in range(1,n*2):
            ka.append(n * i)

        for j in range(1,n*2):
            xe.append(2 * j)

        for k in ka:
            for z in xe:
                if k == z:
                    return k
