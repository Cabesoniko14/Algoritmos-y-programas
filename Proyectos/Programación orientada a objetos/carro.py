#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 17:35:50 2021

@author: javi
"""

class Carro:
    def __init__(self, color, num_puertas, capacidad_tanque, max_pasajeros):
        #self.color = color
        self.set_color(color)
        self.num_puertas = num_puertas
        self.set_capacidad_tanque(capacidad_tanque)
        self.max_pasajeros = max_pasajeros
        self.kilometraje = 0

    def viajar(self, kms):
        self.kilometraje += kms
        print ("Recorreras", kms, "kms")
        
    def set_capacidad_tanque(self, capacidad_tanque):
        try:
            self.capacidad_tanque = float(capacidad_tanque)
        except ValueError:
            print("Error: capacidad_tanque inválido")
            self.capacidad_tanque = 40
    
    def set_color(self, color):
        if color.upper() in ["ROJO", "VERDE", "BLANCO"]:
            self.color=color.upper()
        else:
            print("ERROR: Color inválido")
            self.color="BLANCO"

    def __str__(self): #siempre debe regresar str
        return "CARRO: "+self.color+ " " + str(self.num_puertas)+" puertas"

    def __repr__(self): #siempre debe regresar str
        return self.color

    def __eq__(self, otro):
        return self.max_pasajeros == otro.max_pasajeros

    def __lt__(self, otro):
        return self.max_pasajeros < otro.max_pasajeros

    def __gt__(self, otro):
        return self.max_pasajeros > otro.max_pasajeros



carro1 = Carro("blanco", 2, 40, 7)

carro2 = Carro("verde", 2, 40.4, 6)

lista = [carro1, carro2]
lista.sort()
print(lista)


