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
        return f"{super().__str__()} und {begruenung}"


class Schrägdach(Dachform):
    def __init__(self, material, farbe, winkel):
        super().__init__(material, farbe)
        self.winkel = winkel

    def beschreibung(self):
        return f"{super().__str__()} und einem Neigungswinkel von {self.winkel} Grad"


class Satteldach(Dachform):
    def __init__(self, material, farbe, winkel):
        super().__init__(material, farbe)
        self.winkel = winkel

    def beschreibung(self):
        return f"{super().__self__()} und einem Satteldach mit einem Neigungswinkel von {self.winkel} Grad"
