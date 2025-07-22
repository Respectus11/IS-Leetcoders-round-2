def isPalindrome(x):
    if x < 0:
        return False
    else:
        return str(x) == str(x)[::-1]

print(isPalindrome(-121))  # Output: False
print(isPalindrome(10))    # Output: False
