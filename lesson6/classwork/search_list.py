fruit = ["apple", "banana", "cherry", "date", "elderberry"]

if "banana" in fruit:
    print("Banana is in the list.")
else:
    print("Banana is not in the list.")

print("Our algorithm:")

found = False
index = -1

for i in range(len(fruit)): # iterate through each index
    item = fruit[i]      # get the item at that index
    if item == "banana": # check if it matches "banana"
        found = True     # set found to True if a match is found
        index = i       # store the index where it was found
        break            # exit the loop early since we found it

if found == True:
    print("Banana is in the list at index", index)
else:
    print("Banana is not in the list")
    
