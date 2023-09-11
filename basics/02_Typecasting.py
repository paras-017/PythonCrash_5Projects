#In Python, typecasting, also known as type conversion or type coercion, refers to the process of changing the data type of an object from one type to another. Python is a dynamically typed language, which means that variables can change their data type during execution. Typecasting allows you to explicitly specify the desired data type for a variable or value.

x = int(3.14)                  #int(): Used to convert a value to an integer data type.
y=float("42.5")                #float(): Used to convert a value to a floating-point (decimal) number.
s = str(123)                   #str(): Used to convert a value to a string.
b = bool(0)                    #bool(): Used to convert a value to a Boolean (True or False).

my_tuple = (1,2,3) 
my_list = list(my_tuple)       #list(): Used to convert an iterable (e.g., tuple, string) to a list.

my_list2 = [4,5,6]
my_tuple2 = tuple(my_list2)    #tuple(): Used to convert an iterable to a tuple.



my_list3 = [1,1,1,2,3,3,4,1,5,3,5,5,6,6,4,6,78,8,89,6,6]
my_set = set(my_list3)         #set(): Used to convert an iterable to a set, removing duplicates.

my_list4 = [("a", 51), ("b", 23), ("c", 93)]
my_dict = dict(my_list4)
print(my_dict['b'])
