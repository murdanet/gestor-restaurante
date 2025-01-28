import sqlite3
from unittest.mock import right

import _sqlite3
from tkinter import *

#Configuracion de la raíz
root = Tk()
root.title("Bar Celona - Menú")
root.resizable(0,0)
root.config(bd=25,relief="sunken")

Label(root, text="   Bar    Celona   ", fg="darkblue", font=("Times New Roman",28,"bold italic")).pack()
Label(root, text="Menú del día  ", fg="blue", font=("Times New Roman",22,"bold italic")).pack()

#Separación de titulos y categorías
Label(root,text="").pack()

conexion= sqlite3.connect("restaurante.db")
cursor=conexion.cursor()

#Buscar las categorías y platos de la BBDD
categorias = cursor.execute("SELECT * FROM categoria").fetchall()
for categoria in categorias:
        Label(root, text=categoria[1],fg="black", font=("Times New Roman",18,"bold italic")).pack()
        platos = cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(categoria[0])).fetchall()
        for plato in platos:
            Label(root, text=plato[1], fg="gray", font=("Verdana", 14, "italic")).pack()

#Separación entre categorías
Label(root,text="").pack()


conexion.close()

#Precio del menu
Label(root, text="13.80(IVA incl)", fg="darkblue", font=("Times New Roman", 18, "bold italic")).pack(side="right")

#Ejecutamos el bucle de aplicación
root.mainloop()
