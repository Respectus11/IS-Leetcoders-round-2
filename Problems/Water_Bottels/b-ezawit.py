class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        result = numBottles     
        empty = numBottles      

        while empty >= numExchange:
            exchanged = empty // numExchange    
            result += exchanged                
            empty = empty % numExchange + exchanged  

        return result
