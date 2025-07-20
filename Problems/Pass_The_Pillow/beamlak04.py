import math
def pass_the_pillow(n,time):
    people = [num for num in range(2,n + 1)]
    reverse = [num for num in range(n-1,0, -1)]
    row = math.ceil(time/(n-1))
    if row % 2 == 0:
        return reverse[(time-1) % (n-1)]
    
    return people[(time-1) % (n-1)]
