class Solution(object):
    def lengthOfLastWord(self, s):
        s=s.rstrip()
        length=len(s)-1
        count=0
        while length >=0 and s[length]!=' ':
                count+=1
                length-=1
        return count
        """
        :type s: str
        :rtype: int
        """
        