# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
#import random
import re

# Funktion gibt eine Liste aller Sätze mit einem bestimmten wort 'vocab' aus dem Korpus zurück
def get_sentences(vocab, korpus):
    tree = ET.parse(korpus)
    root = tree.getroot()
    sentence_list=[]
    for text in root:
        for sentence in text:
            for line in str(sentence.text).splitlines():
                if len(line.split())==5:
                    if line.split()[1]==vocab:
                        sentence_list.append(sentence.text)
    return sentence_list

# Funktion soll alle Sätze aus einer Satzliste zurückgeben, die mit einem Lemma-Pattern un einem Tag-Pattern matchen
# momentanes Problem: Tag-Pattern
def get_pattern(sentence_list, pattern_l, pattern_t):
    matches=[]
    for sentence in sentence_list:
        lemmas=''
        tags=''
        for line in sentence.splitlines():
            if len(line.split())==5:
                lemmas += line.split()[1]
                tags += line.split()[2]
                if re.match(pattern_l,lemmas) is not None:
                    print(sentence)
                    if re.match(pattern_t,tags) is not None:
                        matches.append(sentence)
    return(matches)   

# Funktion die in den Sätzen der Liste das Wort findet und durch Lücke ersetzt.
# Die Funktion gibt ein Tupel mit dem Satz und dem Lösungswort zurück.

import random

def delete_word(sentence_list, vocab):
    sentence = random.choice(sentence_list)
    sList = sentence.splitlines()
    wordList = []
    blanc = []
    for s in sList:
        if s != '':
            wordList.append(s.split())
    for word in wordList:
        if word[1] != None:
            if word[1] == vocab:
                blanc.append('<blanc>')
                solution = word[0]
            else:
                blanc.append(word[0])
    blanc = ''.join(blanc)
    return (blanc, solution)
 
# Tests:    
pl=re.compile('(\w+[はも])?\w+が(\w+)?大きい(\w+)?')
pt=re.compile('(\w+P.bind)?\w+P.c.g(\w+)?Ai.free(Aux)?')
k =  'jpWaC-L4.vert'
v = '大きい'
m=get_sentences(v,k)
for t in get_pattern(m, pl,pt):
    print(t)

s = delete_word(m, v)
