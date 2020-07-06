from math import *
import time
start = time.time()

def TriangleValue(lastvalue, value):
    return lastvalue + value

def NumberOfDivider(value):
    count = 0
    carre = int(sqrt(value))+1
    for i in range(1,carre):
        if(value % i == 0):
            if(i / value == i):
                count +=1
            else:
                count +=2

    return count

lastTriangle = 0
result = 0
i = 1

while(result == 0):
    triangle = TriangleValue(lastTriangle, i)
    lastTriangle = triangle
    i += 1       
    devider = NumberOfDivider(triangle)
    if(devider >= 500):
        result = triangle

end = time.time()
print("--- %s seconds ---" %  (end - start))
print(result)
