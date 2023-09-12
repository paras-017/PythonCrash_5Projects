def myFunc():
    # print("hello")
    return "hello"

# print(myFunc())

def letterGenerator(name, date):
    st = f'''Hello, Hiring Team
        my name is {name} ,
        I am a Full Stack Developer, and i am thinking to join this company on 
        {date}'''
    return st

print(letterGenerator('Paras', '3-oct-2023'))