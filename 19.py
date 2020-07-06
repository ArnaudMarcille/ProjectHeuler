monthDays = [31,28,31,30,31,30,31,31,30,31,30,31]
monthDaysLeapYear = [31,29,31,30,31,30,31,31,30,31,30,31]

def IsLeapYear(year):
    if(year % 4 !=0):
        return False
    if(year % 100 == 0):
        if(year % 400 == 0):
            return True
        else:
            return False
    else:
        return True

def GetMonthDef(month, year):
    if(IsLeapYear(year)):
        return monthDaysLeapYear[month]
    else:
        return monthDays[month]

def ComputeFirstSundayDay(lastFirstDay, month, year):
        days = GetMonthDef(month -1, year)
        value = lastFirstDay
        while value < days:
            value += 7
        return value - days

total = 0
day = 0 #First monday is 1 so first sunday is 0
for year in range(1900, 2000):
    for month in range(0,12):        
        day = ComputeFirstSundayDay(day, month, year)        
        if(day == 1):
            total += 1

print(total)