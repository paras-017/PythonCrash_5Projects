try:
    a = int(input('Enter the number\n'))
    print(a+5)
except:
    print('Some error occured')


try:
    b = int(input('Enter the number\n'))
    print(a+b)
except Exception as e:                        #Information about error
    print(f"Error is {e}")
