def heightChecker(heights):
    expected = sorted(heights)
    count = 0
    for i in range(len(heights)):
        if heights[i] != expected[i]:
            count += 1
    return count
# Example usage
print(heightChecker([1, 1, 4, 2, 1, 3]))  # Output: 3
print(heightChecker([5, 1, 2, 3, 4]))  # Output: 5
print(heightChecker([1, 2, 3, 4, 5]))   # Output: 0