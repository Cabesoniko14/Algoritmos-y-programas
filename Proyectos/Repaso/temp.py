"""
def nicomano(n):
    
    num_cubos_calculados = 0
    impar = 1
    contador = 0
    num_sumas = 1
    cubo = 0
    
    while  num_cubos_calculados < n:
        
        while contador < num_sumas:
            
            cubo+=impar
            impar += 2            
            contador+=1
        
        print(cubo)
        cubo=0
        num_sumas+=1
        contador = 0
        num_cubos_calculados += 1

print(nicomano(5))

def modifica_var_valor(param_valor):
    param_valor = param_valor*2
    print(param_valor)
    
    
def modifica_var_referencia(param_referencia):
    param_referencia = param_referencia*2
    print(param_referencia)
    
variable = 5
lista= [88]

modifica_var_valor(variable)

modifica_var_referencia(lista)


lista=["a","b"]

for elemento in lista:
    print(elemento) #copia de la lista

for i in range(len(lista)):
    print(lista[i]) #aca cualquier cosa que le haga a la lista se guarda
    
    
def doblar_lista (lista):
    for i in range(len(lista)):
        lista[i]=lista[i]*2
        
lista=[11,12,13,14,15]
print(lista)
doblar_lista(lista)
print(lista)
"""

texto = "ITAM seeks to contribute to the individual's comprehensive education and to develop a freer, more just, and prosperous society. It also aims to become a community in its fullest sense, an institution of excellence and academic freedom, and a high quality autonomous research center."
 
texto=texto.upper()
texto=texto.replace(",","")
texto=texto.replace(".","")
texto=texto.replace("'S","")
texto=texto.replace("'","")

palabras_sin_repeticion=list(set(texto.split())) #para no repetir
palabras_con_repeticion=texto.split()

diccionario = {}

for palabra in palabras_sin_repeticion:
    diccionario[palabra] = palabras_con_repeticion.count(palabra)

def suma_tipica(a,b):
    return a+b

suma_lambda = lambda a, b: a+b

print(suma_tipica(3,4))
print(suma_lambda(3,4))

multiplicadora = lambda a, b, c, d, e : a*b*c*d*e
print(multiplicadora(1,2,3,4,5))    
    
multiplica_listas = lambda lista, multiplicador : lista*multiplicador
print(multiplica_listas([1,2,3],3))

lista = list(diccionario.items())
lista.sort(key = lambda tupla: tupla[1])

print(lista)
    
    
    
    
    
    
    
    
    
    
    
    
    
    