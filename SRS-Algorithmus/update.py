# Spaced-Repetition-Algorithmus, auf dem SuperMemo2-Algorithmus basierend

import time

# Funktion, um neue Werte für easiness, repetitions, interval und nextPractice zu errechnen
def updateCard(repetitions, easiness, interval, quality):
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
