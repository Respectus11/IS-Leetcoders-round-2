 class Solution(object):
    def rotateString(self, s, goal):
        if(len(s)!=len(goal)): 
            return False
        s=s+s
        return True if s.find(goal)!= -1 else False
