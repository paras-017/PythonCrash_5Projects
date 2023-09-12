s = 'Harry is a good boy.'

# Writing to file
with open("sample.txt",'w') as f:
    f.write(s)

# Appending to a file 
with  open("sample.txt", 'a') as f:
    f.write(" This line should  append in the last")

# Reading a file
with open("sample.txt", 'r') as f:
    s = f.read()
    print(s)