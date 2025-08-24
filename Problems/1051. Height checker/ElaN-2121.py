class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        theSorted=sorted(heights)
        yes=0
        for i in range(len(heights)):
            if heights[i]!=theSorted[i]:
                yes+=1
        return yes