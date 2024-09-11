# variabla argument, s.k. overloading
def myFunk(*input):
    for arg in input:
        print(arg)
myFunk("Hej", "på", "dig")
myFunk("Adjö!")

# ytterligare ett exempel med overloading i konstruktor
class Bil:
    def __init__(self, *args):
        if (len(args) > 0):
            self.maxSpeed = args[0]
            if (len(args) > 1):
                self.license = args[1]
            else:
                self.license = "Okänt registreringsnummer"
bil1 = Bil(120)             # konstruera bil med endast ett argument
bil2 = Bil(150, "ABC12D")   # konstruera bil med två argument
print(bil1.maxSpeed)        # 120
print(bil1.license)         # Okänt registreringsnummer
print(bil2.maxSpeed)        # 150
print(bil2.license)         # ABC12D

# standardvärden i konstruktor
def my_function(country = "Sverige"):
  print("Jag kommer från " + country)
my_function("Norge")    # Jag kommer från Norge
my_function()           # Jag kommer från Sverige
my_function("Danmark")  # Jag kommer från Danmark

# variablers livslängd och synlighet i och utanför metoder
x = 10
def my_function():
    #global x
    x = 5
    print(x)
my_function()			# 5
print(x)				# 10
