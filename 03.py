def devider(value):
    number = 13195 
    contin = True
    while(contin):
        if value % number == 0:
            contin = False
        else:
            number -= 1
    
    return number

baseValue = 6857

print(devider(baseValue))






