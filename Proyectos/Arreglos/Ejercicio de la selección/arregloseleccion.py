import numpy as np

datos = np.loadtxt("seleccionMexicana.csv", dtype="str", delimiter=",", encoding="UTF-8", usecols = (0,1), skiprows=0)

# Carga los datos y crea un array con los nombres de los jugadores

nombres = np.loadtxt("seleccionMexicana.csv", dtype="str", delimiter=",", encoding="UTF-8", usecols = 0)

# Carga los datos y crea un array con los números de los jugadores

numeros = np.loadtxt("seleccionMexicana.csv", dtype="int", delimiter=",", encoding="UTF-8", usecols = 1)

# Encuentra el nombre del jugador que tenga el número del dorsal mayor.

dorsal_mayor = nombres[numeros == max(numeros)]

# Encuentra todos aquellos jugadores cuyos dorsales sean mayores a 10.

mayores = nombres[numeros>10]

# Une (apila) los arreglos de los jugadores y de los dorsales.

data = np.stack((numeros, nombres), axis=1)

# Guarda los datos en un archivo

np.savetxt("datos.txt", data, fmt="%s,%s")