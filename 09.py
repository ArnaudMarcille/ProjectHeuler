target = 1000

def IsTriplet(a, b, c):
    return (a*a + b*b == c*c)

result = 0

for a in range(1,target):
    for b in range(a, target):
        for c in range(b, target):
            if IsTriplet(a,b,c) and a + b + c == target:
                result = a * b * c
                print(a)
                print(b)
                print(c)
                break
        if result != 0:
            break
    if result != 0:
        break


print(result)
