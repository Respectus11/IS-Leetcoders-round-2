class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        place = 1
        movement = 1
        for i in range(time):
            place += movement
            if place ==n or place ==1:
                movement *= -1
        return place

