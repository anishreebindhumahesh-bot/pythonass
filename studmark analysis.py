
# Create a list containing five student marks
marks = [85, 35, 90, 45, 72]

# Convert list into tuple
marks_tuple = tuple(marks)

# Display collections and data types
print("List:", marks)
print("List Data Type:", type(marks))

print("Tuple:", marks_tuple)
print("Tuple Data Type:", type(marks_tuple))

# Find highest and lowest marks
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))

# Count students who scored at least 40
count = sum(1 for mark in marks if mark >= 40)
print("Students scored at least 40:", count)

# Check whether all marks are between 0 and 100
valid = all(0 <= mark <= 100 for mark in marks)
print("All marks are valid:", valid)

# Modify list element
marks[0] = 95
print("Modified List:", marks)

# Modify tuple element
try:
    marks_tuple[0] = 95
except TypeError:
    print("Tuple cannot be modified")

# Observation:
# List is mutable, so its elements can be changed.
# Tuple is immutable, so its elements cannot be changed.
