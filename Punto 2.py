#Reto 8, punto 1 (Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.)
def cuadrados(*args):
  for i in args: # Se recorre la lista de numeros
    cuad=i**2  # Se calcula el cuadrado de cada numero
    print(f"el cuadrado de {i} es {cuad}") # Se imprime el numero y su cuadrado

#Reto 7, punto 5 (Imprimir el factorial de un número natural n dado)
def factorial (*args):
  for i in args: # Se recorre la lista de numeros
    N=i  # Se guarda el valor inicial en el valor N
    Factorial : int = 1 # El factorial se empieza por 1
    while i >= 1 : # Se repite el ciclo mientras que el numero sea mayor o igual a 1 
      Factorial *= i	# El factorial se multiplica por el numero
      i-=1 # El numero se resta por uno y se repite el ciclo
    print("El factorial de " +str(N)+" es "+str(Factorial))  # Se imprime el numero y su factorial 

#Reto 4, punto 4 (4.Dado un número real x, construya un programa que permita determinar si el número es positivo, negativo o cero. Para cada caso de debe imprimir el texto que se especifica a continuación:)
def determinante (*args):
  for i in args:  # Se recorre la lista de numeros
    if i >0 : # Si el numero es positivo
      print(f"El numero {i} es positivo") # Se imprime que el numero es positivo
    elif i <0 : # Si el numero es negativo
      print(f"El numero {i} es negativo") # Se imprime que el numero es negativo
    else:  # Si el numero es no es ni negativo ni positivo
      print(f"El numero {i} es el neutro para la suma") # Se imprime que el numero es el neutro para la suma