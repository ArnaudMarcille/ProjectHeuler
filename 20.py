def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

strValue = str(factorial(100))

numbers = [int(i) for i in list(strValue)]

sum = 0
for x in numbers:
    sum += x

print(sum)