from pyproj import Transformer

lat = 47.5347037
lng = 7.6424084

t = Transformer.from_crs("EPSG:4326", "EPSG:2056")

r = t.transform(lat,lng)
print(r)