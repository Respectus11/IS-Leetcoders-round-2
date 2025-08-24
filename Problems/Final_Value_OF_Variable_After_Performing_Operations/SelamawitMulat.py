def finalValueAfterOperation(self,operations):
    X=0
    for op in operations:
        if op=="++X" or op=="X++":
            X+=1
        else:
            X-=1
    return X