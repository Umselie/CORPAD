# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
#import random
import config


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
                blanc.append('____')
                solution = word[0]
            else:
                blanc.append(word[0])
    blanc = ''.join(blanc)
    return (blanc, solution)
 
# Funktion: Worte konstant, Satzstrukturen variabel
def fixed_word(vocab, korpus):
    sentence_list = get_sentences(vocab, korpus)
    sentence_with_solution = delete_word(sentence_list, vocab)
    config.globalsolution = sentence_with_solution[1]
    return(sentence_with_solution[0])
'''
 # Tests:    
pl=re.compile('(\w+[はも])?\w+が(\w+)?大きい(\w+)?')
pt=re.compile('(\w+P.bind)?\w+P.c.g(\w+)?Ai.free(Aux)?')
k =  'jpWaC-L3.vert'
v = getword('N5')[1]
m=get_sentences(v,k)
#for t in get_pattern(m, pl,pt):
    #print(t)
#print(v)
s = fixed_word(v,k)

print(s)
print(config.solutionxoxo)
'''