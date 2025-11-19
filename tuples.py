# Tuples are just like list - they can store multiple
#items. But Tuples are imutable (cant be changed)

my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

#Accessing items
print(my_tuple[0])
print(my_tuple[2])

#check if item exits
if "cherry" in my_tuple:
    print("Yes, it is")

#single item tuple
single = ("apple")
print(single)

#nested tuple
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
combine = (tuple1, tuple2)
print(combine)