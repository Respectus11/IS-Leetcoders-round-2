class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = str(x)
        length = len(y)
        start = 0
        end = length-1

        for i in range(0,length):
            if(y[start] != y[end] ):
                return False
            start += 1
            end -= 1
        
        return True

#Example usage
sol = Solution()
print(sol.isPalindrome(121)) #True
print(sol.isPalindrome(-121)) #False

