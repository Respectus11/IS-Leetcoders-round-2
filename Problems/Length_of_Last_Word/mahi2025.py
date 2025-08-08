def lengthOfLastWord(s):
    words = [word for word in s.split(' ') if word]
    return len(words[-1]) if words else 0


def test():
    result1 = lengthOfLastWord("Hello World")
    print(f"Input: 'Hello World', Output: {result1}")
    print(f"Last word: 'World'")
    
   
    result2 = lengthOfLastWord("   fly me   to   the moon  ")
    print(f"Input: '   fly me   to   the moon  ', Output: {result2}")
    print(f"Last word: 'moon' ")
    
if __name__ == "__main__":
    print("Test result")
    print("=" * 30)
    test()
