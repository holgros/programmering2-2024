class Fordon:
    def kör(self):
        print("Nu kör vi!")
class Bil(Fordon):
    def tuta(self):
        print("Tuuut!!")
b = Bil()
b.kör()     # anropar en Fordon-metod i ett Bil-objekt
b.tuta()    # anropar en Bil-metod
