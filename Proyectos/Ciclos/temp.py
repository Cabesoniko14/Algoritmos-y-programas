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

"""
"""
def factorial(n):
    if n<=1:
        return 1
    else:
        print("f(",n,")=",n,"*","f(",n-1,")")
        return n*factorial(n-1)

print(factorial(5))

def fibo (n):
    if n<=2:
        return n-1
    anterior=0
    siguiente=1
    contador=2
    while (contador<n):
        temporal=anterior
        contador+=1
        anterior=siguiente
        siguiente=temporal+siguiente
    return siguiente
    
def fibo_rec (n):
    if n<=2:
        return n-1
    else:
        print ("fibo_rec(",n-2,"), + fibo_rec(",n-1,")")
        return fibo_rec(n-2) + fibo_rec(n-1)
    
import time

n=30
start=time.perf_counter()
fibo(n)
print("Iterativo:",time.perf_counter()-start)

start=time.perf_counter()
fibo_rec(n)
print("Recursivo:",time.perf_counter()-start)
"""
"""
def ciclo(n):
""
  

º   if n==0:
        print(n)
    else:
        print(n)
        n-=1
        ciclo(n)
        
print (ciclo(20))


def ciclo_incremental(n, contador):
    if contador==n:
        print(n)
    else:
        print(contador)
        contador+=1
        ciclo_incremental(n,contador)
        
        
def imprime_lista_decremental(lista):
    #caso base, imprimir el primer elemento
    #caso recursivo, imprimir los siguientes de manera decreciente
    
    if len(lista)==1:
        print("Elemento:", lista[0])
    else:
        print("Elemento:", lista[len(lista)-1])
        imprime_lista_decremental(lista[0:len(lista)-1])


def i_lista_dec_v2(lista):
    if len(lista)==1:
        return "Elemento: "+str(lista[0])
    else:
        return "E:"+ str(lista[len(lista)-1]) +" " +i_lista_dec_v2(lista[0:len(lista)-1])
    
def imprime_lista_inc(lista):
    if len(lista)==1:
        print("Elemento:", lista[0])
    else:
        print("Elemento:",lista[0] )
        imprime_lista_inc(lista[1:])

"""

def rellenar(texto, longitud, caracter):
    if len(texto) >= longitud:
        return texto
    else:
        return rellenar(caracter+texto, longitud, caracter)


matriz = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]



def impresion(matriz, i=0, j=0):
    if j==len(matriz[0]):
        j=0
        i+=1
    
        if i==len(matriz):
            return ""
        else:
            return "\n" + impresion(matriz, i, j)
    else:
        sub_resultado = rellenar(str(matriz[i][j]),4,"0")
        j+=1
        return sub_resultado + " " + impresion(matriz, i, j)





