class Solution:
    def merge(self,  left, right):
        output = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                output.append(left[i])
                i += 1
            else:
                output.append(right[j])
                j += 1
        while i < len(left):
            output.append(left[i])
            i += 1
        while j < len(right):
            output.append(right[j])
            j += 1
        return output
    

    def mergeSort(self, unsortedArray):
        start = 0
        end = len(unsortedArray)-1
        if start < end:
            midPoint = (start + end) // 2
            return self.merge(self.mergeSort(unsortedArray[start:midPoint+1]),self.mergeSort(unsortedArray[midPoint+1: end + 1]))
        return unsortedArray[start:end +1]