from tkinter import *

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
primerVentana.mainloop()