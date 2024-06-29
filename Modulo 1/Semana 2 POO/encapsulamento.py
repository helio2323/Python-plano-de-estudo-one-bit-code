class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    def show(self):
        # accessing public data member
        print(f"Nome: {self.name} Salário: {self.__salary}")
        
fulano = Employee("Fulano", 4000)
sicrano = Employee("Sicrano", 10000)
fulano.name = "Fulano 2"
fulano.__salary = 40000
fulano.show()
sicrano.show()