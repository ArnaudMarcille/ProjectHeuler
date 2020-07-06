Target = 20
moveCount = 2 * Target

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

result = (factorial(moveCount)) / (factorial(Target) * factorial(moveCount - Target))

print(result)  