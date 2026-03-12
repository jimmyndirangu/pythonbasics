class Car:
    # constructor
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    # method
    def drive(self):
        print(self.brand,f"is my dream Car and {self.color} in color")


# object creation
car1=Car("Lexus","White")
car1.drive()

car2=Car("Mercedes","Black")
car2.drive()

car3=Car("Audi","Grey")
car3.drive()


# creation of a class called fruits which should have attributes type, color, price 
class Fruits:
    def __init__(self,type,color,price):
        self.type=type
        self.color=color
        self.price=price
    def display(self):
        print(self.type,f"is {self.color} and costs {self.price}")

fruit1=Fruits("Banana","Yellow","Ksh.50")
fruit1.display()

fruit2=Fruits("Green Apple","Green","Ksh.35")
fruit2.display()

fruit3=Fruits("Strawberry","Red","Ksh.100")
fruit3.display()