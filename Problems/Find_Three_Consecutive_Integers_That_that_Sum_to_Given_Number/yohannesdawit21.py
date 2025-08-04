def sumOfThree(num):
    if num % 3 != 0:
        return []
    
    x = num // 3
    return [x - 1, x, x + 1]
# Example usage
print(sumOfThree(9))  # Output: [2, 3, 4]
print(sumOfThree(12))  # Output: [3, 4, 5]
print(sumOfThree(7))  # Output: []