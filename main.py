import yoppa_lib as yl


while True:
    phrase = yl.listen()
    
    # l = yl.phrase_in(phrase)
    
    # for i in l: print(i)

   
    if yl.phrase_in(phrase, 'count'):
        for i in range(0, 10): print(i, end=' ')
        break

    else:
        yl.speak("repeat")
