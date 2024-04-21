#Reto 6, punto 1 (Dado la figura de la imagen, desarrolle Una función matemática para calcular el volumen y el área superficial.)
import math
Volumen= lambda r1,r2,h:(4/3 * math.pi * r1**3)+((math.pi* r2**2* h)/3)  #Volumen de un cono y una esfera y despues se suman.
Area = lambda r1,r2,h :(4*math.pi * r1**2)+((math.pi * r2**2)+(math.pi*r2* ((r2**2 + h**2) **0.5))) #Area de un cono y una esfera y despues se suman.

#Reto 6, punto 2 (Dado la figura de la imagen, desarrolle Una función matemática para calcular el área y el perimetro.)
Area= lambda a,b,r:(a*b)+(2*(math.pi*r**2)) #Area de un rectangulo y dos circulo y despues se suman.
Perimetro= lambda a,b,r:(2*(a+b))+(2*(2*math.pi*r))  #Perimetro de un rectangulo y dos circulo y despues se suman.

#Reto 6, punto 3 (Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.)
Carne = lambda N,M,K : 6*N +7*M + K #Calculo el total de carne dado cantidad de N gallinas, M gallos y K pollitos.
