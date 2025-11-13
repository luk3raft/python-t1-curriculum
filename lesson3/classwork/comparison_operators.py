print(5 > 3)  # greater than
print(5 < 3) # less than

# the < or > symbol comes fist, befor the equals sign
print(5 >= 5) # greater than or equal to
print(4 <= 5) # less than or equal to

# two equals signs for comparison, one equals for assignment to variable
print(5 == 5) # equal to
print(5 != 3) # not equal to

a = 10
b = 7
print(a > b)
print(a == b)

x = int(input("Give me a number: "))
y = int(input("Give me another number: "))
print(x < y)

c = "apple"
d = "banana"
print("apple" == "apple")
print("Apple" == "apple")  # Case matters when comparing strings
print(c != d)
print("cat" > "dog")  # Alphabetical comparison when greather than and less than
print("dog" < "zebra")