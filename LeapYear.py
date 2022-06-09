def LeapYear(x):
    if(x % 400 == 0):
        return "is leap year"
    elif(x % 100 == 0):
        return "NOT a leap year"
    elif(x % 4 == 0):
        return "is leap year"
    else:
        return "NOT a leap year."