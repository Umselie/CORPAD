# -*- coding: utf-8 -*-
"""
Created on Sat May 18 12:18:28 2019

@author: Doreen
"""
import sqlite3
connection = sqlite3.connect("vocab.db")

cursor = connection.cursor()
for row in cursor.execute('SELECT * FROM word'):
        print(row)

connection.commit() 
  
# close the connection 
connection.close() 