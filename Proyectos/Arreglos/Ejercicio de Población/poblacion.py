#1. Carga los datos

import numpy as np

with open("poblacion.csv") as lectura, \
     open("poblacionMundial.csv", "w") as escritura:
         lineas = lectura.readlines()
         for linea in lineas:
             linea = linea.replace(", ", " ")
             linea = linea.replace("\"", "")
             escritura.write(linea)
             
             
country, code, year, total, urban_percentage = np.loadtxt("poblacionMundial.csv", delimiter=",", dtype="str", encoding="UTF-8", skiprows=1, unpack = True)

year = year.astype(int)
total = total.astype(np.int64)
urban_percentage = urban_percentage.astype(float) 

max_urban = country[urban_percentage == max(urban_percentage)]

#2. Obtenga arrays para 1960 y para 1961 de cada columna

indices60 = np.where(year == 1960)
indices61 = np.where(year == 1961)

country60 = country[indices60]
code60 = code[indices60]
total60 = total[indices60]
urban_percentage60 = urban_percentage[indices60]

country61 = country[indices61]
code61 = code[indices61]
total61 = total[indices61]
urban_percentage61 = urban_percentage[indices61]

#3. Incrementó el promedio de la población urbana?
if urban_percentage60.mean() < urban_percentage61.mean():
    print("sí incrementó el promedio de la población")
else:
    print("No incrementó el promedio de la población")
    
#4. Incrementó la poblacion?

if total60.sum() < total60.sum():
    print("Sí incrementó la población")
else:
    print("No incrementó la población")

#4. Calcula el porcentajde de crecimiento por cada país

crecimiento = ((total61*100)/total60) - 100

#5. Imprímelo con su país

paises_y_crecimiento = np.stack((country60, crecimiento), axis = 1 )

#6. Listado de países con crecimiento

paises_con_crecimiento = country60[crecimiento > 0]
paises_con_decrecimiento = country60[crecimiento < 0]

#7. País con el máximo crecimiento

pais_max_crecimiento = country60[crecimiento == max(crecimiento)]

#8. País con el mayor decrecimiento

pais_max_decrecimiento = country60[crecimiento == min(crecimiento)]

#9. Países con crecimiento entre 0 y 1%

paises_crecimiento_entre_0y1 = country60[(crecimiento>0)*(crecimiento<1)]