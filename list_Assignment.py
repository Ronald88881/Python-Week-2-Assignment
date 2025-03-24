# Step 1: Creating an empty list called my_list
my_list = []

# Step 2: Appending elements 10, 20, 30, 40 to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Step 3: Inserting 15 at second position
my_list.insert(1, 15)

# Step 4: Extending my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])

# Step 5: Removing the last element from my_list
my_list.pop()

# Step 6: Sorting my_list in ascending order
my_list.sort()

# Step 7: Finding and printing the index of the value 30 in my_list.
index = my_list.index(30)
print(index)

# Output: 3