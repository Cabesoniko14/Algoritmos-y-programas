#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 17:27:36 2021

@author: javi
"""

class Cilindro:
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura
        
    def __str__(self):
        return "CILINDRO \n"+ "radio: " + str(self.radio) +"\n" + "altura: " + str(self.altura) +"\n" + "area: " + str(self.calcular_area()) + "\n" + "volumen: " + str(self.calcular_volumen()) + "\n"
        
    def __repr__(self):
        return "[radio="+str(self.radio)+", "+ "altura=" + str(self.altura) + "]"
    
    def __lt__(self, otro):
        return self.calcular_volumen() < otro.calcular_volumen()
    
    def __gt__(self, otro):
        return self.calcular_volumen() > otro.calcular_volumen()
    
    def __et__(self, otro):
        return self.calcular_volumen() == otro.calcular_volumen()
        
    def calcular_volumen(self):
        from math import pi
        return pi*(self.radio**2)*self.altura
    
    def calcular_area(self):
        from math import pi
        return 2*pi*self.radio*(self.radio+self.altura)
    
    
    
    
    
        