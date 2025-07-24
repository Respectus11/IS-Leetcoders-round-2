class Solution:
    def numWaterBottles(self, numBottles, numExchange):
        total = numBottles
        empty = numBottles

        while empty >= numExchange:
            new_full = empty // numExchange
            total += new_full
            empty = new_full + (empty % numExchange)
        
        return total
