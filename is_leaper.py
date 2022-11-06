def is_leap(year):
    leap = False

    if (not(year & 3 or year & 15 and not(year % 25))):
        return (not(leap))
    return (leap)

year = int(input())
print(is_leap(year))
