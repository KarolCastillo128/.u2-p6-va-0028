import matplotlib.pyplot as plt
import numpy as np
# Karol Castillo 0028

cant_productos=[100,150,200,300,500]
precio = [4000, 7000,9000,12000,18000]

plt.plot(cant_productos,)
plt.show()

#personalizar grafica
plt.plot(
    cant_productos,
    precio,color="green",
    marker="o",
    linestyle="dashed",
    linewidth=2,
    markersize=12,
    )
plt.title("ventas de walmart")
plt.xlabel("cant prod")
plt.ylabel("precio")
plt.show()