#days in month finder
print("-------->>>> DAYS IN MONTH FINDER <<<<--------\n")

# Leap Year Function
def leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year%400==0):
        return True
    else:
        return False

def days_in_month(year,month):
    """It finds the number of day for months in a leap or non 
    leap year """
    leap_result = bool(leap(year))
    leapyearmonths = [31,29,31,30,31,30,31,31,30,31,30,31]
    non_leapyearmonths = [31,28,31,30,31,30,31,31,30,31,30,31]

    if leap_result == True:
        return leapyearmonths[month-1]
    else:
        return non_leapyearmonths[month-1]

year = int(input("ENter the year: ".title()))
month = int(input("Enter the month: ".title()))
days = days_in_month(year,month)
print("Number of days are ".title(),days)