# -*- coding: utf-8 -*-
"""
Created on Sat May 18 16:22:10 2019

@author: Doreen
"""
import tkinter as tk

def go_to_solution():
    f3.pack()
    f2.pack_forget()

def go_to_n5():
    f1.pack_forget()
    f2.pack()
    
def go_to_gap():
    f3.pack_forget()
    f2.pack()

master = tk.Tk()

# Frame zur Auswahl des Levels
f1 = tk.Frame(master)
l1 = tk.Label(f1, text="Wähle einen Level aus:")
l1.pack()
b1 = tk.Button(f1, text="N5", command=go_to_n5)
b1.pack()

# Frame mit Lückentext
f2 = tk.Frame(master)
l2 = tk.Label(f2, text="Lückentext")
l2.pack()
b2 = tk.Button(f2, text="Lösung", command=go_to_solution)
b2.pack()

# Frame mit Lösung
f3 = tk.Frame(master)
l3 = tk.Label(f3, text="Lösung")
l3.pack()
b3 = tk.Button(f3, text="weiter", command=go_to_gap)
b3.pack()


# show first frame
f1.pack()

master.mainloop()
