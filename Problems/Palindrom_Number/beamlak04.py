def is_palindrome(x):
    palindrome = True
    word = str(x)
    end = len(str(x))-1
    for start in range(len(str(x))):
        if word[start] == word[end]:
            start += 1
            end -= 1
            if start > end:
                break
        else:
            palindrome = False
            break
        
    return palindrome
