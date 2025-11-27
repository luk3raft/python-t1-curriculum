import random

animals = ['cat', 'dog', 'rabbit', 'hamster', 'parrot']

length = len(animals)

random_index = random.randint(0, length - 1)

random_animal = animals[random_index]
print("Randomly selected animal:", random_animal)