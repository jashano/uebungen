class vector3():
    def __init__(self,x=0,y=0,z=0):
        self.setCoordinates(x,y,z)

    def setCoordinates(self,a,b,c):
        self._coordinates=[0,0,0]
        self._coordinates[0]=a
        self._coordinates[1]=b
        self._coordinates[2]=c

    def getCoordinates(self):
        return self._coordinates

    def len(self):
        return ((self._coordinates[0]**2+
                 self._coordinates[1]**2+
                 self._coordinates[2]**2)**0.5)

    coordinates = property(getCoordinates, setCoordinates)

a=vector3(2,3,4)
b=vector3()
c=vector3()
a.setCoordinates(5,6,7)
print(a.coordinates, "Länge des Vektors:",a.len())
print(b.coordinates)

#c.coordinates([1,2,4])
#setCoordiantes funktioniert nicht mit Listen . TypeError: 'list' object is not callable