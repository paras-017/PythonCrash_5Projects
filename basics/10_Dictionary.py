dict1 = {}                  #its dictionary not empty set to create empty set you can create set by ==>b = set()
print(type(dict1))


dict2 = {
    "st_name":"paras",
    "st_rollNo":33,
    "st_class":"VII-C",
}
print(dict2["st_rollNo"])                #gives error if key is not found
print(dict2.get("st_rollNo"))            #saves you from getting error if key not found

print(dict2.keys())

print(dict2.values())