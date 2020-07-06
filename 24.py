base = [0,1,2]

def swap(elements, i, j):
    elements[i], elements[j] = elements[j], elements[i]

def NextHighestWord(string):
    S = [ord(i) for i in string]
    #find non-incresing suffix from last
    i = len(S) - 1
    while i > 0 and S[i-1] >= S[i]:
        i = i - 1
    if i <= 0:
        return string

    #next element to highest is pivot
    j = len(S) - 1
    while S[j] <= S[i -1]:
        j = j - 1
    S[i-1],S[j] = S[j],S[i-1]

    #reverse the suffix
    S[i:] = S[len(S) - 1 : i-1 : -1]
    ans = [chr(i) for i in S]
    ans = "".join(ans)
    return ans
   


print("Start !!")
result = "0123456789"
i = 1
while i < 1000000:
    if(1000000 * 0.25 == i):
        print("25 % !!")
    elif (1000000 * 0.5 == i):
        print("50 % !!")
    elif (1000000 * 0.75 == i):
        print("75 % !!")

    result = NextHighestWord(result)
    i +=1

print(result)