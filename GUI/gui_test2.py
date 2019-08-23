# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 21:11:47 2019

@author: Doreen
"""

import get_sentence_with_blank
from tkinter import *
import config
import update

# creating basic window
window = Tk()
window.geometry('800x500')

window.title("CORPAD")


################################### functions ######################################

def go_to_level(level,corpus):
    frame2.pack()
    frame1.pack_forget()
    config.globallevel = level
    config.globalcorpus = corpus
    getwordslists(level)
    sentence.config(text = fixed_word(getword()[1], config.globalcorpus))
    sentence.grid(row=0)
    #sentence.config(text = 'ada')
    
def show_solution():
    solution_label.config(text= config.globalsolution)
    frame3.pack()
    
def update_sentence(quality):
    updateCard(quality)
    sentence.config(text = fixed_word(getword()[1], config.globalcorpus))
    frame3.forget()
    solution_label.config(text= '')
    bedeutung_label.config(text= '')
    
def show_meaning():
    bedeutung_label.config(text = config.global_current_word[3])

 # Frame 1: Levelauswahl
frame1 = Frame(window)
frame1.pack()
b5 = Button(frame1, font = ('arial', 18),text = "N5", command = lambda: go_to_level('N5','jpWaC-L4.vert'))
b4 = Button(frame1, font = ('arial', 18),text = "N4", command = lambda: go_to_level('N4','jpWaC-L3.vert'))
b3 = Button(frame1, font = ('arial', 18),text = "N3", command = lambda: go_to_level('N3','jpWaC-L2.vert'))
b2 = Button(frame1, font = ('arial', 18),text = "N2", command = lambda: go_to_level('N2','jpWaC-L1.vert'))
b1 = Button(frame1, font = ('arial', 18),text = "N1", command = lambda: go_to_level('N1','jpWaC-L0.vert'))
b5.pack()
b4.pack()
b3.pack()
b2.pack()
b1.pack()

# Frame 2: Sätze mit Lücke
frame2 = Frame(window)

sentence = Label(frame2, font = ('arial', 14), text= '')
sentence.grid(row = 0)
#sentence.pack() 

solution = Button(frame2, font = ('arial', 14),text = "Lösung", fg = "black", cursor = "hand2", command = lambda: show_solution()).grid(row = 1)
#solution.pack()              

solution_label = Label(frame2,font = ('arial', 14),text ='')
solution_label.grid(row=2)
#solution_label.pack()

bedeutung = Button(frame2, font = ('arial', 14),text = "Bedeutung", fg = "black", cursor = "hand2", command = lambda: show_meaning()).grid(row = 1, column = 1)
bedeutung_label = Label(frame2,font = ('arial', 14),text ='')
bedeutung_label.grid(row=2, column = 1)

frame3 = Frame(window)
d0 = Button(frame3, font = ('arial', 14),text = "0", command = lambda: update_sentence(0)).grid(row=0,column=0)
d1 = Button(frame3, font = ('arial', 14),text = "1",  command = lambda: update_sentence(1)).grid(row=0,column=1)
d2 = Button(frame3, font = ('arial', 14),text = "2",  command = lambda: update_sentence(2)).grid(row=0,column=2)
d3 = Button(frame3, font = ('arial', 14),text = "3",  command = lambda: update_sentence(3)).grid(row=0,column=3)
d4 = Button(frame3, font = ('arial', 14),text = "4",  command = lambda: update_sentence(4)).grid(row=0,column=4)
d5 = Button(frame3, font = ('arial', 14),text = "5",  command = lambda: update_sentence(5)).grid(row=0,column=5)

window.mainloop()