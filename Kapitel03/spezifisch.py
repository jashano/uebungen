from figur import *
from math import *

p1=None
p2=None
p3=None

class Punkt(Figur):
    def __init__(self,x=0,y=0):
        super().__init__("Punkt")
        self.x=x
        self.y=y

    def __str__(self):
        return f"Punkt ({self.x},{self.y})"
    
def dist(p1,p2):
    return ((p2.x-p1.x)**2+(p2.x-p1.x)**2)**0.5

class Dreieck(Figur):
    def __init__(self, p1, p2, p3):
        super().__init__("Dreieck")
        self.p1=p1
        self.p2=p2
        self.p3=p3
    
    def Umfang(self):
        return dist(self.p1,self.p2)+dist(self.p2,self.p3)+dist(self.p1,self.p3)
    
    def flaeche(self):
        return 1/2*abs((self.p2.x-self.p1.x)*(self.p3.y-self.p1.y)-(self.p3.x-self.p1.x)*(self.p2.y-self.p1.y))
    
    def __str__(self):
        return self.name + f" mit {self.p1}, {self.p2} und {self.p3}"
    
class Rechteck(Figur):
    def __init__(self,p1, p2):
        super().__init__("Rechteck")
        self.p1=p1
        self.p2=p2
        
    def Umfang(self):
        return 2*(abs(self.p2.x-self.p1.x))+2*(abs(self.p2.y-self.p1.y))
    
    def flaeche(self):
        return abs(self.p2.x-self.p1.x)*abs(self.p2.y-self.p1.y)
    
    def __str__(self):
        return self.name + f" mit {self.p1} und {self.p2}"
    
class Kreis(Figur):
    def __init__(self,mittelpunkt=Punkt(0,0),radius=0):
        super().__init__("Kreis")
        self.mittelpunkt=mittelpunkt
        self.radius=radius
        
    def Umfang(self):
        return 2 * pi * self.r
    
    def flaeche(self):
        return self.radius**2 * pi
    
    def __str__(self):
        return self.name + f"mit M={self.m}, r={self.r}"
    
class Polygon(Figur):
    def __init__(self,*punkte):
        super().__init__("Polygon")
        self.punkte=list(punkte)
        
    def Umfang(self):
        perimeter = 0
        for i in range(len(self.punkte)):
            perimeter += dist(self.punkte[i], self.punkte[(i+1)%len(self.punkte)])
        return perimeter
    
    def __str__(self):
        punktestr = " ".join(str(p) for p in self.punkte)
        return f"{self.name} {punktestr}"
    
a = Punkt(0,5)
b = Punkt(0,9)
c = Punkt(5,5)
d = Punkt(3,2)
e = Punkt(7,10)
print(a,b,c)

# # Dreieck
# d = Dreieck(a,b,c)
# print(d)
# U = d.Umfang()
# print(U)

# Rechteck
# g = Rechteck(b,c)
# print(g)
# U = g.Umfang()
# print(U)

# Polygon
poly=Polygon(a,b,c,d,e)
U = poly.Umfang()
print(U)
print(poly)