my_tuple = tuple((1, 2, "string"))
print(my_tuple)

my_list = [2, 4, 6]
print(my_list)    # outputs: [2, 4, 6]
print(type(my_list))    # outputs: <class 'list'>
tup = tuple(my_list)
print(tup)    # outputs: (2, 4, 6)
print(type(tup))    # outputs: <class 'tuple'>


                        #You can also create a tuple using a Python built-in function called tuple().
# This is particularly useful when you want to convert a certain iterable (e.g., a list, range, string, etc.) to a tuple: