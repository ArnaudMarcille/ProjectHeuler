def cycle_length(den):
    reste = 10
    i = 0
    #Calcul des décimales tant que le reste n'est pas égal à 10
    while reste != 10 or i < 1:
        reste = (reste % den) * 10
        i += 1
    return i

maxCycle = 0
maxValue = 0
for i in range(2, 1001):
    if i % 5 != 0 and i % 2 != 0:
        length = cycle_length(i)
        if(length > maxValue):
            maxValue = length
            maxCycle = i

print(maxCycle)
print(maxValue)
