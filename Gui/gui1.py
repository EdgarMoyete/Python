from tkinter import *

raiz = Tk()

mi_frame = Frame(raiz, width = 400, height = 300)
mi_frame.pack()

# mi_img = PhotoImage(file = "python_logo_vector.png")
Label(mi_frame, text='Hola mundo en GUI con Python', font=('18')).place(x=50, y=50)
# Label(mi_frame, image = mi_img).place(x = 10, y = 20)

txt = Entry(mi_frame)
txt.place(x=10, y=10)

raiz.mainloop()