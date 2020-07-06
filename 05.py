import time
start = time.time()

result = 0
i = 0
counter = 1

def DevideBy(value, devider):
    if(devider == 1):
        return True
    else:
        if(value % devider == 0):
            return DevideBy(value, devider-1)
        else:
            return False


while result < 1:
    if(DevideBy(i, 20) and i != 0):
        result = i
    else:
        i = counter * 20
        counter = counter +1
    

print("Sucess")
end = time.time()
print(result)
print("--- %s seconds ---" %  (end - start))