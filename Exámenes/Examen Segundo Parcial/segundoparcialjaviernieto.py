#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 16:35:23 2021

@author: javi
"""

class Vehiculo: 
    
    def __init__(self, fabricante, tipo, precio):
        self.set_fabricante(fabricante)
        self.set_tipo(tipo)
        self.set_precio(precio)
    
    def __str__(self):
        return str(self.fabricante)+","+str(self.tipo)+","+str(self.precio)
    
    def __repr__(self):
        return self.__str__()
    
    def set_fabricante(self, fabricante):
        if fabricante.strip() == "?":
            self.fabricante = ""
        else:
            self.fabricante = fabricante.strip().upper()
    
    def set_tipo(self, tipo):
        if tipo.strip() == "?":
            self.tipo = ""
        else:
            self.tipo = tipo.strip().upper()
    
    def set_precio(self, precio):
        try:
            if precio == "?":
                self.precio = 0.0
            else:
                 self.precio = float(precio.strip())
        except ValueError:
            self.precio = 0.0

class Agencia:
    
    def __init__(self):
        self.vehiculos = []
    
    def __str__(self):
        acumulado = ""
        for vehiculo in self.vehiculos:
            acumulado += vehiculo.__str__() + "\n"
        return acumulado

    

    def cargardatos(self, nombre_archivo):

        with open(nombre_archivo, "r") as archivo:
            for renglon in archivo.readlines()[3: ]:
                if renglon[0] != ",":
                    renglon = renglon.split(",")
                    self.vehiculos.append(Vehiculo(renglon[0], renglon[4], renglon[9]))
                                                                      

    
    def guardar_datos(self, nombre_archivo):
        with open(nombre_archivo, "w") as archivo:
            texto_final = ""
            for vehi in self.vehiculos:
                texto_final = vehi.fabricante+","+vehi.tipo+","+str(vehi.precio)+"\n"
                archivo.write(texto_final)
                
agenciadejavi = Agencia()
agenciadejavi.cargardatos("vehiculos.csv")
print(agenciadejavi)

