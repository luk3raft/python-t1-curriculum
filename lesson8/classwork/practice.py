# Problem 1
# Write a function that returns your favorite fruit and print it.
def favorite_fruit():
    return "apple"

print(favorite_fruit())



# Problem 2
# Write a function that returns a smiley face and print it.
def smiley_face():
    return ":)"

print(smiley_face())



# Problem 3
# Write a function that takes three parameters: length, width, and height.
# It should return the volume (length * width * height).
def calculate_volume(length, width, height):
    volume = length * width * height
    return volume

print(calculate_volume(3, 4, 5))



# Problem 4
# Create a variable for a book, then print it.
# Modify it inside a function and print it again.
book = "The Great Gatsby"
print(book)

def change_book():
    book = "1984"
    print(book)

change_book()
print(book)



# Problem 5
# Write a function that takes one parameter num.
# The function should return the value of num multiplied by 2.
def double(num):
    return num * 2

print(double(5))