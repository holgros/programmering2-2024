# icke-statiska metoder kräver att man först skapar ett objekt
class Bil:
    def honk(self):		# en Bil-metod
        print("TUUT!!")
    @staticmethod
    def milestokm(miles):
        return 1.6093*miles
    antalBilar = 0      # statiskt attribut
    def __init__(self):
        Bil.antalBilar += 1
'''
honk()      				# fel!!
Bil.honk()  				# också fel!!
'''
print(Bil.milestokm(15))    # 24.14
Bil()
Bil()
Bil()
print(Bil.antalBilar)       # 3