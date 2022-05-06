from tkinter import *

def enviar():
    abc.set('Enviando')

raiz = Tk()

mi_frame = Frame(raiz, width = 400, height = 300)
mi_frame.pack()

abc = StringVar()

lbl_nombre = Label(mi_frame, text = 'Nombres:')
lbl_nombre.grid(row = 0, column = 0, sticky = 'w', padx = 4, pady = 4)

txt_nombre = Entry(mi_frame, textvariable = abc)
txt_nombre.grid(row = 0, column = 1, padx = 4, pady = 4)

lbl_apellido = Label(mi_frame, text='Apellidos:')
lbl_apellido.grid(row = 1, column = 0, sticky = 'w', padx = 4, pady = 4)

txt_apellido = Entry(mi_frame)
txt_apellido.grid(row = 1, column = 1, padx = 4, pady = 4)

lbl_pass = Label(mi_frame, text='pass:')
lbl_pass.grid(row = 2, column = 0, sticky = 'w', padx = 4, pady = 4)

txt_pass = Entry(mi_frame)
txt_pass.grid(row = 2, column = 1, padx = 4, pady = 4)
txt_pass.config(show = '*')

lbl_com = Label(mi_frame, text='comentarios:')
lbl_com.grid(row = 3, column = 0, sticky = 'w', padx = 4, pady = 4)

txt_grande = Text(mi_frame, width=16, height=8)
txt_grande.grid(row=3, column=1)

scroll_v = Scrollbar(mi_frame, command=txt_grande.yview)
scroll_v.grid(row=3, column=2, sticky="nsew")
txt_grande.config(yscrollcommand=scroll_v.set)

btn = Button(raiz, text="Enviar", command=enviar)
btn.pack()

raiz.mainloop()