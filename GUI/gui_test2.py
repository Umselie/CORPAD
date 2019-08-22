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


def show_solution():
    solution_label.config(text= config.globalsolution)



frame2 = Frame(window)
frame2.pack(side = TOP)

sentence = Label(frame2, font = ('arial', 20), text= fixed_word(vokabel, korpus))
sentence.pack() 

solution = Button(frame2, font = ('arial', 18),text = "Lösung", fg = "black", cursor = "hand2", command = lambda: show_solution())
solution.pack()              

solution_label = Label(frame2,font = ('arial', 18),text ='')
solution_label.pack()   
      

window.mainloop()