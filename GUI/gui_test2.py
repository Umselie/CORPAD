# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 21:11:47 2019

@author: Doreen
"""
import words
import get_sentence_with_blank
from tkinter import *
import config
# creating basic window
window = Tk()


window.title("CORPAD")

korpus =  'jpWaC-L3.vert'
vokabel = getword('N5')[1]

################################### functions ######################################

def go_to_level(level,corpus):
    frame2.pack()
    frame1.pack_forget()
    config.globallevel = level
    config.globalcorpus = corpus
    
def show_solution():
    solution_label.config(text= config.globalsolution)
    weiter.pack()
    
def update_sentence():
    sentence.config(text = fixed_word(getword(config.globallevel)[1], config.globalcorpus))
    weiter.pack_forget()
    solution_label.config(text= '')

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

# Frame 2
frame2 = Frame(window)

sentence = Label(frame2, font = ('arial', 20), text= fixed_word(getword(config.globallevel)[1], config.globalcorpus))
sentence.pack() 

solution = Button(frame2, font = ('arial', 18),text = "Lösung", fg = "black", cursor = "hand2", command = lambda: show_solution())
solution.pack()              

solution_label = Label(frame2,font = ('arial', 18),text ='')
solution_label.pack()   

weiter = Button(frame2, font = ('arial', 18),text = "weiter", fg = "black", cursor = "hand2", command = lambda: update_sentence())    

window.mainloop()