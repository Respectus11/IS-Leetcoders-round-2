class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        ka = str(x)
        return ka == ka[::-1]
