import math
import time

def SumOfDivider(value):
    devider = []
    carre = int(math.sqrt(value)) + 1 
    for i in range(1,carre):
        if(value % i == 0):
            devider.append(i)
            if(i * i != value):
                devider.append(value / i)
    return sum(devider) - value 


abundant = []
sumable = []

t = time.time()

for i in range(1, 28124):
    if i < SumOfDivider(i):
        abundant.append(i)

    founded = False
    for item in reversed(abundant):
        founded = (i - item) in abundant
        if(founded):
            break
    
    if(founded == False):
        sumable.append(i)


total = sum(sumable)
print(total)
print(time.time() - t)