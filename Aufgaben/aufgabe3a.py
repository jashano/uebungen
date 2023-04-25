class Stadt:
    def __init__(self, name,einwohnerzahl, land, kontinent, koordinate):
        self.name=name
        self.einwohnerzahl=einwohnerzahl
        self.land=land
        self.kontinent=kontinent
        self.koordinate=koordinate

    def __str__(self):
        return f"{self.name},{self.einwohnerzahl},{self.land},{self.kontinent},{self.koordinate}"