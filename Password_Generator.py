import string
import random
from tkinter import*
from tkinter import ttk
from tkinter import messagebox


letter = string.ascii_letters
num = string.digits  
punt = string.punctuation

def Generate_pass():
    printable = f'{letter}{num}{punt}'
    try:
        random_password = random.choices(printable,
         k=int(combopass.get()))
        random_password = ''.join(random_password)

        password.set(random_password)
    except:
        messagebox.askretrycancel(
            message="¿Desea reintentar?", 
        title="Error")


root = Tk()
root.config(bg="black")
root.title("Password Generator")
password = StringVar()
frame=Frame(root,bg="black")
frame2=Frame(root)
# Etiquetas
labeltam=Label(frame,text="Tamaño",
bg="black",fg="white")
labelpass = Label(frame, text="Password"
,bg="black",fg="white")

#Entry
entrypass = ttk.Entry(frame,textvariable=password,
width=30)

# lista desplegable
combopass =ttk.Combobox(frame,width=30) 
combopass['values']=[x for x in range(6,21)]

#Botones
btngrate = ttk.Button(frame2,text="Generar",
command=Generate_pass)



labeltam.grid(row=0,column=1,pady=10,padx=10)
labelpass.grid(row=1,column=1,pady=10,padx=15)
entrypass.grid(row=1,column=2,padx=25)
combopass.grid(row=0,column=2,padx=25)
btngrate.grid(row=2,column=1)
frame.pack()
frame2.pack(side=BOTTOM)
root.mainloop()
