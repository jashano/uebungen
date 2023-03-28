class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x},{self.y},{self.z})"
    
    def len(self):
        return (self.x**2 + self.y**2+ self.z**2)**0.5
    
    def __add__(self,other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self,other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self,other):
        if type(other) == Vector3:
            return Vector3(self.x*other.x, self.y*other.y)
        elif type(other) == float or type(other) == int:
            return Vector3(self.x * other, self.y * other, self.z * other)
      
    def __rmul__(self, other):
        return Vector3(self.x * other, self.y * other, self.z * other)

    def dot(self,other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self,other):
        return Vector3(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)
    
    def normalize(self):
         length = self.len()
         return Vector3(self.x / length, self.y / length, self.z / length)


a = Vector3(6,4,2)
b = Vector3(2,1,0)

## Länge
# w=a.len()
# print(w)

# c = a * b # Komponentenweise Multiplikation
# print(c)

# d = a.dot(b) # Skalarprodukt
e = a.cross(b) # Kreuzprodukt
# print(d)
print(e)

## Int und Float mult mit Vektor
# z=3.5*a #float mult mit Vektor
# y=a*3.5 #Vektor mult mit float
# print(z)
# print(y)
# t=3*a
# u=a*3
# print(t)
# print(u)

## Normalisieren
# r=a.normalize()
# print(r)