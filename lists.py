# Lists are uesed to store multiple items in a 
# single variable

my_list = [10, 20, 30, 40, 50]
print(my_list)

mixed_lists = [1, "apple", 3.5, True]
print(mixed_lists)

#Accessing list items by their index number
fruits = ["apple", 'banana', "cherry"]
print(fruits[0])
print(fruits[2])

#you can also use negative indexes to count from the end
print(fruits[-2])

#modify the lists
fruits[1] = "mango"
print(fruits)

#adding to the end of list
fruits.append("orange")
print(fruits)

#adding to particular positon in list
fruits.insert(1, "kiwi")
print(fruits)

#removing items from lists
fruits.remove("apple")
print(fruits)

#checking if item exits in list
if "mango" in fruits:
    print("yes, mango is in list")

#checking list length
print(len(fruits)) #return the number of items in list
