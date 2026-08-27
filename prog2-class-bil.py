class Bil:
    def __init__(self, ägare='', reg='', märke='', tjänstevikt='', hp='', nm=''):
        self.ägare= ägare
        self.reg = reg
        self.märke = märke
        self.tjänstevikt= tjänstevikt
        self.hp = hp
        self.nm = nm

class Persson:
    def __init__(self, förnamn=''):
        self.förnamn = förnamn

k = Bil()
k.ägare = Persson(förnamn='Bertil')


bil1 = Bil(ägare=Persson(förnamn='Bertil'), reg="SWA199", märke="Bmw", tjänstevikt="1395kg", hp="193hp", nm="280nm")




bil2 = Bil(ägare=Persson(förnamn='Gustaf'), reg="xlp856", märke="Bmw", tjänstevikt="1545kg", hp="286hp", nm="580nm")

print(bil1.reg, bil1.märke, bil1.tjänstevikt, bil1.hp, bil1.nm)
print(bil2.reg, bil2.märke, bil2.tjänstevikt, bil2.hp, bil2.nm)

