# 1. Create a tuple called "travel_bag" with at least 5 items
travel_bag = ("shirts", "pants", "toothbrush", "passport", "shoes")

# 2. Print the second and fourth items
print(travel_bag[1])  # second item
print(travel_bag[3])  # fourth item

# 3. Check if "shoes" is in the travel bag
if "shoes" in travel_bag:
    print("You are ready to walk")
else:
    print("you forgot your shoes!!")

# 4. Make a new tuple called "essentials" with 3 must-have items
essentials = ("wallet", "phone", "charger")

# 5. Combine both tuples into one called "final_bag"
final_bag = travel_bag + essentials

# 6. Print how many total items you now have
print(len(final_bag))

# 7. Print the last item in your "final_bag"
print(final_bag[-1])
