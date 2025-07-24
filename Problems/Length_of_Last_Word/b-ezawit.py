class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s) - 1
        lastword = ""
        while i>=0 and s[i] ==' ':
            i -= 1
        
        while i>=0 and s[i] != ' ':
            lastword = s[i] + lastword
            i -= 1
        return len(lastword)

sol = Solution()
s = sol.lengthOfLastWord("hello world")
print(s)
