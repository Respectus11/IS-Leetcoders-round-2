def passThePillow(n, time):
    current_position = 1
    direction = 1
    
    for _ in range(time):
        current_position += direction
        if current_position == n:
            direction = -1
        elif current_position == 1:
            direction = 1
    
    return current_position


def test():
    result1 = passThePillow(4, 5)
    print(f"Input: n=4, time=5, Output: {result1}")
    print(f"Simulation result: {passThePillow(4, 5)}")
    
    result2 = passThePillow(3, 2)
    print(f"\nInput: n=3, time=2, Output: {result2}")
    print(f"Simulation result: {passThePillow(3, 2)}")
    
if __name__ == "__main__":
    print("Test")
    print("=" * 30)
    test()
