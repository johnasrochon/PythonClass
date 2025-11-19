#Dictionaires store data in KEY:VALUE pairs
#meaning word and definiton

students = {
    "name": "Leo",
    "age": 22,
    "major": "computer science"
}

print(students)

#accessing items
print(students["name"]) #access by key
print(students.get("major")) #access another way (.get)

#add new item
students["graduation_year"] = 2028
print(students)

#changing values
students["age"] = 28
print(students)

#remove item
students.pop("major")
print(students)

#check if KEY exists
if "name" in students:
    print("Key 'name' is in the dictionary")

#Nested dictionary
students = {
    "student1": {"name": "leo", "age": 20},
    "student2": {"name": "Alex", "age": 30},
}
print(students["student1"]["name"])