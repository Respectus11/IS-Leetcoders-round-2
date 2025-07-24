class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):
            return False

        for i in range(len(s)):
            c = s[0]
            s = s[1:]
            s += c
            
            if s == goal:
                return True
        
        return False
        
        