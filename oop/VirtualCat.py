class Cat:

    def __init__(self, name):
        self.name = name
        self.mood = "content"
        self.hunger = 0
        self.energy = 5

    def meow(self):
        if self.energy <= 0:
            print(f"{self.name} is too tired to meow!")
            self.mood = "grumpy"
        else:
            print(f"{self.name} says: Meow!")
            self.energy -= 1
            if self.energy == 0:
                self.mood = "grumpy"

    def nap(self):
        print(f"{self.name} is taking a nap...")
        self.energy += 2
        if self.hunger > 0:
            self.hunger -= 1
        if self.energy >= 6:
            self.mood = "happy"

    def eat(self):
        if self.hunger > 0:
            self.hunger -= 2
            if self.hunger < 0:
                self.hunger = 0
        self.energy += 1
        self.mood = "content"
        print(f"{self.name} eats some cat food.")

    def play(self):
        if self.energy < 2:
            print("Too tired to play!")
        else:
            self.energy -= 2
            self.hunger += 1
            self.mood = "excited"
            print(f"{self.name} is playing!")

    def status(self):
        print(f"Name: {self.name}")
        print(f"Mood: {self.mood}")
        print(f"Energy: {self.energy}")
        print(f"Hunger: {self.hunger}")

# -------- TEST CODE BELOW --------

cat = Cat("Garfield")

print("\n--- Initial Status ---")
cat.status()

print("\n--- Whiskers Meows ---")
cat.meow()
cat.status()

print("\n--- Whiskers Plays ---")
cat.play()
cat.status()

print("\n--- Whiskers Meows Until Tired ---")
cat.meow()
cat.meow()
cat.meow()
cat.status()

print("\n--- Whiskers Tries to Play While Too Tired ---")
cat.play()
cat.status()

print("\n--- Whiskers Eats ---")
cat.eat()
cat.status()

print("\n--- Whiskers Takes a Nap ---")
cat.nap()
cat.status()

print("\n--- More Napping (should become happy) ---")
cat.nap()
cat.status()

print("\n--- Whiskers Eats Again ---")
cat.eat()
cat.status()

print("\n--- Whiskers Plays Again ---")
cat.play()
cat.status()
