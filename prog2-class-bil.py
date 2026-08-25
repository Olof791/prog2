class Bil:
    def __init__(self):
        self.reg = ""
        self.märke = ""
        self.tjänstevikt= ""
        self.hp = ""
        self.nm =""

bil1 = Bil()
bil1.reg= "SWA199"
bil1.märke= "Bmw"
bil1.tjänstevikt="1395kg"
bil1.hp="193hp"
bil1.nm="280nm"



bil2 = Bil()
bil2.reg="xlp856"
bil2.märke="Bmw"
bil2.tjänstevikt="1545kg"
bil2.hp="286hp"
bil2.nm="580nm"

print(bil1.reg, bil1.märke, bil1.tjänstevikt, bil1.hp, bil1.nm)
print(bil2.reg, bil2.märke, bil2.tjänstevikt, bil2.hp, bil2.nm)