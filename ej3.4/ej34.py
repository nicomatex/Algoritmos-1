"""
Alumno: Nicolas Federico Aguerre
Padron: 102145
Practica: Alan
Corrector: Gaston
"""

import math


def calcular_norma_vector(x,y,z):
	"""
	Recibe las componentes cartesianas de un vector en R3 
	y devuelve la norma de dicho vector.
	"""

	sumatoria_componentes_cuadrados = math.pow(x,2) + math.pow(y,2) + math.pow(z,2)
	norma = math.sqrt(sumatoria_componentes_cuadrados)

	return norma;


def calcular_diferencia_vectores(x1,y1,z1,x2,y2,z2):
	"""
	Recibe dos vectores en R3 en el formato (x1,y1,z1,x2,y2,z2)
	y devuelve el vector resultante de la resta entre los vectores
	ingresados.
	"""

	diferencia_x = x1-x2
	diferencia_y = y1-y2
	diferencia_z = z1-z2

	return diferencia_x,diferencia_y,diferencia_z


def calcular_producto_vectorial(x1,y1,z1,x2,y2,z2):
	"""
	Recibe dos vectores en R3 en el formato (x1,y1,z1,x2,y2,z2)
	y devuelve el producto vectorial entre ellos
	en el orden ingresado(v1 x v2).
	"""

	resultado_x = y1*z2 - z1*y2#Calcula la componente X del vector resultado. 
	resultado_y = z1*x2 - x1*z2#Calcula la componente Y del vector resultado.
	resultado_z = x1*y2 - y1*x2 #Calcula la componente Z del vector resultado.

	return resultado_x,resultado_y,resultado_z


def calcular_area_triangulo_de_vertices(xA,yA,zA,xB,yB,zB,xC,yC,zC):
	"""
	Recibe las coordenadas de tres puntos A,B,C en R3 en 
	el formato (xA,yA,zA,xB,yB,zB,xC,yC,zC) y devuelve
	el area del triangulo definido por dichos puntos.
	"""

	ABx,ABy,ABz = calcular_diferencia_vectores(xB,yB,zB,xA,yA,zA) #Calcula el vector AB
	ACx,ACy,ACz = calcular_diferencia_vectores(xC,yC,zC,xA,yA,zA) #Calcula el vector AC

	producto_x,producto_y,producto_z = calcular_producto_vectorial(ABx,ABy,ABz,ACx,ACy,ACz) #Calcula el producto vectorial entre AB y AC 

	norma = calcular_norma_vector(producto_x,producto_y,producto_z)

	area = norma/2

	return area

def calcular_area_cuadrilatero_convexo(xA,yA,xB,yB,xC,yC,xD,yD):
	"""
	Recibe las coordenadas de 4 puntos A,B,C,D en R2 y devuelve el area
	del cuadrilatero convexo definido por ellos
	"""

	"""
	Calcula el area del cuadrilatero mediante la suma de las areas de dos triangulos definidos 
	por los puntos A,B,C y A,C,D 
	"""

	area_triangulo1 = calcular_area_triangulo_de_vertices(xA,yA,0,xB,yB,0,xC,yC,0)
	area_triangulo2 = calcular_area_triangulo_de_vertices(xA,yA,0,xC,yC,0,xD,yD,0)

	area = area_triangulo1+area_triangulo2
	return area
