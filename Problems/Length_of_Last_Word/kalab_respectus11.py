class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
# first lets remove spaces using strip fun
# also split string into word
        holder = s.strip() 
        holder = holder.split()
        return len (holder[-1]) 