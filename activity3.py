##Activity 3. Index in lists
my_list = [10, 20, 30, 40, 50]
element_to_find = 30

if element_to_find in my_list:
    index = my_list.index(element_to_find)
    print(f"The element {element_to_find} is at index {index}.")
else:
    print(f"The element {element_to_find} is not in the list.")

# we also can Print particular index value
print (f"The value at index 0 is {my_list[0]}.") 
##Print the length of the lest using len()
print(f"The length of the list is {len(my_list)}.")
# Change an element value in the list
newElement_value= my_list[0]=999
print("The new list fatre the change is:", my_list)