def water_bottles(numBottles, numExchange):
    max_drink = numBottles
    while numBottles >= numExchange:
        max_drink += numBottles // numExchange
        numBottles = numBottles // numExchange + numBottles % numExchange
    return max_drink
