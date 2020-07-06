sumSquare = 0
squareSum = 0

for i in range(1,101):
    result = i * i
    sumSquare = sumSquare + result
    squareSum = squareSum + i


print(abs(sumSquare))

squareSum = squareSum * squareSum

print(abs(squareSum))

final = squareSum - sumSquare

print(abs(final))