def is_palindrome(X):
    if x<0:
        return False
    original_num=X
    reversed_num=0
    while x>0:
        reversed_num=reversed_num*10 + (X%10)
        x=x//10
    if original_num==reversed_num:
        return True
        