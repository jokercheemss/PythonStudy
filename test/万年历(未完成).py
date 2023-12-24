#打印日历
def isLeep(y):
    return y%400 == 0 or y%4 == 0 and y%100!=0
def maxDays(y,m):
    d = 30
    if m == 1or m==3 or m ==5 or m==7 or m ==8 or m ==10 or m ==12:
        d ==31
    elif m ==2:
        d =29 if isLeep(y) else 28
        return d
def countDays(y,m,d):
    days =d
    if m>=2:
        days+=31
    if m>=3:
        days+=29 if isLeep(y) else 28
    if m>=4:
        days+=31
    if m >= 5:
         days += 31
    if m >= 6:
        days += 31
    if m >= 7:
        days += 31
    if m >= 8:
        days += 31
    if m >= 9:
        days += 31
    if m >= 10:
        days += 31
    if m >= 11:
        days += 31
    if m >= 12:
        days += 31
        return days
def cw(y,m):
    w =(y -1)+(y -1)//400+(y)

