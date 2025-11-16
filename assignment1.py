# Define a function that takes a name as an argument
def greet_user(name):
    greeting_message = f"Hello, {name}! Welcome to Python."
    print(greeting_message)

# Assign a value to a variable
user_name = "Alice"

# Call the function, passing the variable as an argument
greet_user(user_name)

# Reassign the variable and call the function again
user_name = "Bob"
greet_user(user_name)

# Define a function to calculate the area of a rectangle
def calculate_rectangle_area(length, width):
    area = length * width
    return area

# Assign values to variables
rectangle_length = 10
rectangle_width = 5

# Call the function and store the returned value in a variable
calculated_area = calculate_rectangle_area(rectangle_length, rectangle_width)

# Print the result using f-strings
print(f"The area of a rectangle with length {rectangle_length} and width {rectangle_width} is: {calculated_area}")

# Another example with different values
new_length = 7.5
new_width = 3.2
another_area = calculate_rectangle_area(new_length, new_width)
print(f"The area of a rectangle with length {new_length} and width {new_width} is: {another_area}")