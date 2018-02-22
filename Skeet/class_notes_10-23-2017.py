# 10/23/2017 In-Class

class Shutter:
    def __init__(self):
        self.louver_count = 0
        self.color = ""
        self.room = ""

    def display(self):
        print("Shutter color:{}, room:{}, louvers:{}".format(self.color, self.room, self.louver_count))

    def get_area(self):
        print("Getting the area...")


class TraditionalShutter(Shutter):
    def __init__(self):
        super().__init__()
        self.width = 0
        self.height = 0

    def display(self):
        print("Traditional shutter color:{}, width:{}, height:{}".format(self.color, self.width, self.height))


class SunburstShutter(Shutter):
    def __init__(self):
        super().__init__()
        self.radius = 0


s1 = TraditionalShutter()
s1.color = "Off-White"
s1.room = "Living Room"
s1.louver_count = 20
s1.width = 60
s1.height = 48

s2 = SunburstShutter()
s2.color = "Snow-White"
s2.room = "Kitchen"
s2.louver_count = 30
s2.radius = 20

s1.display()
s2.display()

