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

#remove item
fruits.remove("banana")
print(fruits)

fruits.discard("kiwi")
print(fruits)

#if you are not sure an item exists use discard

#set operations (like math)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.union(set2)) #combine both with no duplicate
print(set1.intersection(set2)) #common elements (returns duplicates)
print(set1.difference(set2)) #non duplicates in set1