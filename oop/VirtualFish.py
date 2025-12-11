class Fish:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.hunger = 0
        self.energy = 5
        self.cleanliness = 10
        self.mood = "relaxed"

    def swim(self):
        if self.energy <= 0:
            print(f"{self.name} is too tired to swim!")
            return

        print(f"{self.name} is swimming around!")
        self.energy -= 1
        self.hunger += 1
        self.dirty_tank()

    def eat(self):
        if self.hunger <= 0:
            print(f"{self.name} is not hungry right now.")
        else:
            self.hunger -= 2
            if self.hunger < 0:
                self.hunger = 0

        self.energy += 1
        print(f"{self.name} munches on some fish flakes.")

    def rest(self):
        print(f"{self.name} is resting peacefully.")

        self.energy += 2
        if self.energy > 10:
            self.energy = 10

        if self.hunger > 0:
            self.hunger -= 1

    def dirty_tank(self):
        self.cleanliness -= 2
        if self.cleanliness < 0:
            self.cleanliness = 0

        if self.cleanliness < 3:
            self.mood = "stressed"
        else:
            self.mood = "relaxed"

    def clean_tank(self):
        self.cleanliness = 10
        self.mood = "relaxed"
        print("The tank is sparkling clean!")

    def status(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Energy: {self.energy}")
        print(f"Hunger: {self.hunger}")
        print(f"Tank Cleanliness: {self.cleanliness}")
        print(f"Mood: {self.mood}")

# FISH TEST CODE BELOW

fish = Fish("Nemo", "Clownfish")

print("\n--- Initial Status ---")
fish.status()

print("\n--- Nemo Swims 3 Times ---")
fish.swim()
fish.status()
fish.swim()
fish.status()
fish.swim()
fish.status()

print("\n--- Nemo Eats ---")
fish.eat()
fish.status()

print("\n--- Nemo Rests ---")
fish.rest()
fish.status()

print("\n--- Swim Until Tank Gets Dirty ---")
for _ in range(5):
    fish.swim()
fish.status()

print("\n--- Clean the Tank ---")
fish.clean_tank()
fish.status()

print("\n--- Push Nemo to Low Energy ---")
while fish.energy > 0:
    fish.swim()
fish.status()

print("\n--- Try Swimming With No Energy ---")
fish.swim()
fish.status()

print("\n--- Feed Nemo and Let Him Rest ---")
fish.eat()
fish.rest()
fish.status()
