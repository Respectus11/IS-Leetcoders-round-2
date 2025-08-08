class Solution:
    def height_checker(self, heights: list):
        copy = [height for height in heights]
        copy.sort()
        output = 0
        for i in range(len(heights)):
            if heights[i] != copy[i]:
                output += 1
        return output
   