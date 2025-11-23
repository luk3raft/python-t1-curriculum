age = int(input("how old are you? "))
has_ticket = input("Do you have a movie ticket? (yes/no) ")

if (age >- 13 and has_ticket == "yes"): #AND both conditions must be true for the statement to be true
    print ("You can enter the PG-13 movie.")
    else:
        print("sorry you can't enter")
print("Movie check complete.")

has_pass = input("Do you have a bus pass? (yes/no) ")
has_coins = input("Do you have coins to pay? (yes/no) ")
if has_pass == "yes" or has_ticket == "yes":  # OR: at least one condition must be true for the statement to be true.
    print("You can ride the bus.")
else:
    print("You can't ride the bus.")
print("Bus check complete.")

homework_done = imput("Did you do your homework? (yes/no)")
if not homework_done == "yes":  #NOT flips true to false to true
    print("Go finish your homework!")
else:
    print("Nice job! your all done")
print ("homework check complete")

#
is_raining = imput("Is it raining? (yes/no)")
has_umbrella = imput("Do you have an umbrella? (yes/no)")

if is_raining == input
