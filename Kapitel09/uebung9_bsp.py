import matplotlib.pyplot as plt
import shapely
import shapely.wkt

g0 = shapely.wkt.loads("POINT(2 2)")
g1 = shapely.wkt.loads("LINESTRING(0 0,1 1,1 2)")
g2 = shapely.wkt.loads("POLYGON((0 0,4 0,4 4,0 4,0 0),(1 1, 2 1, 2 2, 1 2,1 1))")
g3 = shapely.wkt.loads("MULTIPOINT(0 0,1 2)")
g4 = shapely.wkt.loads("MULTILINESTRING((0 0,1 1,1 2),(2 3,3 2,5 4))")
g5 = shapely.wkt.loads("MULTIPOLYGON(((0 0,4 0,4 4,0 4,0 0),(1 1,2 1,2 2,1 2,1 1)),((-1 -1,-1 -2,-2 -2,-2 -1,-1 -1)))")
g6 = shapely.wkt.loads("GEOMETRYCOLLECTION(POINT(2 3),LINESTRING(2 3,3 4))")

x,y = g0.xy
plt.plot(x,y,'ro')

x,y = g1.xy
plt.plot(x,y,'gx-')

x,y = g2.exterior.xy
plt.plot(x,y,'ko-')

x,y = g2.interiors[0].xy
plt.plot(x,y,'b-')


plt.axis("equal")
plt.show()