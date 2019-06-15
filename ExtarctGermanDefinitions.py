# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 18:01:52 2019

@author: amkaf
"""

# Funktion die alle Einträge aus dem Wörterbuch entfernen soll, die nicht Deutsch sind
# Das Wörterbuch kann man hier (www.edrdg.org/jmdict/j_jmdict.html) finden

import xml.etree.ElementTree as ET
tree = ET.parse('JMdict')
root = tree.getroot()

for entry in root.findall('entry'):
    for sense in entry.findall('sense'):
        for gloss in sense.findall('gloss'):
            lang = gloss.attrib
            if lang['{http://www.w3.org/XML/1998/namespace}lang'] != 'ger':
                root.remove(entry) # funktioniert noch nicht
                
tree.write('JMdictGer.xml')