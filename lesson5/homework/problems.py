

# Problem 1
# Create a list of 3 operating systems.
# Print the last one using len().
# Then reverse the list and print it.
operating_systems = ["Windows", "macOS", "Linux"]
length = len(operating_systems)
print("Last operating system using len():", operating_systems[length - 1])
operating_systems.reverse()
print("Reversed list of operating systems:", operating_systems)



# Problem 2
# Create a list of 4 school subjects.
# Print the second subject.
# Then sort them alphabetically and print the result.
school_subjects = ["Math", "History", "Biology", "Art"]
print("Second subject:", school_subjects[1])
school_subjects.sort()
print("Alphabetically sorted subjects:", school_subjects)



# Problem 3 
# Create a list of 5 error codes.
# Print how many there are.
# Then find the index of "403" and print it.
error_codes = [200, 301, 403, 404, 500]
print("Number of error codes:", len(error_codes))
index_403 = error_codes.index(403)
print("Index of 403 error code:", index_403)



# Problem 4 
# Create a list of 2 programming languages.
# Print a random one.
# Then append another language and print the list.
import random
programming_languages = ["Python", "JavaScript"]
random_language = random.choice(programming_languages)
print("Random programming language:", random_language)
programming_languages.append("c++")
print("Programming languages after append:", programming_languages)



# Problem 5
# Create a list of 6 passwords.
# Print the one in the middle using len().
# Then remove the first password in the list and print it.
passwords = ["pass123", "qwerty", "letmein", "abc123", "password", "123456"]
length = len(passwords)
middle_index = length // 2
print("Middle password using len():", passwords[middle_index])
removed_password = passwords.pop(0)
print("Removed first password:", removed_password)