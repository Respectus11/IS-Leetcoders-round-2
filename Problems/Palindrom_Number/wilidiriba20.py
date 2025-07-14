def palindrom(num):
   rev=str(num)[::-1]
   if str(num) == rev:
      return True
   else :
      return False
print(palindrom(121))
