# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 13:06:27 2019

@author: Doreen
"""

# Spaced-Repetition-Algorithmus, auf dem SuperMemo2-Algorithmus basierend

import time
import random

def getwordslists(level):
    connection = sqlite3.connect("vocab.db")
    cursor = connection.cursor() 
    request = 'SELECT * FROM ' +  level + ' WHERE nextPractice >='+str(int(round(time.time() * 1000)))
    revisions = cursor.execute(request)
    config.globalrevisions = cursor.fetchmany(20)
    i = 20 - len(config.globalrevisions)
    print(i)
    x = 10+i
    request = 'SELECT * FROM ' +  level + ' WHERE repetitions = 0'
    new = cursor.execute(request)
    config.globalnew = cursor.fetchmany(size=x)
    
    connection.close()
    config.global_new_and_revisions = [config.globalrevisions,config.globalnew]

def getword():
    config.global_current_word = random.choice(random.choices(config.global_new_and_revisions, weights=map(len, config.global_new_and_revisions))[0])
    return

''''
for e in getword('N5'):
    print(e)
connection.close()
'''

# Funktion, um neue Werte für easiness, repetitions, interval und nextPractice zu errechnen
def getNewValues(quality):
    repetitions = config.global_current_word[4]
    easiness = config.global_current_word[5]
    interval = config.global_current_word[6]
    
    assert quality >= 0 and quality <= 5
    
    easiness = max(1.3, easiness + 0.1 - (5.0 - quality) * (0.08 + (5.0 - quality) * 0.02))
    
    if quality < 3:
        repetitions = 0
    else:
        repetitions += 1
        
        
    if repetitions <=1:
        interval =1
    elif repetitions == 2:
        interval = 6
    else:
        interval = round(interval * easiness)
        
        
    secondsInDay = 60 * 60 * 24
    now = int(round(time.time() * 1000))
    nextPractice = now + secondsInDay*interval
    
    return(repetitions,easiness,interval,nextPractice)

def updateCard(quality):
    newValues = getNewValues(quality)
    connection = sqlite3.connect("vocab.db")
    cursor = connection.cursor()
    cursor.execute('UPDATE' + config.globallevel + 'SET repetitions = ' + newValues[0] + ', easiness = ' + newValues[1] +', interval = ' + newValues[2] + ', nextPractice = ' + newValues[3] + ' WHERE id = ' + config.global_current_word[0])