class Ninja:
# implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet("Gregory", "Lion", "Destroy")

    def walk(self):
        self.play = play()
        return self

    def feed(self):
        self.eat = eat()
        return self

    def bathe(self):
        self.bathe = noise(self)
        return self

class Pet:

    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
    
    def sleep(self):
        print(f"{self.name} energy increased by 25!")
        return self
    
    def eat(self):
        print(f"{self.name} energy increased by 5 & health by 10!")
        return self
    
    def play(self):
        print(f"{self.name}'s health has increased by 5!")
        return self
    
    def noise(self):
        print(f"{self.name} GO RAWRRRRRRR")
        return self


justin = Ninja("Justin", "Won","bone", "chicken", "Dinosaur")

justin.pet.play().sleep().eat().noise()