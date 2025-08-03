class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num%3==0:
            chosen=num//3
            chosenList=[chosen-1,chosen,chosen+1]
            return chosenList
        else:
            return []