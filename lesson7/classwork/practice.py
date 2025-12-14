# Problem 1
# Find and print the total sum of all the numbers in the list.
numbers = [4, 11, 22, -6, 3]
total = 0
for num in numbers:
    total = total + num
print("Sum:", total)



# Problem 2
# Find and print the biggest number in the list.
numbers = [-9, 17, 5, -3, 0]
biggest = numbers[0]
for num in numbers:
    if num > biggest:
        biggest = num
print("Biggest number:", biggest)



# Problem 3
# Find and print the sum of only the negative numbers in the list (negative means less than 0).
numbers = [2, -1, 8, 10, -7, 6]
total = 0
for num in numbers:
    if num < 0:
        total = total + num
print("Sum of negative numbers:", total)



# Problem 4
# Find and print the sum of only the even numbers in the list. 
numbers = [8, 3, 15, 22, 11, 6]
total = 0
for num in numbers:
    if num % 2 == 0:
        total = total + num
print("Sum of even numbers:", total)



# Problem 5
# Find and print the biggest number that is negative in the list.
numbers = [-1, -30, -5, 7, 12, -2]
biggest_negative = None
for num in numbers:
    if num < 0:
        if biggest_negative is None or num > biggest_negative:
            biggest_negative = num
if biggest_negative is not None:
    print("Biggest negative number:", biggest_negative)
else:
    print("No negative numbers found")