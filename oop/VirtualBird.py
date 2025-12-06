class Bird:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.energy = 5
        self.hunger = 0

    def sing(self):
        if self.energy == 0:
            print("Too tired to sing!")
        else:
            print(f"{self.name} is singing!")
            self.energy -= 1

    def eat(self):
        if self.hunger == 0:
            print(f"{self.name} is not hungry.")
        else:
            print(f"{self.name} eats some seeds.")
            self.energy += 1
            self.hunger -= 1

    def fly(self):
        if self.energy < 2:
            print("Not enough energy to fly!")
        else:
            print(f"{self.name} is flying high!")
            self.energy -= 2
            self.hunger += 1

    def status(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Energy: {self.energy}")
        print(f"Hunger: {self.hunger}")


# TEST CODE BELOW

bird = Bird("Tweety", "Canary")

print("\n--- Initial Status ---")
bird.status()

print("\n--- Tweety Tries to Sing ---")
bird.sing()
bird.status()

print("\n--- Tweety Flies Twice ---")
bird.fly()
bird.fly()
bird.status()

print("\n--- Tweety Tries to Sing Again ---")
bird.sing()
bird.status()

print("\n--- Tweety Eats ---")
bird.eat()
bird.status()

print("\n--- Tweety Flies Again ---")
bird.fly()
bird.status()

print("\n--- Tweety Eats Until Hunger Is 0 ---")
bird.eat()
bird.eat()
bird.status()

print("\n--- Tweety Tries to Eat While Not Hungry ---")
bird.eat()
bird.status()
