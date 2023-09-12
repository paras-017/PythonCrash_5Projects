i = 0
while(i<10):
    i+=1
    if(i == 5):
        continue       #don't run for 5
    print(i)


while (True):
    num = int(input("Enter the number\n"))
    if(num == 0 or num == ''):
        break     #EXIT from the loop


print("finished incrementing")