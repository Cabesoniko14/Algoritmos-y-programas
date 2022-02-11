#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 09:30:29 2021

@author: javi
"""
class Accion:
    
    def __init__(self, empresa, id, open, min, max, close):
        self.empresa = empresa
        self.id = id
        self.open = float(open)
        self.min = float(min)
        self.max = float(max)
        self.close = float(close)
    
    def __str__(self):
        return "Accion: " + self.empresa + " " + \
        self.id + " " + \
        str(self.open) + " " + \
        str(self.min) + " " + \
        str(self.max) + " " + \
        str(self.close)
    
    def __repr(self):
        return self.__str__()


class Sesion:
    
    def __init__(self):
        import datetime
        self.fecha = datetime.datetime.now()
        self.acciones = []
        
    def __str__(self):
        acumulado = ""
        for accion in self.acciones:
            acumulado += accion.__str__() + "\n"
        return acumulado
    
    def existe(self, nombre_archivo):
        try:
            archivo = open(nombre_archivo)
            archivo.close()
            return True
        except FileNotFoundError:
            print("Error: el archivo no existe")
            return False
    
    def convertir_lista_a_accion(self, accion_en_lista):
        empresa = accion_en_lista[0]
        id = accion_en_lista[1]
        open = accion_en_lista[2]
        min = accion_en_lista[3]
        max = accion_en_lista[4]
        close = accion_en_lista[5]
        return Accion(empresa, id, open, min, max, close)
    
    def cargar_datos(self, nombre_archivo):
        import datetime
        if self.existe(nombre_archivo):
            with open(nombre_archivo, "r") as archivo:
                f = archivo.readline() #fecha
                f = f[f.index(":")+1:].strip().split(",")
                self.fecha = datetime.datetime(int(f[0]), int(f[2]), int(f[1]))
                archivo.readline() #encabezado
                for linea in archivo.readlines():
                    accion_en_lista = linea.strip().split(",")
                    self.acciones.append(self.convertir_lista_a_accion(accion_en_lista))
        else:
            print("No pude procesar la informacion")
            
    def actualizar(self):
        import random
        
        for accion in self.acciones:
            if random.random() < 0.5:
                accion.open = accion.close * (1+random.random())
            else: 
                accion.open = accion.close * (random.random())
    
    def guardar_datos(self, nombre_archivo):
        with open(nombre_archivo, "w") as archivo:
            archivo.write("Fecha:"+str(self.fecha.year)+"."+str(self.fecha.day)+"."+str(self.fecha.month)+"\n")
            archivo.write("Empresa,ID,open,min,max,close\n")
            texto_accion = ""
            for accion in self.acciones:
               texto_accion = accion.empresa+","+accion.id+","+str(accion.open)+","+str(accion.min)+","+str(accion.max)+","+str(accion.close)+"\n"
               archivo.write(texto_accion)

sesion = Sesion ()
sesion.cargar_datos("acciones.csv")
print(sesion)
sesion.actualizar()
print(sesion)
sesion.guardar_datos("acciones.csv")


