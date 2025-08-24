class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        be=sorted(heights)
        count=0
        for i in range(len(heights)):
           if heights[i] != be[i]:
             count+=1
           else :
              continue
        return count
