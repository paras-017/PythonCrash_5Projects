import datetime
presentYear = datetime.date.today().year

BornYear = int(input("Enter the year you were born\n"))
# print(type(BornYear))                 #way to check type in python in JS we use typeof(354)
print(f'Your age is {presentYear-BornYear}')
