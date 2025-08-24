class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ke= s.split( )
        count=0
        b=ke[len(ke)-1]
        for i in b:
            count+=1
        return count
