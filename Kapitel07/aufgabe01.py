import random
import matplotlib.pyplot as plt

# Erzeugen von 1000 Zufallszahlen im Bereich von [-100, -100] bis [100,100]
x = []
y = []
color = []

for i in range(1000):
    x.append(random.uniform(-100,100))
    y.append(random.uniform(-100,100))
    #color.append((random.random(),random.random(),random.random()))
    color.append(random.choice(['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']))


# Plotten der Zufallszahlen mit verschiedenen Farben
plt.scatter(x, y, c=color)

# Anzeigen des Plots
plt.xlabel("X-Achse")
plt.ylabel("Y-Achse")
plt.show()