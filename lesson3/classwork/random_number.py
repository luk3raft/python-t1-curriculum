import random # importing a module (required to use random.randint(a, b))

x = random.randint(1, 6) # return a number between [1, 6] (inclusive)

print(x)

for i in range(5):  # range(5) means the for loop runs 5 times.
    print("hello!")

# range(n) means i goes from 0 to n-1.
for i in range(5):  # range(5) means the for loop runs 5 times.
    print(i)  # i goes from 0-4, despite the for loop running 5 times.

num = 5
for i in range(num):  # range(5) means the for loop runs 5 times. -> i goes from 0-4.
    print(i*2)  # prints 0, 2, 4, 6, 8