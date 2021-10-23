from sqlite3.dbapi2 import paramstyle
from tkinter import ttk 
from tkinter import *
import CambiarHoras

import sqlite3

class Horario:

    baseDatos = 'Horario.db'

    def __init__(self,root):

        #Crea los 2 Frames

        self.wind = root
        self.wind.title('Generador de Horarios UV')
        self.wind.geometry('1500x800')

        CambiarHoras.Horas(root)

        frame1 = generarFrame(self,'Añadir Asignatura')
        frame2 = generarFrame(self,'Horario')
        frame3 = generarFrame(self,'Materias')

        frame1.pack(fill="both", expand="yes", padx=20,pady=1)
        frame2.pack(fill="x", expand="yes", padx=20,pady=1)
        frame3.pack(fill="both", expand=True, padx=20,pady=1)

        #Crea el header de la tabla

        self.trv = ttk.Treeview(frame2,columns=(1,2,3,4,5,6,7),show="headings",height="15")
        self.trv.pack()

        self.trv.heading(1,text="Hora")
        self.trv.heading(2,text="Lunes")
        self.trv.heading(3,text="Martes")
        self.trv.heading(4,text="Miercoles")
        self.trv.heading(5,text="Jueves")
        self.trv.heading(6,text="Viernes")
        self.trv.heading(7,text="Sabado")

        #Debo hacer el llamado de la funcion consulta para mostrar el contenido en la tabla

        self.consulta()

        #Aquí empiezan a generarse botones

        label1 = generarTexto(self,frame1,"Tipo de Hora",0,0)


    #Crea la conexion con la base de datos

    def runQuery(self,query,parameters = ()):
        with sqlite3.connect(self.baseDatos) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query,parameters)
            conn.commit()

            return result

    def consulta(self):
        book = self.trv.get_children()

        for i in book:
            self.trv.delete(i)

        query = 'SELECT Hora,Lunes,Martes,Miercoles,Jueves,Viernes,Sabado FROM Horario'
        rows = self.runQuery(query)

        listaHoras = []

        for j in rows:
            listaHoras.append(j[0])
            self.trv.insert("",0,text=j[1],values=j)

        print(listaHoras)

        tublaCambiar = tuple(listaHoras[0:10])
        print(tublaCambiar)
        return tublaCambiar



    def actualizarHoras(self):

        horasMilitares = self.consulta()

        nuevasHoras = ('9 pm a 10 pm','8 pm a 9 pm','7 pm a 8 pm','6 pm a 7 pm','5 pm a 6 pm','4 pm a 5 pm','3 pm a 4 pm','2 pm a 3 pm','1 pm a 2 pm','12 pm a 1 pm')


        query = 'UPDATE Horario SET Horas = ?  WHERE Horas = ?'

        for i in horasMilitares:
            for j in nuevasHoras:

                print("i =",i,"j =",j)

                parameters = (i,j)
                self.runQuery(query,parameters)
                self.consulta()


        



def generarFrame(self,texto):
    nombreFrame = LabelFrame(self.wind, text=texto, font=("Calibri",14))
    return nombreFrame


def generarTexto(self, ubicacion,texto,fila,colummna):

    label = Label(ubicacion,text=texto,width=20)
    label.grid(row=fila,column=colummna,padx=5,pady=3)
    return label








if __name__ == '__main__':
    root = Tk()
    product = Horario(root)
    root.mainloop()
