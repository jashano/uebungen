import shapely
from shapely.geometry import Point, Polygon
from shapely import wkt
import matplotlib.pyplot as plt

Muttenz = Point([7.6424084,47.5347037])
print(Muttenz.wkt)

s = "POINT (47.5347037 7.6424084)"
p = wkt.loads(s)
file = open("Kapitel09/schweiz.wkt")
ch = file.read()
file.close()

schweiz = wkt.loads(ch)

for geometry in schweiz.geoms:
    x,y = geometry.exterior.xy
    plt.plot(x,y)
#plt.show()

if Muttenz.within(schweiz):
    print("Ja, Muttenz ist in Schweiz")
else:
    print("liegt nicht in Schweiz")