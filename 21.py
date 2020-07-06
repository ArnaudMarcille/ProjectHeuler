
target = 10000
sums = []
def SumOfDivisible(target):
    final = int(target / 2) + 1
    sum = 0
    for i in range(1,final):    
        if target % i == 0:
            sum += i
    return sum

for i in range(1,target+1):    
    sums.append(SumOfDivisible(i))

sumOfPair = 0
lis = []
for i in range(1, target):
    for y in  range(i + 1, len(sums)):
        if(sums[i-1] == y and sums[y-1] == i):
            sumOfPair += y + i
            lis.append([i,y])



print(sumOfPair)
print(lis)
