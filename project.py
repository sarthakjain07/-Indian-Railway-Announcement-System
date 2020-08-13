import os # used to interact with os
import pyaudio # use to play and record audio files
import pandas # provides high performance data structures and data analysing tools
from gtts import gTTS # convert text to speech
from pydub import AudioSegment # manipulating or playing with audios

def textToSpeech(text, filename):
    myobj=gTTS(text=str(text), lang="en", slow=False)
    myobj.save(filename)

def mergeAudios(audios):
    '''This func is used to merge audios'''
    integrate=AudioSegment.empty() # this is func of AudioSegment
    for audio in audios:
        integrate += AudioSegment.from_mp3(audio) # takes the audio(voice) from audio
    return integrate    

def developScripts():
    '''This function generate clips from audio'''
    # 1 provoke May I have your attention please
    audio=AudioSegment.from_mp3('railway.mp3') # takes the audio from raiway.mp3
    start= 18500      # in milisecond
    finish= 23500
    finalaudio=audio[start:finish] # slicing the part of audio needed
    finalaudio.export("1_H.mp3",format='mp3') # exporting audio file with name 1.mp3 and format mp3
    
    # 3 provoke se chalkar
    audio=AudioSegment.from_mp3('railway.mp3')
    start= 30400 
    finish= 31100
    finalaudio=audio[start:finish]
    finalaudio.export("3_H.mp3",format='mp3')

    # 5 provoke to
    audio=AudioSegment.from_mp3('railway.mp3')
    start= 31700 
    finish= 32500
    finalaudio=audio[start:finish]
    finalaudio.export("5_H.mp3",format='mp3')
    
    # 7 provoke via
    audio=AudioSegment.from_mp3('railway.mp3')
    start= 33900 
    finish= 34800
    finalaudio=audio[start:finish]
    finalaudio.export("7_H.mp3",format='mp3')

    # 9 provoke is arriving shortly....
    audio=AudioSegment.from_mp3('railway.mp3')
    start= 36600 
    finish= 40300
    finalaudio=audio[start:finish]
    finalaudio.export("9_H.mp3",format='mp3')

    
def developAnnouncements():
    '''This function generates announcements'''
    xl_content=pandas.read_excel("announce_hindi.xlsx")#reading the xcel file using pandas.read_excel
    print(xl_content)
    for index, item in xl_content.iterrows():
        # 2 train no. and name
        textToSpeech(item['train_no']+" "+item['train_name'], '2_H.mp3')
        # 4 from city
        textToSpeech(item['from'], '4_H.mp3') # this func will convert text to speech and give it a filename
        # 6 to city
        textToSpeech(item['to'], '6_H.mp3')
        # 8 via cities
        textToSpeech(item['via'], '8_H.mp3')
        # 10 platform no.
        textToSpeech(item['platform'], '10_H.mp3')
        audios=[f"{i}_H.mp3" for i in range(1,11)] # list comprehension in python
        announcement=mergeAudios(audios)
        announcement.export(f"{item['train_name']}.mp3", format="mp3")


if __name__ == "__main__":
    print("JAI KANHAIYA LAL KI")
    print("Developing Scripts.......")
    developScripts() #No need to run this again as we have got files already
    developAnnouncements()    