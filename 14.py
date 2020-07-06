def CollatzCompute(value):
    if(value % 2 == 0):
        return value / 2
    else:
        return 3 * value + 1

def CollatzLength(value):
    x = value
    counter = 1
    while(x != 1):
        x = CollatzCompute(x)
        counter +=1
    return counter

maximum = 0
identifier = -1

for i in range(1000000,1, -1):
    val = CollatzLength(i)
    if(val > maximum):
        maximum = val
        identifier = i

print(identifier, "with", maximum, "terms")
       