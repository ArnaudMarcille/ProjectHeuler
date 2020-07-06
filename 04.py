def reverse(value): 
    listValue = [d for d in str(value)]
    reversed = listValue[::-1]    
    return int("".join(reversed)) 

def IsPalindrome(value):
    reversed = reverse(value)
    return reversed == value


max = 0

for i in range (100,999):
    for y in range(100, 999):
        result = i*y
        if IsPalindrome(result) and result > max:
            max = result

print(max)

