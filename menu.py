import random
 
from tkinter import *
 
import sqlite3
 
import os
 
class Interface(Frame):
 
    def __init__(self, fenetre, **kwargs):
 
        Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
 
        self.pack(fill=BOTH)
 
        self.code_label = Label(self, text="Code",bg="blue",fg="white",font = ("Impact", 32))
 
        self.code_label.grid(row=0,column=0)
 
        self.designation_label = Label(self, text="Désignation",bg="blue",fg="white",font = ("Impact", 32))
 
        self.designation_label.grid(row=2,column=0)
 
        self.qt_label = Label(self, text="Quantitées",bg="blue",fg="white",font = ("Impact", 32))
 
        self.qt_label.grid(row=4,column=0)
 
                  
 
        self.code_entry = StringVar()
 
        self.code_entry_entry = Entry(self, textvariable=self.code_entry,width=50,font = ("Impact", 20))
 
        self.code_entry_entry.grid(row=1,column=0)
 
                    
 
        self.designation_entry = StringVar()
 
        self.designation_entry_entry = Entry(self, textvariable=self.designation_entry,width=50,font = ("Helvetica", 20))
 
        self.designation_entry_entry.grid(row=3,column=0)
 
                     
 
        self.quantite_entry = StringVar()
 
        self.qt_entry = Entry(self, textvariable=self.quantite_entry,width=50,font = ("Helvetica", 20))
 
        self.qt_entry.grid(row=5,column=0)
 
        self.bind('<Return>', self.savedata)
 
        self.u_ent_btn = Button(self, text="Valider",command=self.congo,font = ("Impact", 20),bg="blue",fg="white")
 
        self.u_ent_btn.grid(row=6,column=0)
 
    def fermer(self):
 
        print("je sais")
 
    def africa(self):
 
        self.conn = sqlite3.connect('database.db')
 
        self.c = conn.cursor()
 
        self.c.execute("CREATE TABLE IF NOT EXISTS produit (Code TEXT, Designation TEXT, Quantite REAL)")
 
        self.conn.commit()
 
        self.conn.close()
 
        return self.conn
 
    def congo (self):
 
        print(dir(self.code_entry))
 
        self.conn = sqlite3.connect('database.db')
 
        self.c = conn.cursor()
 
        self.c.execute('INSERT INTO produit (Code, Designation, Quantite) VALUES (?,?,?)', (self.code_entry.get(), self.designation_entry.get(),self.quantite_entry.get()))
 
        self.conn.commit()
 
        self.code_entry_entry.delete(0,'end')
 
        self.designation_entry_entry.delete(0,'end')
 
        self.qt_entry.delete(0,'end')
 
        print("OK")
 
fenetre = Tk()
 
interface = Interface(fenetre)
 
interface.configure(bg="blue")
 
interface.mainloop()
