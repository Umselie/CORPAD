# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 21:11:47 2019

@author: Doreen
"""

import get_sentence_with_blank
from tkinter import *
from tkinter import messagebox
import config
import update

# creating basic window
window = Tk()
window.geometry('800x500')

window.title("CORPAD")


################################### Funktionen ######################################

def go_to_level(level,corpus):
    config.globallevel = level
    config.globalcorpus = corpus
    getwordslists(level)
    if not config.global_new_and_revisions:
        messagebox.showinfo("Info", "Keine neuen Wörter zum Lernen!")
    if config.global_new_and_revisions:
        sentence.config(text = fixed_word(getword()[1], config.globalcorpus))
        sentence.grid(row=0)
        frame1.pack_forget()
        frame2.pack()
    
def show_solution():
    solution_label.config(text= config.globalsolution+'\n'+config.global_current_word[2])
    frame3.pack()
    
def update_sentence(quality):
    updateCard(quality)
    config.global_new_and_revisions.remove(config.global_current_word)
    print(config.global_new_and_revisions)
    if not config.global_new_and_revisions:
        if messagebox.askyesno("Message", "Alle Worte für heute gelernt!\n Willst du in diesem Level witerlernen?"):
          go_to_level(config.globallevel,config.globalcorpus)  
        else:
            go_to_levelauswahl()
    if config.global_new_and_revisions:
        sentence.config(text = fixed_word(getword()[1], config.globalcorpus))
        frame3.pack_forget()
        solution_label.config(text= '')
        bedeutung_label.config(text= '')
    
def show_meaning():
    bedeutung_label.config(text = config.global_current_word[3])
    
def go_to_reset():
    frame4.pack()
    frame1.pack_forget()
    frame2.pack_forget()
    
def click_reset_level(level):
    reset(level)
    messagebox.showinfo("Info", level + " wurde zurückgesetzt")
    
def go_to_levelauswahl():
    frame1.pack()
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()

if __name__== "__main__":
     # Frame 1: Levelauswahl
    frame1 = Frame(window)
    frame1.pack()
    levelauswahl_label = Label(frame1,font = ('arial', 14),text ='Wähle einen JLPT-Level aus:')
    b5 = Button(frame1, font = ('arial', 18),text = "N5", command = lambda: go_to_level('N5','jpWaC-L4.vert'))
    b4 = Button(frame1, font = ('arial', 18),text = "N4", command = lambda: go_to_level('N4','jpWaC-L3.vert'))
    b3 = Button(frame1, font = ('arial', 18),text = "N3", command = lambda: go_to_level('N3','jpWaC-L2.vert'))
    b2 = Button(frame1, font = ('arial', 18),text = "N2", command = lambda: go_to_level('N2','jpWaC-L1.vert'))
    b1 = Button(frame1, font = ('arial', 18),text = "N1", command = lambda: go_to_level('N1','jpWaC-L0.vert'))
    levelauswahl_label.pack(padx=5)
    b5.pack()
    b4.pack()
    b3.pack()
    b2.pack()
    b1.pack()
    
    # Frame 2: Sätze mit Lücke
    frame2 = Frame(window)
    
    sentence = Label(frame2, font = ('arial', 14), text= '')
    sentence.grid(row = 0, columnspan = 2,padx = 5,pady = 5)
    
    
    solution = Button(frame2, font = ('arial', 14),text = "Lösung", command = lambda: show_solution()).grid(row = 1, column = 1,padx=5,pady =5)
                 
    
    solution_label = Label(frame2,font = ('arial', 14),text ='')
    solution_label.grid(row=2, column = 1,padx=5,pady =5)
    
    
    bedeutung = Button(frame2, font = ('arial', 14),text = "Bedeutung", command = lambda: show_meaning()).grid(row = 1,padx=5,pady =5)
    bedeutung_label = Label(frame2,font = ('arial', 14),text ='')
    bedeutung_label.grid(row=2,padx=5)
    
    # Frame zur Bewertung der Schwierigkeit auf einer Skala von 0-5:
    frame3 = Frame(window)
    d0 = Button(frame3, font = ('arial', 14),text = "0", command = lambda: update_sentence(0)).grid(row=0,column=0, padx = 5,pady = 5)
    d1 = Button(frame3, font = ('arial', 14),text = "1", command = lambda: update_sentence(1)).grid(row=0,column=1, padx = 5,pady = 5)
    d2 = Button(frame3, font = ('arial', 14),text = "2", command = lambda: update_sentence(2)).grid(row=0,column=2, padx = 5,pady = 5)
    d3 = Button(frame3, font = ('arial', 14),text = "3", command = lambda: update_sentence(3)).grid(row=0,column=3, padx = 5,pady = 5)
    d4 = Button(frame3, font = ('arial', 14),text = "4", command = lambda: update_sentence(4)).grid(row=0,column=4, padx = 5,pady = 5)
    d5 = Button(frame3, font = ('arial', 14),text = "5", command = lambda: update_sentence(5)).grid(row=0,column=5, padx = 5,pady = 5)
    
    # Menü
    menubar = Menu(window)
    submenu = Menu(menubar, tearoff=0)
    submenu.add_command(label="Zurücksetzen", command = lambda: go_to_reset())
    submenu.add_command(label="Levelauswahl", command = lambda: go_to_levelauswahl())
    submenu.add_command(label="Exit", command = window.destroy)
    
    menubar.add_cascade(label="Optionen", menu=submenu)
    window.config(menu=menubar)
    
    # Frame zum zurücksetzen der gelernten Wörter
    frame4 = Frame(window)
    r5 = Button(frame4, font = ('arial', 18),text = "N5 zurücksetzen", command = lambda: click_reset_level('N5'))
    r4 = Button(frame4, font = ('arial', 18),text = "N4 zurücksetzen", command = lambda: click_reset_level('N4'))
    r3 = Button(frame4, font = ('arial', 18),text = "N3 zurücksetzen", command = lambda: click_reset_level('N3'))
    r2 = Button(frame4, font = ('arial', 18),text = "N2 zurücksetzen", command = lambda: click_reset_level('N2'))
    r1 = Button(frame4, font = ('arial', 18),text = "N1 zurücksetzen", command = lambda: click_reset_level('N1'))
    back = Button(frame4, font = ('arial', 14),text = "Zurück zur Levelauswahl", command = lambda: go_to_levelauswahl())
    r5.grid(row = 0,pady=5)
    r4.grid(row=1,pady=5)
    r3.grid(row=2,pady=5)
    r2.grid(row=3,pady=5)
    r1.grid(row=4,pady=5)
    back.grid(row=6,pady=20)
    window.mainloop()

