import random

class Solution(object):
    def sortArray(self, nums):
        self.quickSort3Way(nums, 0, len(nums) - 1)
        return nums

    def quickSort3Way(self, arr, low, high):
        if low >= high:
            return

    
        pivot_index = random.randint(low, high)
        arr[low], arr[pivot_index] = arr[pivot_index], arr[low]
        pivot = arr[low]

        lt = low    
        gt = high      
        i = low + 1    

        while i <= gt:
            if arr[i] < pivot:
                arr[lt], arr[i] = arr[i], arr[lt]
                lt += 1
                i += 1
            elif arr[i] > pivot:
                arr[i], arr[gt] = arr[gt], arr[i]
                gt -= 1
            else: 
                i += 1

        self.quickSort3Way(arr, low, lt - 1)
        self.quickSort3Way(arr, gt + 1, high)
