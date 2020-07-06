from math import *

def IsPrime(value, lastPrime):
    for prime in lastPrime:
        if prime > sqrt(value):
            return True
        else:
            if(value % prime == 0):
                return False
    
    return True

target = 2000000
basePrime = [2,3,5,7,11,13]
sum = 0

for i in range(2,target+1):
    if(IsPrime(i, basePrime)):
        basePrime.append(i)
        sum += i


print(sum)