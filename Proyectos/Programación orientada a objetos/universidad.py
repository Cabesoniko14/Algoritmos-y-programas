#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 11:06:33 2021

@author: javi
"""

class Persona:
    
    def __init__(self, clave_unica, nombre, apellidos):
        self.clave_unica = clave_unica
        self.nombre = nombre
        self.apellidos = apellidos
        
    def __str__(self):
        return "Clave Única: " + str(self.clave_unica) + "\n" + \
        "Nombre: " +  self.nombre + "\n" + \
        "Apellidos: " + self.apellidos
    
    def __repr__(self):
        return self.__str__()
  
    
class Estudiante(Persona):
    
    def __init__(self, clave_unica, nombre, apellidos, carrera):
        super().__init__(clave_unica, nombre, apellidos)
        self.carrera = carrera
    
    def __str__(self):
        return super().__str__() + "\n" "Carrera: " +  self. carrera


class Profesor(Persona):
    
    def __init__(self, clave_unica, nombre, apellidos, departamento):
        super().__init__(clave_unica, nombre, apellidos)
        self.departamento = departamento
    
    def __str__(self):
        return super().__str__() + "\n" "Departamento: " + self.departamento

javi = Persona ("188507", "Javier", "Nieto")
print(javi)

javier = Estudiante ("188507", "Javier", "Nieto", "Economia")
print(javi)