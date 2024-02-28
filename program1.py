month = int(input("Type the number of a month: "))

s = ("winter", "spring", "summer", "autumn")

if month in (12, 1, 2):
    ss = s[0]
elif month in (3, 4, 5):
    ss = s[1]
elif month in (6, 7, 8):
    ss = s[2]
elif month in (9, 10, 11):
    ss = s[3]
else:
    ss = "Invalid month number"

print("The season for this month is:",ss)