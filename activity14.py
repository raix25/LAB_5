## Activity 14. Covert Tuple to List and List to Tuple using
# Create a tuple with a list as its 3rd element
t = (10, 20, [97, 98, 99])

# Convert the tuple to a list using list()
list_from_tuple = list(t)

# Print the list obtained from the tuple
print("List from tuple:", list_from_tuple)

# Modify the list (now it's a list)
list_from_tuple[2].append(100)  # Add an element to the list

# Convert the modified list back to a tuple using tuple()
tuple_from_list = tuple(list_from_tuple)

# Print the final tuple
print("Tuple from modified list:", tuple_from_list)