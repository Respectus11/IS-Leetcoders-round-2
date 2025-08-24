def pass_the_pillow(n,time):
    person=1   # this refers to curret person  i mean the person who holds the pillow
    direction=1 # this indicates a forward movement  ... if it was -1, i would indicate a backward movemet.
    for_in range(time):
        person+=direction
        if person==n:
            direction=-1
        if person==1:
            direction=1
        return person