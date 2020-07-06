grid = []

def ComputeNumbers(level, LastNumber):
    if(level == 0):
        return 1
    return LastNumber + 8

def FillLevel(grid, level, lastValue, lastNumber):
    center = int(len(grid) / 2)

    if(level == 0):
        grid[center][center] = 1
        return [grid, 1, 0]

    total = ComputeNumbers(level, lastNumber)
    # Fill right 
    for y in range(1, int(total/4) +1):
        x= center + level
        line = y + (center - level)
        lastValue += 1
        grid[line][x] = lastValue

    # fill but
    for x in range(int(total/4) -1, -1 ,-1):
        y = center + level
        lastValue += 1
        grid[y][x + (center - level)] = lastValue

    # fill left

    for y in range(int(total/4) -1, -1 ,-1):
        x = center - level
        line = y + (center - level)
        lastValue += 1
        grid[line][x] = lastValue

    # fill top

    for x in range(1, int(total/4) +1):
        y = center - level
        lastValue += 1
        grid[y][x + (center - level)] = lastValue

    return [grid, lastValue, total]


# 1 . 3 . 5 . 7 . 9 . . . 13 . . . 17 . . . 21 . . . 25
size = 1001
center = int(size / 2)



for y in range(0,size):
    line = []
    for x in range(0, size):
        line.append(0)    
    grid.append(line)

count = 1
lastNumber = 0

for level in range(0, int(size / 2) +1):
    result = FillLevel(grid, level, count, lastNumber)
    grid = result[0]
    count = result[1]
    lastNumber = result[2]

level = int(size / 2)
for line in range(0, size):     
    for x in range(0, size):
        if(line == center and x != center):
            grid[line][x] = 0
        elif line != center:
            if x != (center - level) and x != (center + level):
                grid[line][x] = 0
    if(line < center):
        level = level -1
    else:
        level = level +1


tot = 0

grid = result[0]
for n in grid:
    # print(n)
    tot += sum(n)

print(tot)
