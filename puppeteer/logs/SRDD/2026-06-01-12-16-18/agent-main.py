class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.level = 1
        self.experience = 0

class Trainer:
    def __init__(self):
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)
        print(f'Added {pet.name} ({pet.species}) to your pets.')

    def display_pets(self):
        print('You have the following pets:')
        for pet in self.pets:
            print(f'- {pet.name} ({pet.species})')

# Create a trainer
trainer = Trainer()
print('Trainer created.')

# Create some pets
dragon = Pet('Scorch', 'Dragon')
unicorn = Pet('Sparkles', 'Unicorn')
phoenix = Pet('Rise', 'Phoenix')
print('Pets created.')

# Add pets to the trainer
trainer.add_pet(dragon)
trainer.add_pet(unicorn)
trainer.add_pet(phoenix)

# Display the pets
trainer.display_pets()