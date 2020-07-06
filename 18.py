strValues = [n.strip() for n in open("18.txt", "r")]
values = []
for val in strValues:
    values.append([int(n) for n in val.split(" ")])

def GetChild(level, index):
    childs = []
    global values
    
    if(level == len(values) -1):
        return childs

    nextLevel = values[level + 1]
    childs.append(nextLevel[index])
    childs.append(nextLevel[(index+1)])


    return childs

def ComputeMax(level, index):
    childs = GetChild(level, index)
    max = childs[0]
    if max < childs[1]:
        max = childs[1]    
    return max

max = 0
for n in range(len(values)-2, -1 , -1):
    for x in range(0, len(values[n])):
        values[n][x] = ComputeMax(n,x) + values[n][x]

print(values[0][0])

