# Superklass till alla nedanstående klasser
class Media:
    def __init__(self, titel):
        self.titel = titel

# Subklass till Media
class Bok(Media):
    def __init__(self, titel, antal_sidor):
        super().__init__(titel)
        self.antal_sidor = antal_sidor

# Subklass till Media, superklass till Film
class Ljudspår(Media):
    def __init__(self, titel, speltid):
        super().__init__(titel)
        self.speltid = speltid

# Subklass till Film (och Media)
class Film(Ljudspår):
    def __init__(self, titel, speltid, upplösning):
        super().__init__(titel, speltid)
        self.upplösning = upplösning

# Testar klasserna
b = Bok("Bröderna Karamazov", 840)  # skapa en bok med titel och antal_sidor
print(b.titel)      # Bröderna Karamazov
print(b.antal_sidor) # 840
if isinstance(b, Media) and isinstance(b, Bok): # True
    print("b är samtidigt av typen Media och Bok")
f = Film("De sju samurajerna", "3:27:02", "1080")
print(f.titel)      # De sju samurajerna
print(f.speltid)    # 3:27:02
print(f.upplösning) # 1080
if isinstance(f, Media) and isinstance(f, Ljudspår) and isinstance(f, Film):    # True
    print("f är samtidigt av typen Media, Ljudspår och Film")
