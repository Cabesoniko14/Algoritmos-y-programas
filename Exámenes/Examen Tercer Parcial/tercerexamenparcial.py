#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 17:31:50 2021

@author: javi
"""
import pandas as pd

# ******* 3er Examen Parcial de Algoritmica y Programacion *****
#
# Clave unica:
# Nombre:
#
# El examen es individual.
#
#
#
# Actividad unica. Crea un ejercicio ORIGINAL de analisis de datos
# y resuelvelo utilizando pandas. El ejercicio deberá ajustarse
# a los siguientes lineamientos.
#
#
# a. (2 puntos) Redacta un parrafo que provea de contexto al ejercicio.
# Por ejemplo, el ejercicio puede estar asociado al analisis de la
# bolsa de valores, al analisis de ventas de una cadena de supermercados,
# al analisis de resultados deportivos, etc. NOTA: no se pueden utilizar los
# los contextos de los ejercicios vistos en clase.
#
# Introduce tu respuesta en el siguiente espacio utilizando comentarios "#":
#
#
#El trabajo va a estar basado en el videojuego FIFA Ultimate Team. En este videojuego, salen al mercado diferentes 
#jugadores para que las personas los puedan comprar. Celebrando el final de temporada de  la liga española de futbol, 
#salieron al mercado 19 jugadores con versiones mejoradas para conmemorar el "Equipo de la Temporada" (TOTS).
#En este trabajo, voy a incluir en un DataFrame elnombre de cada jugador, su posición, su valor más bajo en el mercado,
# y la suma total de sus estadísticas.


# b. (1 punto) Crea manualmente (o de forma automatizada, si asi lo deseas)
# un archivo CSV que contenga entre 10 y 20 renglones, y entre 4 y 6 columnas
# de informacion. Los datos y sus tipos (str, int y/o float) pueden ser
# aleatorios, pero asociados al contexto definido en el inciso anterior.
# Carga el archivo creado en un dataframe para su posterior analisis.
#
# Introduce tu respuesta en el siguiente espacio:

tots_laliga = pd.read_csv("totslaliga.csv", index_col=(0), header = None)


# c. (1 punto) En funcion del contexto, personaliza el nombre de las columnas
# y el indice (o identificadores de los renglones).
#
# Introduce tu respuesta en el siguiente espacio:

tots_laliga.index.name = "numero_jugador"
tots_laliga.columns = ["nombre", "posicion", "precio", "suma_stats"]


# d. (1 punto) Borra alguna de las columnas del DataFrame

tots_laliga.pop("posicion")


# e. (1 punto) Crea una nueva columna en el DataFrame en función
# de las columnas existentes.
#indica el valor en monedas por unidad de stat por jugador 

tots_laliga["valor_por_stat"] = tots_laliga["precio"]/tots_laliga["suma_stats"]


# f. (1 punto) Utilizando iloc, realiza una seleccion de renglones y columnas
# que cumplan con una condicion booleana. En el contexto de tu ejercicio,
# define el enunciado de una consulta y el codigo correspondiente.
#
# Introduce tu respuesta en el siguiente espacio:

#priemro voy a ordenar los datos por sort_by para que excluya los dos jugadores mas caros

tots_laliga.sort_values(by="precio", ascending = True, inplace = True)

#ahora con el iloc voy a impirmir todos los 5 jugadores  mas caros
# y voy a imprimir su nombre, posicion y precio. Ademas, quiero que superen unas dadas stats


print(tots_laliga.iloc[tots_laliga.shape[0]-5: , [0,1,2]][tots_laliga["suma_stats"]>2500])



# g. (1 punto) Repite el inciso anterior, pero ahora utiliza loc.
#
# Introduce tu respuesta en el siguiente espacio:



print(tots_laliga.loc[[4,6,8,1,15],["nombre", "precio", "suma_stats"]][tots_laliga["suma_stats"]>2500])

#titanic.loc[[321, 574], ["edad", "genero"]][(titanic["edad"] > 0) & (titanic["edad"] < 11) ]



# h. (1 punto) Utilizando groupby, realiza dos agrupamientos diferentes de
# la informacion incluida en el dataframe.
#
# Introduce tu respuesta en el siguiente espacio:



tots_laliga.groupby("nombre")[["precio", "suma_stats"]].agg(["mean", "min", "max", "std", "count"])




# i. (1 punto) Grafica los datos.
#
# Introduce tu respuesta en el siguiente espacio:

tots_laliga.plot()












# Nota: Es muy importante que todos los incisos y datos sean coherentes con
# el contexto definido.





# Las respuestas a este examen se deben enviar a itam.examen@gmail.com y a
# octavio.gutierrez@itam.mx. Recomiendo que tambien envien las respuestas con
# copia a alguno de sus correos para que sirva como acuse de recibo. Pueden
# enviar el archivo “.py” y/o pegar el codigo dentro del cuerpo del correo.
#
# No olviden incluir tambien el archivo CSV que crearon.
#
# Favor de poner su nombre y clave unica en el correo.
#
# La hora limite para entregar el examen es 7 pm. En caso de entregar
# el examen posterior a esa hora, habria un descuento de 10% por cada tres
# minutos de retraso.
#
# A mas tardar la siguiente semana, te enviare un mensaje en el chat de
# Teams con la calificacion de tu tercer examen parcial.
# Si deseas revision, por favor contactame via correo para
# concertar cita antes del examen final.
#
# Mucha suerte en el examen!!
