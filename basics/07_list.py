l1 = [3,5,23,34,'string',True,101,200]
l2 = ['abba','sbba','aaa','ppp','baa']
l1.remove(200)                      #list is mutable 
# l2.sort()
l1.extend(l2)
print(l1[0:9:2])