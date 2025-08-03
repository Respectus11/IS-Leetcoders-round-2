

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        ka = []
        for i in range(len(nums)-1, -1, -1):  # Fix the range step
            ka.append(nums[i])
        ka.sort()  # Sorts in-place
        return ka  # Return the sorted list
