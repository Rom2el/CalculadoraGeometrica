#Calculadora que nos permita calcular el area y perimetro de las figuras geometricas dadaos los lados
import os
import math

def limpiar():
	os.system('cls')

def main():
	print("\n\t Calculadora Geometrica")
	print("____________________________________________\n")
	print("Presione 0 para salir")
	opcion = int(input("Ingrese el numero de lados de la figra geometrica: "))
	if(opcion ==0):
		exit()
	else:
		limpiar()
		menu(opcion)

def menu(opcion):
	if(opcion<3):
		print("Ingrese un numero de lados valido\n")
		print("Presione ENTER para continuar\n")
		raw_input()
		limpiar()
		main()
	elif(opcion == 3):
		print("\t TRIANGULO")
		a = float(input("Ingrese el lado A: "))
		b = float(input("Ingrese el lado B: "))
		c = float(input("Ingrese el lado C: "))

		if(a + b) > c:
			if(a + c) > b:
				if (b + c) > a:
					triangulo(a,b,c)
					raw_input()
					limpiar()
					main()

				else:
					print("No es un triangulo")
			else:
				print("No es un triangulo")
		else:
			print("No es un triangulo")
	elif(opcion ==4):
		
		print("1. Cuadrado")
		print("2. Rectangulo")
		op= int(input("\t Elija una opcion:\n"))
		if(op==1):
			print("CUADRADO\n")
			a = float(input("Ingrese el lado A: "))
			cuadrado(a)
			raw_input()
			limpiar()
			main()
		elif(op==2):
			print("RECTANGULO\n")
			a = float(input("Ingrese el lado A: "))
			b = float(input("Ingrese el lado B: "))
			rectangulo(a,b)
			raw_input()
			limpiar()
			main()
		else:
			print("opcion invalida\n")

def cuadrado(a):
 	perimetro= a * 4
 	area = a**2
 	print ("el perimetro es: " + str(perimetro))
 	print ("el area es: " + str(round(area,3)))

def rectangulo(a,b):
 	perimetro= (a*2)+(b*2)
 	area = a*b
 	print ("el perimetro es: " + str(perimetro))
 	print ("el area es: " + str(round(area,3)))

def triangulo(a,b,c):
 	perimetro= a + b + c
 	s=(a+b+c)/2
 	raiz=s*(s-a)*(s-b)*(s-c)
 	area=math.sqrt(raiz)
 	print ("el perimetro es: " + str(perimetro))
 	print ("el area es: " + str(round(area,3)))




main()