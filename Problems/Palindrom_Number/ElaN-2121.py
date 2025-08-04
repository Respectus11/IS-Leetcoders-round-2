class Solution(object):
    def palindrome(self,number):
        input=str(number)
        left=0
        right=len(input)-1
        while(left<right):
            if input[left]==input[right]:
                left+=1
                right-=1
            else:
                return False
        return True