def isPalindrome(x):
    return str(x) == str(x)[::-1]
# Example usage
print(isPalindrome(121))  # True 
print(isPalindrome(-121))  # False