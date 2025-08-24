def numWaterBottles(self, numBottles, numExchange):
    total_bottle=numBottles
    empty=numBottles
    while empty>=numExchange:
        new_full_bottle=empty//numExchange
        total_bottle +=new_full_bottle
        empty=empty%numExchange + new_full_bottle
    return total_bottle