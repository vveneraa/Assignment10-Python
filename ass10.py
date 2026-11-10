#1
import math
class Car:
    def __init__(self, color="Black", manufacturer="Toyota", model="Camry", year=2020):
        self.color = color
        self.manufacturer = manufacturer
        self.model = model
        self.year = year

car1 = Car()
car2 = Car(color="Gray", year=2019)
car3 = Car("Red", "Honda", "Civic", 2024)
car4 = Car(manufacturer="BMW", model="M4")

print(car1.color, car1.manufacturer, car1.model, car1.year)
print(car2.color, car2.manufacturer, car2.model, car2.year)
print(car3.color, car3.manufacturer, car3.model, car3.year)
print(car4.color, car4.manufacturer, car4.model, car4.year)

#2

class Solid:
    def surfaceArea(self):
        return None

    def volume(self):
        return None

class Cube(Solid):
    def __init__(self, dblSideLength):
        self.dblSideLength = dblSideLength

    def surfaceArea(self):
        return 6 * self.dblSideLength ** 2

    def volume(self):
        return self.dblSideLength ** 3

class Sphere(Solid):
    def __init__(self, dblRadius):
        self.dblRadius = dblRadius

    def surfaceArea(self):
        return 4 * math.pi * self.dblRadius ** 2

    def volume(self):
        return (4 / 3) * math.pi * self.dblRadius ** 3

cube1 = Cube(5)
sphere1 = Sphere(3)

print("Cube Surface Area:", cube1.surfaceArea())
print("Cube Volume:", cube1.volume())
print("Sphere Surface Area:", sphere1.surfaceArea())
print("Sphere Volume:", sphere1.volume())

#3

class Employee:
    def describe(self):
        print("I am an employee.")

class Manager(Employee):
    def describe(self):
        super().describe()
        print("I manage a team.")

manager1 = Manager()
manager1.describe()

#4

class Account:
    def __init__(self, accountNumber, balance):
        self.accountNumber = accountNumber
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, accountNumber, balance, interestRate):
        super().__init__(accountNumber, balance)
        self.interestRate = interestRate

    def display_account(self):
        print("Account Number:", self.accountNumber)
        print("Balance:", self.balance)
        print("Interest Rate:", self.interestRate)

    def add_interest(self):
        self.balance += self.balance * self.interestRate

savings1 = SavingsAccount(12345, 1000, 0.05)

savings1.display_account()
savings1.add_interest()
savings1.display_account()
savings1.add_interest()
savings1.display_account()