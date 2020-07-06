figures = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
decades = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
specials = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "eigtheen", "seventeen", "nineteen"]
hundreds = "hundred"
thousands = "thousand"

def ToWords(value, result):
    if(value < 10):
        return result + figures[value] + " "
    if(value < 20):
        rest = value % 10
        return result + specials[rest]
    if(value < 100):
        rest = value % 10
        index = int((value - rest) / 10)
        result = result + decades[index] + " "
        return ToWords(rest, result)    
    if(value < 1000):
        rest = value % 100
        index = int((value - rest) / 100)
        result = result + figures[index] + " " + hundreds + " "
        if(rest > 0):
            result = result + "and "
        return ToWords(rest, result)    
    if(value < 100000):
        rest = value % 1000
        index = int((value - rest) / 1000)
        result = result + figures[index] + " " + thousands + " "
        if(rest > 0):
            result = result + "and "
        return ToWords(rest, result) 
    return ""

sum = 0

# content = ToWords(115, "")
# print(content)
# for word in content.split(" "):
#         sum += len(word)

for i in range(1, 1001):
    content = ToWords(i, "")
    for word in content.split(" "):
        sum += len(word)

print(sum)

