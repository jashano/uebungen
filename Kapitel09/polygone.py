import matplotlib.pyplot as plt
import shapely
import shapely.wkt

wkt1 = "POLYGON (( -5 -5, 5 -5, 5 5, -5 5, -5 -5))"
wkt2 = "POLYGON (( 1 -1,4 -1, 4 1, 1 1, 1 4, -1 4, -1 1, -4 1, -4 -1, -1 -1, -1 -4, 1 -4, 1 -1))"

g1 = shapely.wkt.loads(wkt1)
g2 = shapely.wkt.loads(wkt2)

x,y = g1.exterior.xy

plt.plot(x,y,'r-')
plt.axis("equal")

x,y = g2.exterior.xy
plt.plot(x,y,'b-')

differenz = g1.difference(g2)
print(differenz)

print("EXTERIOR:", differenz.exterior)
print("INTERIOR:", differenz.interiors[0])

print(g1.length)
print(g1.area)

plt.show()