def sumOfThreeConseNum(num):
    if num % 3 != 0:
        return []
  
    middle_number = num // 3
    
    
    first_number = middle_number - 1
    second_number = middle_number
    third_number = middle_number + 1
    
    return [first_number, second_number, third_number]


def test():
    result1 =sumOfThreeConseNum(33)
    print(f"Input: 33, Output: {result1}")
    print(f"Sum check: {sum(result1)} = 33")
    
    result2 = sumOfThreeConseNum(4)
    print(f"Input: 4, Output: {result2}")
    
    
if __name__ == "__main__":
    print("Test result:")
    print("=" * 30)
    test()
    
   