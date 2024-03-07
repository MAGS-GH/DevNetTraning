# Kapitel omkring Metoder, Funktion og klasser

# Forskellen på en metode og en funktioner er om de har en direkte relation til en klasse
# En funktion kan blive kaldt over alt også uden en klasse eller objekt
# En metode skal hænge sammen med et objekt (klasse)

def myCity(city): 
    print("I live in " + city + ".") 

myCity("Austin") 
myCity("Tokyo") 
myCity("Salzburg") 

class Location:
    def __init__(self, name, country): 
        self.name = name 
        self.country = country 
    def myLocation(self): 
        print("Hi, my name is " + self.name + " and I live in " + self.country + ".")

loc = Location("Mathias", "Danmark") #loc er nu en instans af klassen Location fra før
print(loc.name) 
print(loc.country) 
print(type(loc)) 

loc1 = Location("Tomas", "Portugal")
loc1.myLocation() 

loc2 = Location("Ying", "China") 
loc3 = Location("Amare", "Kenya")
loc2.myLocation() 
loc3.myLocation()


class Circle: 
    def __init__(self, radius): 
        self.radius = radius 
    def circumference(self): 
        pi = 3.14 
        circumferenceValue = pi * self.radius * 2 
        return circumferenceValue 
    def printCircumference(self): 
        myCircumference = self.circumference() 
        print ("Circumference of a circle with a radius of " + str(self.radius) + " is " + str(myCircumference)) 
# First instantiation of the Circle class. 
circle1 = Circle(2) 
# Call the printCircumference for the instantiated circle1 class. 
circle1.printCircumference() 
# Two more instantiations and method calls for the Circle class. 
circle2 = Circle(5) 
circle2.printCircumference() 
circle3 = Circle(7) 
circle3.printCircumference() 