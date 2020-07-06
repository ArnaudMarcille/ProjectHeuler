letters = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8, 'i' : 9, 'j' : 10, 'k' : 11, 'l' : 12, 'm' : 13, 'n' : 14, 'o' : 15, 'p' : 16, 'q' : 17, 'r' : 18, 's' : 19, 't' : 20, 'u' : 21, 'v' : 22, 'w' : 23, 'x' : 24, 'y' : 25, 'z' : 26}

def GetWeight(value):
    global letters
    sum = 0
    for i in list(value):
        sum += letters[i.lower()]
    return sum

strValues = [n.strip() for n in open("22.txt", "r")]
names = strValues[0].replace("\"", "").split(',')
names.sort()
print(len(names))

sum = 0

for i in range(0, len(names)):
    weight = GetWeight(names[i])
    score = weight * (i + 1)
    sum += score

print(sum)

