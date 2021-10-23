from io import open_code
from sqlite3.dbapi2 import paramstyle
from tkinter import ttk 
from tkinter import *
import sqlite3
import Interfaz

class Horas:

    baseDatos = 'Horario.db'


    def __init__(self,root):

        def seleccionar(event):
            if opcion1.get() == "Estilo Militar" :
                pass
            elif opcion1.get() == "Estilo Normal":
                interfaz = Interfaz.Horario(root)
                interfaz.consulta()
            else:
                pass


        opciones = ["Estilo Militar","Estilo Normal"]

        eleccion = StringVar()
        eleccion.set(opciones[0])

        opcion1 = ttk.Combobox(root, values = opciones)
        opcion1.current(0)
        opcion1.bind("<<ComboboxSelected>>",seleccionar)
        opcion1.pack(padx=1,pady=5)




    
