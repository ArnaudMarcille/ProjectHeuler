def Quadratic(n):
    return (n * n) + n + 41
def Incredible(n):
    return (n *n) - (79 * n) + 1601

content = []
for i in range(0, 41):
    content.append(Quadratic(i))

print(content)