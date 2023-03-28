class Punkt:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def __str__(self):
        return f"POINT ({self.x},{self.y})"
    

p1=Punkt(3,4)
p2=Punkt(10,20)

print(p1)