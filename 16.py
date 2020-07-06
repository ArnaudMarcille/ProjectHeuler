value = 2**1000

strValue = str(value)

numbers = [int(i) for i in list(strValue)]

sum = 0
for x in numbers:
    sum += x

print(sum)