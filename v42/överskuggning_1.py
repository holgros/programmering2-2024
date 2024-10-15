class Superclass:
    def hej(self):
        print("Hej från Super!")
class Subclass(Superclass):
    def hej(self):
        print("Hej från Sub!")
sup = Superclass()
sup.hej()   # Hej från Super!
sub = Subclass()
sub.hej()   # Hej från Sub!
