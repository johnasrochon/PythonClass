#sets are UNORDERED, UNINDEXED, and have NO DUPLICATE

fruits = ("apple", "banana", "cherry")
print (fruits)

#check if item exist
print("banana" in fruits)

#add item
fruits.add("orange")
print(fruits)

#add multiple items
fruits.update(["kiwi", "mango"])
print(fruits)