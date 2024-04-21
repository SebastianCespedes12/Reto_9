def Potencia_rec(a,b): 
  if b == 0: # Si el exponente es 0
    return 1 # Se retorna 1
  else: # Si el exponente no es 0
    return a*Potencia_rec(a,b-1) # Se retorna la base multiplicada por la funcion de la base y el exponente menos 1