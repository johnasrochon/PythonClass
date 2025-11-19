report_card = {
    "name": "Alice Smith",
    "subject": "Mathematics",
    "grades": [85, 92, 78, 95]
}

print("Student Name: {report_card['name']}")
print("Subject: {report_card['subject']}")

# Calculate the average of the grades
average_grade = sum(report_card["grades"]) / len(report_card["grades"])

# Add the "average" key
report_card["average"] = average_grade

# Print performance based on average
if report_card["average"] >= 90:
    print("Excellent")
elif 70 <= report_card["average"] <= 89:
    print("Good job")
else:
    print("Needs improvement")

# Remove the "subject" key
del report_card["subject"]

# Print the updated report card
print("\nUpdated Report Card:")
print(report_card)