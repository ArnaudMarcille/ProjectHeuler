from math import *
import time
start = time.time()

def IsPrime(value, lastPrime):
    for prime in lastPrime:
        if prime > sqrt(value):
            return True
        else:
            if(value % prime == 0):
                return False
    
    return True


basePrime = [2,3,5,7,11,13]
Found = False

i = 2
y = 0

while Found == False:
    if(IsPrime(i, basePrime)):
        y += 1
        basePrime.append(i)
        if(y == 10001):
            Found = True
    if Found == False:
        i += 1


print(i)


end = time.time()
print("--- %s seconds ---" %  (end - start))





