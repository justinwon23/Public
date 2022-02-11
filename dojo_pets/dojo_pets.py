# How to return energy/health to preserve



class Ninja:
# implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self

class Pet:

    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 80
        self.health = 100
    
    def sleep(self):
        self.energy += 25
        return self
    
    def eat(self):
        self.energy += 5
        self.health += 10
        return self.energy, self.health #This is questionable
        
    
    def play(self):
        self.health += 5
        self.energy -= 15
        return self
    
    def noise(self):
        print(f"{self.name} GO RAWRRRRRRR")
        return self

Gregory= Pet("Gregory", "Lion", ["sit, speak, attack "])

justin = Ninja("Justin", "Won","bone", "chicken", Gregory)

justin.bathe().feed().feed().feed()
print(Gregory.health)
print(Gregory.energy)





