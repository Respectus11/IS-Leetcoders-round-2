class Solution:
    def isPalindrome(self, s):
        cleaned = ''
        for char in s:
            if char.isalnum():
                cleaned += char.lower()
        
        reversed_cleaned = cleaned[::-1]
        return cleaned == reversed_cleaned
