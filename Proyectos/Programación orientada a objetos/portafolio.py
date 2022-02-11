#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 17:50:41 2021

@author: javi
"""

class Fija:
    
    def __init__(self, num_titulos, costo, tasa):
        self.num_titulos = num_titulos
        self.costo = costo
        self.tasa = tasa #0.1 < -10%
        
    def __repr__(self):
        return "[F, "+str(self.calcular_rendimiento())+"]"
    
    def __str__(self):
        return "Num titulos: "+str(self.num_titulos)+"\n"+ \
    "Costo promedio: "+ str(self.costo)+"\n"+ \
    "Tasa: "+ str(self.tasa)
    
    def __lt__(self, otro):
        return self.costo*self.num_titulos < otro.costo*otro.num_titulos
    
    def __gt__(self, otro):
        return self.costo*self.num_titulos > otro.costo*otro.num_titulos
    
    def __eq__(self, otro):
        return self.costo*self.num_titulos == otro.costo*otro.num_titulos
    
    def calcular_rendimiento(self):
        #definicion de un metodo, regresa un float
        return self.num_titulos*self.costo*(1+self.tasa)
    


class Variable:
    
    def __init__(self, num_titulos, costo):
        self.num_titulos = num_titulos
        self.costo = costo
    
    def __repr__(self):
        return "[V, "+str(self.calcular_rendimiento())+"]"
    
    def __str__(self):
        return "Num titulos: "+str(self.num_titulos)+"\n"+ \
    "Costo promedio: "+ str(self.costo)+"\n"
    
    def __lt__(self, otro):
        return self.costo*self.num_titulos < otro.costo*otro.num_titulos
    
    def __gt__(self, otro):
        return self.costo*self.num_titulos > otro.costo*otro.num_titulos
    
    def __eq__(self, otro):
        return self.costo*self.num_titulos == otro.costo*otro.num_titulos
    
    def calcular_rendimiento(self):
        from random import random
        if random()>0.5:
            #accion sube de precio
            self.costo = self.costo * (1 + random() * 0.2)
        else:
            #accion baja de precio
            self.costo = self.costo * (1 - random() * 0.2)
            
        return self.num_titulos*self.costo
    
class Portafolio:
    
    contador = 1
    
    def __init__(self, cliente, productos):
        self.id = Portafolio.contador
        Portafolio.contador += 1
        self.cliente = cliente
        self.productos = productos
    
    
    def __str__(self):
        texto = ""
        for producto in self.productos:
           texto+= producto.__str__()+"\n\n"
        return texto
    
    
    def __repr__(self):
        return self.__str__()
    
    
    def promocion_retencion(self, tasa_promocional):
       for producto in self.productos:
           if isinstance(producto, Fija):
               producto.tasa = producto.tasa + tasa_promocional
           
    def calcular_valor(self):
        suma = 0
        for producto in self.productos:
            suma += producto.calcular_rendimiento()
        return suma
    
    
    def titulos_por_tipo(self):
        titulos_fija=0
        titulos_variable=0
        for producto in self.productos:
            if isinstance(producto, Fija):
                titulos_fija += producto.num_titulos
            else:
                titulos_variable += producto.num_titulos
            return titulos_fija, titulos_variable
        
        
    def captura_productos(self):
        continua = True
        while continua == True:
            tipo = int(input("Indica 0 para Fija y 1 para Variable: "))
            num_titulos = int(input("Indica el número de títulos: "))
            costo = float(input("Indica el costo: "))
            if tipo == 0:
                tasa = float(input("Indica la tasa: "))
                self.productos.append(Fija(num_titulos, costo, tasa))
            else: 
                self.productos.append(Variable(num_titulos, costo))
            if input("Continuar (S/N)?: ") == "N":
                continua = False
 
    
 
lista_productos = [Fija(3,100,0.10), Variable(1,100)]


porta1 = Portafolio("Octavio", [Fija(10,100,0.1), Fija(5,100,0.1), Variable(7,100)])

class Broker:
    
    def __init(self):
        self.portafolios = []
