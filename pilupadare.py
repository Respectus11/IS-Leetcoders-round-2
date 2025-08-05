 
def finalValueAfterOperations(operations):
    value = 0
    for operation in operations:
        if operation in ("++X", "X++"):
            value += 1
        else:
            value -= 1
    return value
