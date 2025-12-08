animals = ["cat", "cat", "dog", "fish", "bird", "cat", "lizard"]
print(animals)

num_cats = animals.count("cat")
print(num_cats, "cats")
      
print("Our algorithm:")

counter = 0

for i in range(len(animals)):
    item = animals[i]
    if item == "cat":
        counter = counter + 1
print(counter, "cats")

numbers = [13, 5, 7, 11, 9, 18]
print(numbers)

for i in range(len(numbers)):  
    item = numbers[i]
    if item > 10:
        counter = counter + 1
print(counter, "numbers greater than 10")