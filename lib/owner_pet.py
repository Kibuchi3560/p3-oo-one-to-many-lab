class Pet:
    pass
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]


    def __init__(self ,name, pet_type , owner = "None"):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        if not pet_type in Pet.PET_TYPES:
            raise Exception (f" {pet_type} is not valid as a pet type")

        Pet.all.append(self)
class Owner:
    pass
    
    def __init__ (self , name):
        self.name = name
        
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet , Pet):
            raise Exception("Pet is not valid")

        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)

