from tkinter import *
from tkinter import messagebox as tkMessageBox
import sqlite3
def ResulReg():
    tkMessageBox.showinfo("Registro","El registro se ha realizado con éxito")


def VentanaRegistro():
    VentanaRegistro = Tk()
    VentanaRegistro.title("Registro de Usuarios")
    VentanaRegistro.geometry("600x600+100+100")

    Label(VentanaRegistro,text="PROTECO",font="Arial 30 bold").place(x=415,y=30)
    Label(VentanaRegistro,text="BOOKS",font="Arial 30 bold").place(x=450,y=70)
    nombre=StringVar()
    apellido=StringVar()
    edad=StringVar()
    NomUser=StringVar()
    Password=StringVar()
    Label(VentanaRegistro,text="Ingresa los datos que se te piden",font="Arial 20 bold").place(x=150,y=150)

    Label(VentanaRegistro,text="Nombres").place(x=270,y=200)
    nom=Entry(VentanaRegistro,textvariable=nombre,justify="center").place(x=210,y=230)
    Label(VentanaRegistro,text="Apellidos").place(x=270,y=260)
    apl=Entry(VentanaRegistro,textvariable=apellido,justify="center").place(x=210,y=290)
    Label(VentanaRegistro,text="Edad").place(x=280,y=320)
    edd=Entry(VentanaRegistro,textvariable=edad,justify="center").place(x=210,y=350)
    Label(VentanaRegistro,text="Nombre de Usuario").place(x=250,y=380)
    nUser=Entry(VentanaRegistro,textvariable=NomUser,justify="center").place(x=210,y=410)
    Label(VentanaRegistro,text="Contraseña").place(x=260,y=440)
    nUser=Entry(VentanaRegistro,textvariable=Password,justify="center").place(x=210,y=470)


    Button(VentanaRegistro,text="Registrar",font="Arial 20 bold",command=ResulReg).place(x=240,y=530)






    VentanaRegistro.mainloop()

def Salir():
    exit(0)

primerVentana=Tk()
primerVentana.geometry("700x700+50+50")

background_image=PhotoImage(file="backg.gif")
background_label = Label(primerVentana, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

primerVentana.config(bg="white")
primerVentana.title("PROTECO BOOKS")

logo=PhotoImage(file="Captura.gif")
labelImagen=Label(primerVentana,image=logo).place(x=20,y=20)

labelTitle=Label(primerVentana,text="PROTECO",font="Arial 30 bold").place(x=515,y=30)
labelTitle=Label(primerVentana,text="BOOKS",font="Arial 30 bold").place(x=550,y=70)

UpUser = Button(primerVentana,text="Registrar Usuario",font="Arial 20 bold",command=VentanaRegistro).place(x=270,y=250)
InUser = Button(primerVentana,text="Iniciar Sesión",font="Arial 20 bold").place(x=280,y=330)
End = Button(primerVentana,text="Salir",font="Arial 20 bold",command=Salir).place(x=320,y=410)

##Para el registro se abre una nueva ventana a manera de objeto

primerVentana.mainloop()
