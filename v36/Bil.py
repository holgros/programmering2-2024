class Bil:
    def __init__(self, speed, brand):
        self.speed = speed  # tilldela värden på attributet speed
        self.brand = brand  # dito brand
    def honk(self):
        print("TUUT!!")
    def drive(self):
        print("Bilen körs i", self.speed, "kilometer i timmen.")
bil1 = Bil(50, "Volvo")
bil1.honk()             # TUUT!!
bil1.drive()            # Bilen körs i 50 kilometer i timmen
bil2 = bil1             # variabeln bil2 "pekar" på samma objekt som bil1 - vi har alltså inte skapat något nytt objekt
bil2.speed = 70         # ändrar både bil1 och bil2
print(bil1.speed)       # 70