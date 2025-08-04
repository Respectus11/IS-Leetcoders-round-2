class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total=numBottles
        empty=numBottles

        while empty>=numExchange:
            newFull=empty//numExchange
            total+=newFull
            empty=empty % numExchange + newFull
        return total
        