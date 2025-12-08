# Problem 1
# Count and print how many times "Alex" appears in the list.
names = ["Liam", "Alex", "Sophie", "Alex", "Mia"]
count_alex = names.count("Alex")
print("Count of 'Alex':", count_alex)




# Problem 2
# Search for "elephant" in the list and print if it's found.
animals = ["zebra", "giraffe", "lion", "tiger"]
if "elephant" in animals:
    print("'elephant' is found in the list.")
else:
    print("'elephant' is not found in the list.")



# Problem 3
# Count and print how many scores are 100.
scores = [95, 100, 88, 100, 77, 92]
count_100 = scores.count(100)
print("Count of scores with 100:", count_100)



# Problem 4
# Search for the color "blue" in the list and print its index if it's found.
colors = ["red", "green", "blue", "yellow"]
if "blue" in colors:
    blue_index = colors.index("blue")
    print("Index of 'blue':", blue_index)
else:
    print("'blue' is not found in the list.")



# Problem 5
# Count and print how many temperatures in the list are below zero.
temperatures = [3, -2, 5, -7, 0, 4, -1]
count_below_zero = 0
for temp in temperatures:
    if temp < 0:
        count_below_zero += 1
print("Count of temperatures below zero:", count_below_zero)