import time

start_time = time.time() # Se empieza le tiempo
def fibonacci (n)->int :  
  if n == 0: # Si el numero es 0
    return 0 # Se retorna 0
  elif n == 1: # Si el numero es 1
    return 1 # Se retorna 1
  else: # Si el numero no es 0 ni 1
    return fibonacci(n-1) + fibonacci(n-2) #Se retorna la suma de la funcion del numero menos unn y la funcion del numero menos dos
num=38
fibonacci(num)
end_time = time.time() # Se termina el tiempo

timer = end_time - start_time # Se calcula el tiempo con la diferencia de la hora final y la hora inicial
print(f"el tiempo para el numero {num} de la serie es de: {timer}") # Se imprime el tiemp5