class Dachform:
    def __init__(self, material, farbe):
        self.material = material
        self.farbe = farbe

    def __str__(self):
        return f"{self.material} in {self.farbe}"


class Flachdach(Dachform):
    def __init__(self, material, farbe, begruenung):
        super().__init__(material, farbe)
        self.begruenung = begruenung

    def __str__(self):
        return f"Flachdach aus {super().__str__()} und Begrünung = {self.begruenung}"


class Schraegdach(Dachform):
    def __init__(self, material, farbe, winkel):
        super().__init__(material, farbe)
        self.winkel = winkel

    def __str__(self):
        return f"Schrägdach aus {super().__str__()} und einem Neigungswinkel von {self.winkel} Grad"


class Satteldach(Dachform):
    def __init__(self, material, farbe, winkel):
        super().__init__(material, farbe)
        self.winkel = winkel

    def __str__(self):
        return f"Satteldach {super().__str__()} und einem Satteldach mit einem Neigungswinkel von {self.winkel} Grad"

flachdach = Flachdach("Beton", "Grau", True)
schraegdach = Schraegdach("Ziegel", "Rot", 45)
satteldach = Satteldach("Holz", "Braun", 30)

print(flachdach)
print(schraegdach)
print(satteldach)
