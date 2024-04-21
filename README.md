# Reto_9
>### 1.De los retos anteriores selecione 3 funciones y escribalas en forma de lambdas.

```python
#Reto 6, punto 1 (Dado la figura de la imagen, desarrolle Una función matemática para calcular el volumen y el área superficial.)
import math
Volumen= lambda r1,r2,h:(4/3 * math.pi * r1**3)+((math.pi* r2**2* h)/3)  #Volumen de un cono y una esfera y despues se suman.
Area = lambda r1,r2,h :(4*math.pi * r1**2)+((math.pi * r2**2)+(math.pi*r2* ((r2**2 + h**2) **0.5))) #Area de un cono y una esfera y despues se suman.

#Reto 6, punto 2 (Dado la figura de la imagen, desarrolle Una función matemática para calcular el área y el perimetro.)
Area= lambda a,b,r:(a*b)+(2*(math.pi*r**2)) #Area de un rectangulo y dos circulo y despues se suman.
Perimetro= lambda a,b,r:(2*(a+b))+(2*(2*math.pi*r))  #Perimetro de un rectangulo y dos circulo y despues se suman.

#Reto 6, punto 3 (Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.)
Carne = lambda N,M,K : 6*N +7*M + K #Calculo el total de carne dado cantidad de N gallinas, M gallos y K pollitos.

```
>### 2.De los retos anteriores selecione 3 funciones y escribalas con argumentos no definidos (*args).

```python
#Reto 8, punto 1
def cuadrados(*args):
  for i in args: # Se recorre la lista de numeros
    cuad=i**2  # Se calcula el cuadrado de cada numero
    print(f"el cuadrado de {i} es {cuad}") # Se imprime el numero y su cuadrado

#Reto 8, punto 4
def factorial (*args):
  for i in args: # Se recorre la lista de numeros
    N=i  # Se guarda el valor inicial en el valor N
    Factorial : int = 1 # El factorial se empieza por 1
    while i >= 1 : # Se repite el ciclo mientras que el numero sea mayor o igual a 1 
      Factorial *= i	# El factorial se multiplica por el numero
      i-=1 # El numero se resta por uno y se repite el ciclo
    print("El factorial de " +str(N)+" es "+str(Factorial))  # Se imprime el numero y su factorial 

#Reto 4, punto 4
def determinante (*args):
  for i in args:  # Se recorre la lista de numeros
    if i >0 : # Si el numero es positivo
      print(f"El numero {i} es positivo") # Se imprime que el numero es positivo
    elif i <0 : # Si el numero es negativo
      print(f"El numero {i} es negativo") # Se imprime que el numero es negativo
    else:  # Si el numero es no es ni negativo ni positivo
      print(f"El numero {i} es el neutro para la suma") # Se imprime que el numero es el neutro para la suma
```
>### 3.Escriba una función recursiva para calcular la operación de la potencia.

```python
def Potencia_rec(a,b): 
  if b == 0: # Si el exponente es 0
    return 1 # Se retorna 1
  else: # Si el exponente no es 0
    return a*Potencia_rec(a,b-1) # Se retorna la base multiplicada por la funcion de la base y el exponente menos 1
```
>### 4.Utilice la siguiente plantilla de code para contar el tiempo: Realice pruebas para calcular fibonacci con iteración o con recursión. Determine desde que número de la serie la diferencia de tiempo se vuelve significativa. Importante: Revisar este hilo.

```python
import time

start_time = time.time() # Se empieza le tiempo
def fibonacci (n)->int :  
  if n == 0: # Si el numero es 0
    return 0 # Se retorna 0
  elif n == 1: # Si el numero es 1
    return 1 # Se retorna 1
  else: # Si el numero no es 0 ni 1
    return fibonacci(n-1) + fibonacci(n-2) #Se retorna la suma de la funcion del numero menos unn y la funcion del numero menos dos
end_time = time.time() # Se termina el tiempo

timer = end_time - start_time # Se calcula el tiempo con la diferencia de la hora final y la hora inicial
print(timer) # Se imprime el tiempo
```
Desde el termino 36 de la serie, el cambio de tiempo es significativo, como se ve en la siguiente imagen:
[![Captura-de-pantalla-2024-04-21-171956.png](https://i.postimg.cc/vTsjJYbt/Captura-de-pantalla-2024-04-21-171956.png)](https://postimg.cc/jwMZNrWD)
>### 5.Crear cuenta en stackoverflow y adjuntar imagen en el repo
[![Captura-de-pantalla-2024-04-21-173839.png](https://i.postimg.cc/Lskjy2Qp/Captura-de-pantalla-2024-04-21-173839.png)](https://postimg.cc/yJdJx4zQ)
>### 6.Cosas de adultos....ir a linkedin y crear perfil.... Dejar enlace en el repo.
[Perfil de linkedin](https://www.linkedin.com/in/sebastian-cespedes-rico-832376304/)
 
