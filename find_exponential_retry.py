# this is doing exponential retry operation already
#Math.min(random * minTimeout * Math.pow(factor, attempt), maxTimeout)
# http://dthain.blogspot.com/2009/02/exponential-backoff-in-distributed.html
# https://www.npmjs.com/package/retry
import math
import random

maxTimeout = 20 * 1000
minTimeout = 5 * 1000
factor = 2
for attempt in range(1, 4):
    randNumber = random.random()
    delay = min(randNumber * minTimeout * math.pow(factor, attempt),
                maxTimeout)
    print(delay)