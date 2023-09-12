# a = int(input("Enter the Number"))
# match a:
#     case 1:
#         print("Rating is one")
#     case 2:
#         print("Rating is on2")
#     case 3:
#         print("Rating is 3")
#     case 4:
#         print("Rating is 4")
#     case 5:
#         print("Rating is 5")
#     case _:
#         print("Default is running")


# Quick QUIZ : write a python program to print table of a number which liews between 1 and 10
num = int(input("Enter the number you want to find table"))
match num:
    case 5:
        for i in range(5,5*10+1,5):
            print(f"5 x {int(i/5)} = {i}")