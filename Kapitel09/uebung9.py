import shapely
from shapely.geometry import Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon, GeometryCollection
from shapely import wkt
import matplotlib.pyplot as plt

# Gegebene WKT-Objekte
wkt_objects = [
    "POINT(0 0)",
    "LINESTRING(0 0,1 1,1 2)",
    "POLYGON((0 0,4 0,4 4,0 4,0 0),(1 1, 2 1, 2 2, 1 2,1 1))",
    "MULTIPOINT(0 0,1 2)",
    "MULTILINESTRING((0 0,1 1,1 2),(2 3,3 2,5 4))",
    "MULTIPOLYGON(((0 0,4 0,4 4,0 4,0 0),(1 1,2 1,2 2,1 2,1 1)),((-1 -1,-1 -2,-2,-2,-2 -1,-1 -1)))",
    "GEOMETRYCOLLECTION(POINT(2 3),LINESTRING((2 3,3 4)))"
]

for wkt in wkt_objects:
    obj = shapely.wkt.loads(wkt)
    
    # Berechnen der Fläche
    if obj.geom_type in ["Polygon", "MultiPolygon"]:
        area = obj.area
        print(f"Fläche: {area:.2f}")
    
    # Berechnen der Länge
    if obj.geom_type in ["LineString", "MultiLineString"]:
        length = obj.length
        print(f"Länge: {length:.2f}")
    
    # Darstellung mit Matplotlib
    plt.figure()
    plt.title(obj.geom_type)
    
    if obj.geom_type == "Point":
        plt.plot(obj.x, obj.y, "o")
    elif obj.geom_type == "LineString":
        x, y = obj.xy
        plt.plot(x, y)
    elif obj.geom_type == "Polygon":
        x, y = obj.exterior.xy
        plt.fill(x, y, alpha=0.5)
    elif obj.geom_type == "MultiPoint":
        for point in obj:
            plt.plot(point.x, point.y, "o")
    elif obj.geom_type == "MultiLineString":
        for line in obj:
            x, y = line.xy
            plt.plot(x, y)
    elif obj.geom_type == "MultiPolygon":
        for polygon in obj:
            x, y = polygon.exterior.xy
            plt.fill(x, y, alpha=0.5)
    elif obj.geom_type == "GeometryCollection":
        for geom in obj:
            if geom.geom_type == "Point":
                plt.plot(geom.x, geom.y, "o")
            elif geom.geom_type == "LineString":
                x, y = geom.xy
                plt.plot(x, y)
    
    plt.show()