from tkinter import*
from math import*

raiz=Tk()
raiz.title("Calculadora")
raiz.iconbitmap("781760.ico")

miFrame=Frame(raiz)
miFrame.pack()
miFrame.config(bg="SkyBlue4")

operacion=""
reset_pantalla=False
resultado=0

#--------------------pantalla-------------------------------------

numeroPantalla=StringVar()

pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")

#--------------------pulsaciones teclado--------------------------

def numeroPulsado(num):

	global reset_pantalla

	if reset_pantalla!=False:
		numeroPantalla.set(num)
		reset_pantalla=False
	else:
		numeroPantalla.set(numeroPantalla.get() + num)
	
#--------------------funcion retroceder---------------------------

def Retroceder():

	global reset_pantalla

	reset_pantalla=True
	numeroPantalla.set(numeroPantalla.get()[:-1])
	
#--------------------funcion retroceder---------------------------

def Borrar():
	global reset_pantalla

	resultado="0"
	reset_pantalla=True
	numeroPantalla.set(resultado)
	
#--------------------funcion seno---------------------------------
def seno(num):

	global operacion
	global resultado

    resultado = sin(float(num))
   	operacion = "seno"
   	reset_pantalla = True
 	numeroPantalla.set(resultado)

#--------------------funcion raiz---------------------------------
contador_raiz=0
def RaizCuadrada(num):

	global resultado
	global operacion
	global reset_pantalla
	global contador_raiz
	global num1

	import math

	if contador_raiz==0:
		num=float(num1)
		resultado=num1
	else:
		if contador_raiz==1:
			resultado=math.sqrt(float(num))

		else:
			resultado=math.sqrt(float(resultado))

		numeroPantalla.set(resultado)
		resultado=numeroPantalla.get()

	contador_raiz+=1
	operacion="RaizCuadrada"
	reset_pantalla=True

#--------------------funcion cuadraro---------------------------------
contador_cuadrado=0

def Cuadrado(num):

	global resultado
	global operacion
	global reset_pantalla
	global contador_cuadrado
	global num1

	if contador_cuadrado==0:
		num=float(num1)
		resultado=num1
	else:
		if contador_cuadrado==1:
			resultado=float(num)**2
		else:
			resultado=float(resultado)**2
		numeroPantalla.set(resultado)
		resultado=numeroPantalla.get()

	contador_cuadrado+=1
	operacion="Cuadrado"
	reset_pantalla=True

#--------------------funcion suma---------------------------------

def suma(num):

	global resultado
	global operacion
	global reset_pantalla

	resultado+=float(num)
	operacion="suma"
	reset_pantalla=True
	numeroPantalla.set(resultado)

#--------------------funcion resta---------------------------------
num1=0
contador_resta=0

def resta(num):

	global resultado
	global operacion
	global num1
	global reset_pantalla
	global contador_resta

	if contador_resta==0:
		num=float(num1)
		resultado=num1
	else:
		if contador_resta==1:
			resultado=num1-float(num)
		else:
			resultado=float(resultado)-float(num)
		numeroPantalla.set(resultado)
		resultado=numeroPantalla.get()

	contador_resta+=1
	operacion="resta"
	reset_pantalla=True

#--------------------funcion multiplicacion---------------------------------
contador_multi=0
def multiplica(num):

	global resultado
	global operacion
	global contador_multi
	global num1
	global reset_pantalla

	if contador_multi==0:
		num1=float(num)
		resultado=num1
	else:
		if contador_multi==1:
			resultado=num1*float(num)
		else:
			resultado= float(resultado)*float(num)
		numeroPantalla.set(resultado)
		resultado=numeroPantalla.get()
	contador_multi+=1
	operacion="multiplica"
	reset_pantalla=True

#--------------------funcion divide---------------------------------
contador_divi=0

def divide(num):

	global resultado
	global operacion
	global contador_divi
	global num1
	global reset_pantalla

	if contador_divi==0:
		num1=float(num)
		resultado=num1
	else:
		try:
			if contador_divi==1:
				resultado=num1/float(num)
			else:
				resultado=float(resultado)/float(num)
			numeroPantalla.set(resultado)
			resultado=numeroPantalla.get()
		except ZeroDivisionError:
			Borrar()
			resultado="error"
			numeroPantalla.set(resultado)

	operacion="divide"
	contador_divi+=1
	reset_pantalla=True

#--------------------funcion el_resultado---------------------------------

def el_resultado():

	global resultado
	global operacion
	global contador_resta
	global contador_multi
	global contador_divi
	global contador_cuadrado
	global contador_raiz

	if operacion=="suma":
		numeroPantalla.set(resultado+float(numeroPantalla.get()))
		resultado=0

	elif operacion=="resta":
		numeroPantalla.set(float(resultado)-float(numeroPantalla.get()))
		resultado=0
		contador_resta=0

	elif operacion=="multiplica":
		numeroPantalla.set(float(resultado)*float(numeroPantalla.get()))
		resultado=0
		contador_multi=0

	elif operacion=="divide":
		numeroPantalla.set(float(resultado)/float(numeroPantalla.get()))
		resultado=0
		contador_divi=0

	elif operacion=="Cuadrado":
		numeroPantalla.set(float(numeroPantalla.get())**2)
		resultado=0
		contador_cuadrado=0

	elif operacion=="RaizCuadrada":
		numeroPantalla.set(math.sqrt(float(numeroPantalla.get())))
		resultado=0
		contador_raiz=0

#--------------------fila 0---------------------------------------

botonBorrar=Button(miFrame, text="CE", width=3, command=lambda:Borrar)
botonBorrar.grid(row=2, column=1)
botonRetrocede=Button(miFrame, text="<--", width=3, command=lambda:Retroceder)
botonRetrocede.grid(row=2,column=2)
botonCuadrado=Button(miFrame, text="x²", width=3, command=lambda:Cuadrado)
botonCuadrado.grid(row=2, column=3)
botonRaiz=Button(miFrame, text="√", width=3, command=lambda:RaizCuadrada)
botonRaiz.grid(row=2, column=4)
botonSeno=Button(miFrame, text="sin", width=3, command=lambda:seno(numeroPantalla.get()))
botonSeno.grid(row=2, column=5)


#--------------------fila 1---------------------------------------

boton7=Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=3, column=1)
boton8=Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=3, column=2)
boton9=Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=3, column=3)
botonDiv=Button(miFrame, text="/", width=3, command=lambda:divide(numeroPantalla.get()))
botonDiv.grid(row=3, column=4)

#--------------------fila 2---------------------------------------

boton4=Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=4, column=1)
boton5=Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=4, column=2)
boton6=Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=4, column=3)
botonMult=Button(miFrame, text="X", width=3, command=lambda:multiplica(numeroPantalla.get()))
botonMult.grid(row=4, column=4)


#--------------------fila 3---------------------------------------

boton1=Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=5, column=1)
boton2=Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=5, column=2)
boton3=Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=5, column=3)
botonRest=Button(miFrame, text="-", width=3, command=lambda:resta(numeroPantalla.get()))
botonRest.grid(row=5, column=4)

#--------------------fila 4---------------------------------------

boton0=Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=6, column=1)
botonComa=Button(miFrame, text=",", width=3, command=lambda:numeroPulsado(","))
botonComa.grid(row=6, column=2)
botonIgual=Button(miFrame, text="=", width=3, command=lambda:el_resultado())
botonIgual.grid(row=6, column=3)
botonSuma=Button(miFrame, text="+", width=3, command=lambda:suma(numeroPantalla.get()))
botonSuma.grid(row=6, column=4)


raiz.mainloop()