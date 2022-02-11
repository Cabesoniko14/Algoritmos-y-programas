#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 17:45:46 2021

@author: javi
"""

def evaluar(a, b, c, operador):
    operador=operador.lower().strip()
    if operador == "and" :
        print(a, "and", b, "and", c, "=", a and b and c)
    elif operador == "or" :
        print(a, "or", b, "or", c, "=", a or b or c)
    else: 
        print("Operador no reconocido")

operador = input("Ingresa el operador a evaluar: ")

evaluar(True, True, True, operador)
evaluar(True, True, False, operador)
evaluar(True, False, True, operador)
evaluar(True, False, False, operador)
evaluar(False, False, False, operador)
evaluar(False, True, False, operador)
evaluar(False, False, True, operador)
evaluar(False, True, True, operador)

contador = 0
while(contador<10):
    print (contador+1)
    contador+=1 #contador=contador+1 para actualizar valor y no volver loca a la compu
