import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from os import remove

def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = "voice.mp3"
    tts.save(filename)
    playsound(filename)
    remove("./"+filename)


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        print('listening...')
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio, show_all = True)
            print(said)
            print('done....')
        except Exception as e:
            print(e)
            return 0

    phrases = []
    for i in dict(said)['alternative']:
        phrases.append(i['transcript'])
    return phrases

def phrase_in(phrases, target):
    # print('\n'*2)
    # print(phrase['alternative'][0]['transcript'])
    # print('\n'*2)
    # if 'alternative' in dict(phrase).keys():
    #     for i in dict(phrase)['alternative']:
    #         try:
    #             if target in i['transcript'] and i['transcript'] == dict(phrase)['alternative'][0]['transcript']:
    #                 return 1
    #             if target in i:
    #                 speak(f'Did you say: {i}?')
    #                 answer = listen()
    #                 if phrase_in(answer, 'yes'): return 1

    #         except Exception as e:
    #             print(e)
    #             return 
    for i in phrases:
        if target in i and i == phrases[0]:
            return 1
        elif target in i:
            speak(f'Did you say: {i}?')
            answer = listen()
            if phrase_in(answer, 'yes'): return 1            

    return 0
    

    {'alternative': 
    [{'transcript': 'test', 'confidence': 0.93551201}, 
    {'transcript': 'text'}, 
    {'transcript': 'best'}], 
    'final': True}