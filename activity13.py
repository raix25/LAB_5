## Activity 13. Tuples in Python
# Create a tuple with a list as its 3rd element
t = (10, 20, [97, 98, 99])

# Print the original tuple
print("Original tuple:", t)

# Access and modify the list within the tuple
mutable_list = t[2]
mutable_list.append(100)  # Add an element to the list

# Print the modified tuple
print("Modified tuple:", t)