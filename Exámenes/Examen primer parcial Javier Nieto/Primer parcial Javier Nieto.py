#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 16:17:43 2021

@author: javi
"""

"Primer ejercicio"
def deportista(x,km_corridos):
    return (sum(km_corridos))/x

contador=1
km_corridos=[]
n=int(input("¿Cuántos días corriste? "))
while contador <= n:
    km_dia = int(input(("¿Cuántos diás corriste el día", contador)))
    km_corridos.append(km_dia)
    contador+=1
else:
    print("Tu promedio recorrido es de", deportista(n,km_corridos),"km.")
    if deportista(n,km_corridos)> 5.5:
        print("Felicidades champ, en promedio recorriste más de 5.5kms")

"Segundo ejercicio"

def triangulo(y, final=0):
    while y>final:
        print("T"*y)
        y-=1

"Tercer ejercicio"



def rec(lista, cont=0):
    if len(lista) > 0:
        if max(lista)==lista[0]:
            cont+=1
            print(cont)
            return rec(lista[1:],cont)
    
        else:
            cont+=1
            return rec(lista[1:],cont)
    else:
        print("")