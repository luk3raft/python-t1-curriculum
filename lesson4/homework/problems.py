# Problem 1
# Ask user for two test scores.
# If BOTH scores are at least 50, print "You passed both!"
# Otherwise, print "You failed at least one."
score1 = int(input("how did you score on your first test 0/100? "))
score2 = int(input("how did you score on your second test 0/100? "))

if score1 >= 50 and score2 >= 50:
    print("You passed both!")
else:
    print("You failed at least one.")



# Problem 2
# Ask user if they brought lunch and water (yes/no).
# If they brought lunch OR water, print "You're somewhat ready."
# If they brought both, print "You're fully ready!"
# If they brought neither, print "You're not ready."
brought_lunch = input("Did you bring lunch? (yes/no)")
brought_water = input("Did you bring water? (yes/no)")


if brought_lunch == "yes" and brought_water == "yes":
    print("You're fully ready!")
elif brought_lunch == "yes" or brought_water == "yes":
    print("You're somewhat ready.")
else:
    print("You're not ready.")



# Problem 3
# Ask user to enter a number.
# If the number is NOT between 1 and 10 (inclusive), print "Out of range."
# Otherwise, print "In range."
number = int(input("Enter a number: "))
if number < 1 or number > 10:
    print("Out of range.")
else:
    print("In range.")




# Problem 4
# Generate a random number between 1 and 10.
# Ask the user to guess.
# If the guess is right AND the number is even, print "Even match!"
# Else if guess is right OR number is 5, print "Nice try!"
# Otherwise, print "Nope."
import random
random_number = random.randint(1, 10)
user_guess = int(input("Guess a number between 1 and 10: "))
if user_guess == random_number and random_number % 2 == 0:
    print("Even match!")
elif user_guess == random_number or random_number == 5:
    print("Nice try!")
else:
    print("Nope.")



# Problem 5
# Ask the user for two numbers.
# If one is divisible by 5 AND the other is NOT divisible by 2, print "Interesting pair!"

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if (num1 % 5 == 0 and num2 % 2 != 0) or (num2 % 5 == 0 and num1 % 2 != 0):
    print("Interesting pair!")