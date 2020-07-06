i = 1
last = 0
counter = 1

while len(str(i)) < 1000:
    current = last + i
    last = i
    i = current
    counter += 1

print(counter)