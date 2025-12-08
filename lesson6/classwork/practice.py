# Problem 1
# Count and print how many time "dog" appears in the list.
pets = ["dog", "cat", "dog", "hamster", "dog", "parrot"]
count_dog = pets.count("dog")
print("Count of 'dog':", count_dog)



# Problem 2
# Count and print how many numbers are odd in the list (a number is odd if it's not divisible by 2).
numbers = [8, 3, 12, 7, 4, 11]
count_odd = 0
for num in numbers:
    if num % 2 != 0:
        count_odd += 1
print("Count of odd numbers:", count_odd)



# Problem 3
# Search for "monkey" in the list and print its index if it's found.
zoo = ["lion", "elephant", "monkey", "giraffe", "zebra"]
if "monkey" in zoo:
    monkey_index = zoo.index("monkey")
    print("Index of 'monkey':", monkey_index)
else:
    print("'monkey' is not found in the list.")



# Problem 4
# Search for 99 in the list and print if it's found.
numbers = [10, 45, 32, 99, 60, 5]
if 99 in numbers:
    print("99 is found in the list.")
else:
    print("99 is not found in the list.")



# Problem 5
# Count and print how many numbers are even in the list (a number is odd if it's divisible by 2).
numbers = [13, 22, 8, 19, 6, 7]
count_even = 0
for num in numbers:
    if num % 2 == 0:
        count_even += 1
print("Count of even numbers:", count_even)