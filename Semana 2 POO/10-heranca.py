# crie um exemplo de heranca

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Animal: {self.name}"

    def make_sound(self):
        print("Animal Fazendo Som")

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def __str__(self):
        return f"Dog: {self.name}"

    def make_sound(self):
        print("Dog Fazendo Som")

