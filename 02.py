sum = 0
i = 1
last = 0

while last <= 4000000:
    current = last + i
    if current % 2 == 0:
        sum += current
    last = i
    i = current


print(sum)
    