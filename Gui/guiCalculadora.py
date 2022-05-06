from tkinter import *

def numeroPulsado(num):
    global operacion
    global reset
    if reset != False: # mejorar
        numero_pantalla.set(num)
        reset = False
    else:
        numero_pantalla.set(numero_pantalla.get() + num)

def suma(num):
    global operacion
    global resultado
    global reset
    operacion = 'suma'
    resultado += int(num)
    reset = True
    numero_pantalla.set(resultado)

num1 = 0
contador_resta = 0
def resta(num):
    global operacion
    global resultado
    global num1
    global contador_resta
    global reset
    if contador_resta == 0:
        num1 = int(num)
        resultado = num1
    else:
        if contador_resta == 1:
            resultado = num1 - int(num)
        else:
            resultado -= int(num)
        numero_pantalla.set(resultado)
        resultado = numero_pantalla.get()
    contador_resta = contador_resta + 1
    operacion = 'resta'
    reset = True

contador_multi = 0
def multiplicacion(num):
    global operacion
    global resultado
    global num1
    global contador_multi
    global reset
    if contador_multi==0:
        num1 = int(num)
        resultado = num1
    else:
        if contador_multi == 1:
            resultado = num1 * int(num)
        else:
            resultado *= int(num)
        numero_pantalla.set(resultado)
        resultado=numero_pantalla.get()
    contador_multi = contador_multi + 1
    operacion = 'multiplicacion'
    reset = True

contador_div = 0
def division(num):
    global operacion
    global resultado
    global num1
    global contador_div
    global reset
    if contador_div == 0:
        num1 = float(num)
        resultado = num1
    else:
        if contador_div == 1:
            resultado = num1 / float(num)
        else:
            resultado /= float(num)
        numero_pantalla.set(resultado)
        resultado = numero_pantalla.get()
    contador_div = contador_div + 1
    operacion = 'division'
    reset = True

def igual():
    global resultado
    global operacion
    global contador_resta
    global contador_multi
    global contador_div
    if operacion == 'suma':
        numero_pantalla.set(resultado + int(numero_pantalla.get()))
    elif operacion=='resta':
        numero_pantalla.set(resultado - int(numero_pantalla.get()))
        contador_resta = 0
    elif operacion=='multiplicacion':
        numero_pantalla.set(resultado * int(numero_pantalla.get()))
        contador_multi = 0
    elif operacion=='division':
        numero_pantalla.set(resultado / int(numero_pantalla.get()))
        contador_div = 0
    resultado = 0
raiz = Tk()

mi_frame=Frame(raiz)
mi_frame.pack()

operacion = ''
reset = False
resultado = 0

numero_pantalla = StringVar()
pantalla = Entry(mi_frame, textvariable=numero_pantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")

btn7 = Button(mi_frame, text='7', height=4, width=8, command=lambda: numeroPulsado('7'))
btn7.grid(row=2, column=1)
btn8 = Button(mi_frame, text='8', height=4, width=8, command=lambda: numeroPulsado('8'))
btn8.grid(row=2, column=2)
btn9 = Button(mi_frame, text='9', height=4, width=8, command=lambda: numeroPulsado('9'))
btn9.grid(row=2, column=3)
btndiv = Button(mi_frame, text='/', height=4, width=8, command=lambda: division(numero_pantalla.get()))
btndiv.grid(row=2, column=4)

btn4 = Button(mi_frame, text='4', height=4, width=8, command=lambda: numeroPulsado('4'))
btn4.grid(row=3, column=1)
btn5 = Button(mi_frame, text='5', height=4, width=8, command=lambda: numeroPulsado('5'))
btn5.grid(row=3, column=2)
btn6 = Button(mi_frame, text='6', height=4, width=8, command=lambda: numeroPulsado('6'))
btn6.grid(row=3, column=3)
btnmul = Button(mi_frame, text='x', height=4, width=8, command=lambda: multiplicacion(numero_pantalla.get()))
btnmul.grid(row=3, column=4)

btn1 = Button(mi_frame, text='1', height=4, width=8, command=lambda: numeroPulsado('1'))
btn1.grid(row=4, column=1)
btn2 = Button(mi_frame, text='2', height=4, width=8, command=lambda: numeroPulsado('2'))
btn2.grid(row=4, column=2)
btn3 = Button(mi_frame, text='3', height=4, width=8, command=lambda: numeroPulsado('3'))
btn3.grid(row=4, column=3)
btnres = Button(mi_frame, text='-', height=4, width=8, command=lambda: resta(numero_pantalla.get()))
btnres.grid(row=4, column=4)

btnpunto = Button(mi_frame, text='.', height=4, width=8)
btnpunto.grid(row=5, column=1)
btn0 = Button(mi_frame, text='0', height=4, width=8, command=lambda: numeroPulsado('0'))
btn0.grid(row=5, column=2)
btnigual = Button(mi_frame, text='=', height=4, width=8, command=lambda: igual())
btnigual.grid(row=5, column=3)
btnres = Button(mi_frame, text='+', height=4, width=8, command=lambda: suma(numero_pantalla.get()))
btnres.grid(row=5, column=4)

raiz.mainloop()