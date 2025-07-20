def rotate_string(s, goal):
    for i in range(len(s)-1):
        if s == goal:
            return True
        s = s +  s[0]
        s = s.replace(s[0], "", 1)        
    return False

