import math
import time
t = time.time()

def Quadratic(n, a, b):
    return (n*n) + a*n + b

# primes = []

# for possiblePrime in range(2, 10000):
#      # Assume number is prime until shown it is not. 
#     isPrime = True
#     for num in range(2, int(possiblePrime ** 0.5) + 1):
#         if possiblePrime % num == 0:
#             isPrime = False
#             break
      
#     if isPrime:
#         primes.append(possiblePrime)

def IsPrime(n):
    for i in range(2, math.floor(math.sqrt(abs(n))) + 1):
        if n % i == 0:
            return False
    return True
 
maxX = 0
maxY = 0
counter = 0

for x in range(-1000, 1000):
    for y in range(-1000,1000):
        if IsPrime(y):
            count = 0
            i = 0
            cont = True
            while cont:
                i += 1
                if IsPrime(Quadratic(i, x, y)) is False:
                    cont = False
                else:
                    count += 1
            
            if(count > counter):
                maxX = x
                maxY = y
                counter = count

print(str(maxX) + " " + str(maxY) + " " + str(counter))

print("result is :" + str(maxX * maxY))
print("========== Done in " + str(time.time() - t) + " seconds ===========")