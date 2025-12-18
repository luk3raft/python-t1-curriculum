def make_greeting():
    greeting = "hello world"
    return greeting

print(make_greeting())

def build_face():
    message = make_greeting()
    return message

#print(build_face())

def personal_greeting(name):
    print("hello", name)
personal_greeting("john")

def rectangle_area(length, width):
    area = length * width
    return area

area = 67
print(area)

print(rectangle_area(3, 4))

def adopt_dog():
    pet = "dog"
    print("the pet is a", pet)
    return pet  


print(adopt_dog())

pet = "cat"

def print_pet():
    pet = "dog"
    print(pet)



print_pet()
print(pet)

pet = "horse"


def print_horse():
    global pet
    pet = "not horse"
    print(pet)
print_horse()
print(pet)