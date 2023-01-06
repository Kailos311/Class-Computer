# from computer import Computer
#
# com1 = Computer('Philips', '4GHz', '16GB', '2TB')
# com1.run()

# ---------- Inheritance ---------- #
# class Animal:
#     alive = True
#     def eat(self):
#         print("This animal is eating")
#     def sleep(self):
#         print("This animal is sleeping")
#
# class Rabbit(Animal):
#     legs = 4
#     def run(self):
#         print("This Rabbit is running")
# class Fish(Animal):
#     legs = 0
#     def swim(self):
#         print("This Fish is swimming")
# class Hawk(Animal):
#     legs = 2
#     def fly(self):
#         print("This Hawk is flying")
#
# rabbit = Rabbit()
# hawk = Hawk()
# fish = Fish()
# rabbit.eat()
# hawk.eat()
# fish.eat()
# print(rabbit.legs)
# print(fish.legs)
# print(hawk.legs)
# rabbit.run()
# hawk.fly()
# fish.swim()

# -------- Multi-level Inheritance --------#
# it's same as inheritance

# -------- Multi-level Inheritance --------#
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

class Car(Vehicle):

    def go(self):
        print("This Car is going")

class Motorcycle(Vehicle):

    def go(self):
        print("This Motocycle is going")
car = Car()
mtcycle = Motorcycle()
car.go()
mtcycle.go()