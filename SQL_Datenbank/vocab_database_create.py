# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 15:50:06 2019

@author: Doreen
"""
import csv
f =open('voc.csv',encoding="utf-8")
csv_reader = csv.reader(f, delimiter=';')
l=[]
for i,row in enumerate(csv_reader):
    s=[]
    for e in row:
        if e =='':
            s.append('NULL')
        else:
            s.append(e)
    
    t=(i,s[0],s[1],s[2])
    l.append(t)

l[0]=(0, '会う', 'あう', 'to meet')
import sqlite3
connection = sqlite3.connect("vocab.db")

cursor = connection.cursor()


sql_command = """
CREATE TABLE IF NOT EXISTS word ( 
id INTEGER PRIMARY KEY, 
kanji NVARCHAR,
kana NVARCHAR,
meaning NVARCHAR
);"""

cursor.execute(sql_command)
#cursor.execute("INSERT INTO word VALUES(?,?,?,?)",(0, '会う', 'あう', 'to meet'))
for item in l:
    #print(item)
    cursor.executemany("INSERT INTO word VALUES(?,?,?,?)", (item,))
  
# To save the changes in the files. Never skip this.  
# If we skip this, nothing will be saved in the database. 
connection.commit() 
  
# close the connection 
connection.close() 
