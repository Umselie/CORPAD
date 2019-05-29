# -*- coding: utf-8 -*-


import sqlite3
import random

# Hilfsfunktion als vorläufigen Ersatz für SRS-Agorithmus
# Gibt ein zufälliges Tupel der Form (id,kana,kanji,definition) zurück

def getword():
    connection = sqlite3.connect("vocab.db")
    cursor = connection.cursor() 
    x=(random.randint(1,669),)
    cursor.execute('SELECT * FROM word WHERE id=?',x)
    result = cursor.fetchone()
    connection.close()
    return result

