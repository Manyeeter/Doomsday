class Car:
    def __init__(self,Name,Type,Speed,Power,Weight,Drag):
        self.Name = Name
        self.Type = Type
        self.Speed = Speed
        self.Power = Power
        self.Weight = Weight
        self.Drag = Drag


def Newcar():
    Data = []
    Name = input("Enter the name of the new car: ")
    VehicleType = input("Enter vehicle type(electric/hybrid/petrol/diesel/ethanol): ")
    TopSpeed = int(input("Enter vehicle top speed: "))
    HorsePower = int(input("Enter vehicle horse power: "))
    WeightKg = int(input("Enter vehicle Weight in kg: "))
    DragCoefficient = float(input("Enter vehicle drag coefficient: "))

    Data.append(Name)
    Data.append(VehicleType)
    Data.append(TopSpeed)
    Data.append(HorsePower)
    Data.append(WeightKg)
    Data.append(DragCoefficient)
    
    return Data
    
x = Newcar()
print(x)