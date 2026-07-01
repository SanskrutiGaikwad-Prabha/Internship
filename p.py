class Vehicle :
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    
    def display_vehicle(self):
        print("Brand :",self.brand)
        print("Model :",self.model)
class Bike(Vehicle):
    def __init__(self,brand,model,engine_cc,mileage):
        super().__init__(self.brand,self.model)
        self.engine_cc=engine_cc
        self.mileage=mileage
    
    def display_bike(self):
        print("Engine Capacity :",self.engine_cc,"cc")
        print("Mileage :",self.mileage,"km/l")

#Create object
bike1=Bike(125,55)
bike1.display_bike()