from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car is starting")

c=Car()
c.start()
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

d=Dog()
d.sound()
c=Cat()
c.sound()

class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing rectangle")

c=Circle()
c.draw()
r=Rectangle()
r.draw()

class Employee(ABC):
    @abstractmethod
    def work(self):
        pass

class Developer(Employee):
    def work(self):
        print("Developer writes code")

class Designer(Employee):
    def work(self):
        print("Designer creates UI designs")

Dev=Developer()
Des=Designer()
obj=[Dev,Des]
for i in obj:
    i.work()

class Bird(ABC):
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flies low")

class Eagle(Bird):
    def fly(self):
        print("Eagle flies high")

s=Sparrow()
e=Eagle()
birds=[s,e]
for i in birds:
    i.fly()

