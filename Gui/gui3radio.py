from tkinter import *
from tkinter import messagebox

def imprimir():
    lbl.config(text=varOpcion.get())

def opciones():
    cad=""
    if rojo.get()==1:
        cad+="rojo"
    if verde.get()==1:
        cad+="verde"
    if azul.get()==1:
        cad+="azul"
    lbl2.config(text=cad)

def ventana():
    messagebox.showinfo("Parametro 1", "Parametro 2")

root = Tk()
root.title("GUI")

frame=Frame(root)
frame.pack()

varOpcion=IntVar()
Radiobutton(frame, text="Masculino", variable=varOpcion, value=1, command=imprimir).pack()
Radiobutton(frame, text="Femenino", variable=varOpcion, value=2, command=imprimir).pack()

lbl=Label(frame)
lbl.pack()

rojo=IntVar()
verde=IntVar()
azul=IntVar()
Checkbutton(frame, text='Rojo', variable=rojo, onvalue=1, offvalue=0, command=opciones).pack()
Checkbutton(frame, text='Verde', variable=verde, onvalue=1, offvalue=0, command=opciones).pack()
Checkbutton(frame, text='Azul', variable=azul, onvalue=1, offvalue=0, command=opciones).pack()

lbl2=Label(frame)
lbl2.pack()

btn = Button(frame, text="Ventana", command=ventana)
btn.pack()

root.mainloop()