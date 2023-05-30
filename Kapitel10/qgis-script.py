from qgis.core import *
import qgis.utils

canvas = iface.mapCanvas()
layers = canvas.layers()

#for layer in layers:
 #   print(layer.name())

# airports = layers[0]
features = airports.getFeatures()
alles = list(features)
#print(alles[0])

file = open("airports.csv", "w", encoding="utf-8")

for data in alles:
    name = data.attributes()[4]
    wikipedia = data.attributes()[9]
    punkt = data.geometry().asPoint()
    file.write(f"{name},{wikipedia},{punkt.x()},{punkt.y()}\n")
    
file.close()
print("DONE")
    
#print(a.geometry().asWkt())
#punkt = a.geometry().asPoint()
#print(punkt.x(),punkt.y())