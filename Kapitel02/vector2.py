class Vector2:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return f"({self.x},{self.y})"

    def __add__(self,other):
        return Vector2(self.x + other.x, self.y + other.y)
    
    def __sub__(self,other):
        return Vector2(self.x - other.x, self.y - other.y)
    
    def __mul__(self,other):
        return Vector2(self.x * other.x, self.y * other.y)
        



v1 = Vector2(1,2)
v2 = Vector2(3,4)
v4 = Vector2(10,10)

v3 = v1 * v2
print(v3)