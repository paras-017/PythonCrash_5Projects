#tuple are immutable

t = (3,5,23,43,50,21,5,1,2,2,2,2,3)
t[1] = 234         #gives error becuase assignments are not allowed in tuples
print(t.count(2))