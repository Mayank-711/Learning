year = int(input("Enter the year you want to check:"))
month = int(input("Enter the month:"))
def is_leapyear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return True
def days_in_month(year, month):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leapyear(year) and month == 2:
        return 29
    else:
        return days[month - 1]

day = days_in_month(year, month)
print(day)

