class Rektangel:
    def __init__(Self, x,y,höjd,bredd)
        Self.x = x
        Self.y = y
        Self.höjd = höjd
        Self.bredd = bredd


    def sätt_höjd(Self, höjd):
        Self.höjd = höjd

    def sätt_bredd(Self, bredd):
        Self.bredd = bredd

    def area(Self):
        return Self.höjd * Self.bredd

    def omkrets(Self):
        return 2 * (Self.höjd + Self.bredd)

r = Rektangel(10, 20, 5, 8)
print("Area:", r.area())
print("Omkrets:", r.omkrets())

r.sätt_höjd(10)
r.sätt_bredd(20)
print("Area:", r.area())
print("Omkrets:", r.omkrets())  