import os

print('This is robo speaker')

while True:
    x = input("Enter what you want me to speak: ")
    if x == 'q':
        print('Bye bye, friend')
        break
    command = f"espeak '{x}'"
    os.system(command)