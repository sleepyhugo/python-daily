class Pet:

    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def describe(self):
        print(f"{self.name} is a {self.age} year old {self.species}")


class Adopter:

    def __init__(self, name):
        self.name = name
        self.pets = []

    def adopt(self, pet):
        if pet not in self.pets:
            self.pets.append(pet)

    def show_pets(self):
        if not self.pets:
            print(f"{self.name} has no adopted pets.")
        else:
            print(f"{self.name}'s adopted pets:")
            for pet in self.pets:
                pet.describe()


class AdoptionCenter:

    def __init__(self):
        self.available_pets_list = []

    def add_pet(self, pet):
        if pet not in self.available_pets_list:
            self.available_pets_list.append(pet)
        else:
            print("Pet already in center.")

    def adopt_pet(self, pet, adopter):
        for p in self.available_pets_list:
            if p == pet:
                self.available_pets_list.remove(p)
                adopter.adopt(p)
                print(f"{adopter.name} adopted {p.name}.")
                return

        print("Pet unavailable for adoption.")

    def available_pets(self):
        if not self.available_pets_list:
            print("No pets available.")
        else:
            print("Pets available for adoption:")
            for pet in self.available_pets_list:
                pet.describe()

# TEST CODE BELOW

center = AdoptionCenter()

pet1 = Pet("Buddy", "dog", 3)
pet2 = Pet("Mittens", "cat", 2)
pet3 = Pet("Thumper", "rabbit", 1)

center.add_pet(pet1)
center.add_pet(pet2)
center.add_pet(pet3)


print("\n--- Available Pets Initially ---")
center.available_pets()

adopter = Adopter("Hugo")

print("\n--- Adoption Attempt 1 ---")
center.adopt_pet(pet1, adopter)

print("\n--- Adoption Attempt 2 ---")
center.adopt_pet(pet3, adopter)

print("\n--- Available Pets After Adoptions ---")
center.available_pets()

print("\n--- Hugo's Adopted Pets ---")
adopter.show_pets()
