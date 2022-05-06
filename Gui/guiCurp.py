from tkinter import Tk, Frame, Label, Entry, Button, StringVar

# funciones

def abreviar_estado(estado):
    # se podria mejorar usando un combo box y asi en lugar de comparar cadenas
    # se compararian numeros
    if estado == "PUEBLA":
        abreviacion = "PL"
    elif estado == "CUIDAD DE MEXICO":
        abreviacion = "DF"
    # poner un elif por cada estado
    else:
        abreviacion = "XX"
    return abreviacion

def primer_consonante(cad):
    for i in range(1, len(cad)):
        if cad[i] != "A" and cad[i] != "E" and cad[i] != "I" and cad[i] != "O" and cad[i] != "U":
            letra = cad[i]
            break
        else:
            letra = "X"
    return letra

def obtener_curp():
    pat = paterno.get().upper()
    mat = materno.get().upper()
    nom = nombre.get().upper()
    ani = anio.get()
    me = mes.get()
    di = dia.get()
    sex = sexo.get().upper()
    est = abreviar_estado(estado.get().upper())
    conso_pat = primer_consonante(pat)
    conso_mat = primer_consonante(mat)
    conso_nom = primer_consonante(nom)

    cad = pat[0:2] + mat[0] + nom[0] + ani[2:] + me + di + sex + est + conso_pat + conso_mat + conso_nom + "00"
    curp.set(cad)

root = Tk()
frame = Frame()
frame.pack()

nombre = StringVar()
lbl_nombres = Label(frame, text = 'Nombres:')
lbl_nombres.grid(row = 0, column = 0)
txt_nombres = Entry(frame, textvariable=nombre)
txt_nombres.grid(row = 0, column = 1)

paterno = StringVar()
lbl_ape_paterno = Label(frame, text = 'Primer apellido:')
lbl_ape_paterno.grid(row = 1, column = 0)
txt_ape_paterno = Entry(frame, textvariable=paterno)
txt_ape_paterno.grid(row = 1, column = 1)

materno = StringVar()
lbl_ape_materno = Label(frame, text = 'Segundo apellido:')
lbl_ape_materno.grid(row = 2, column = 0)
txt_ape_materno = Entry(frame, textvariable=materno)
txt_ape_materno.grid(row = 2, column = 1)

dia = StringVar()
lbl_dia = Label(frame, text = 'Día de nacimiento:')
lbl_dia.grid(row = 3, column = 0)
txt_dia = Entry(frame, textvariable=dia)
txt_dia.grid(row = 3, column = 1)

mes = StringVar()
lbl_mes = Label(frame, text = 'Mes de nacimiento:')
lbl_mes.grid(row = 4, column = 0)
txt_mes = Entry(frame, textvariable=mes)
txt_mes.grid(row = 4, column = 1)

anio = StringVar()
lbl_anio = Label(frame, text = 'Año de nacimiento:')
lbl_anio.grid(row = 5, column = 0)
txt_anio = Entry(frame, textvariable=anio)
txt_anio.grid(row = 5, column = 1)

sexo = StringVar()
lbl_sexo = Label(frame, text = 'Sexo:')
lbl_sexo.grid(row = 6, column = 0)
txt_sexo = Entry(frame, textvariable=sexo)
txt_sexo.grid(row = 6, column = 1)

estado = StringVar()
lbl_estado = Label(frame, text = 'Estado:')
lbl_estado.grid(row = 7, column = 0)
txt_estado = Entry(frame, textvariable=estado)
txt_estado.grid(row = 7, column = 1)

curp = StringVar()
btn = Button(frame, text="Buscar", command=obtener_curp)
btn.grid(row=8, column=0)
txt_curp = Entry(frame, textvariable=curp)
txt_curp.grid(row = 8, column = 1)

root.mainloop()