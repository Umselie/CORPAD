# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 18:01:52 2019

@author: amkaf
"""

# Das Wörterbuch kann man hier (www.edrdg.org/jmdict/j_jmdict.html) finden
# Es ist leider zu groß zum Hochladen 

"""
# Versuch alle Einträge, die nicht deutsch sind, aus dem Worterbuch zu entfernen
# root.remove(entry) funktioniert leider nicht. Fehler: "list.remove(x): x not in list"

import xml.etree.ElementTree as ET
tree = ET.parse('JMdict')
root = tree.getroot()

for entry in root.findall('entry'):
    for sense in entry.findall('sense'):
        for gloss in sense.findall('gloss'):
            lang = gloss.attrib
            if lang['{http://www.w3.org/XML/1998/namespace}lang'] != 'ger':
                root.remove(entry) 
                
tree.write('JMdictGer.xml')
"""

# Funktion die aus dem vollstandigen Wörterbuch die Definition findet

# vocab muss in Hiragana oder Katakana sein im Wörterbuch sind keine Kanji
# die Lesungen von Komposita/sino-japanische Lesungen müssen in Hiragana angegeben werden
# alles was normalerweise mit Katakana geschrieben wird in Katakana

def find_def(vocab):
    tree = ET.parse('JMdict')
    root = tree.getroot()

    for entry in root.findall('entry'):
        for r_ele in entry.findall('r_ele'):
            for reb in r_ele.findall('reb'):
                if reb.text == vocab:
                    for sense in entry.findall('sense'):
                        for gloss in sense.findall('gloss'):
                            lang = gloss.attrib
                            if lang['{http://www.w3.org/XML/1998/namespace}lang'] == 'ger':
                                return(str(gloss.text))

beispiel1 = find_def('おおきい')
beispiel2 = find_def('かいしゃ')
beispiel3 = find_def('アイスクリーム')
