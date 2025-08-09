class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        a = list(s)
        b = list(goal)
     
        for i in range(len(a)):
            k = a[0]            # take first element
            a.remove(k)         # remove it
            a.append(k)         # put it at the end
            if a == b:          # check full list, not single chars
                return True
        return False            # if no match found

              