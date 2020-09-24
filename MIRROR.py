from gtts import gTTS
import speech_recognition as sr
import re
import time
import webbrowser
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib
import requests
from pygame import mixer
import urllib.request
import urllib.parse
import json
import bs4
from playsound import playsound
import pyttsx3
engine =  pyttsx3.init()

def talk(audio):
    "speaks audio passed as argument"

    print(audio)
    for line in audio.splitlines():
        text_to_speech = gTTS(text=audio, lang="en-uk")
        mixer.init()
        engine.say("MIRROR ON AIR ")
        engine.runAndWait()
        mixer.music.load("audio.mp3")
        mixer.music.play()


def myCommand():
    "listens for commands"
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Your Mirror  is Ready...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        print("analyzing...")

    try:
        command = r.recognize_google(audio).lower()
        print("You said: " + command + "\n")
        time.sleep(1)


    except sr.UnknownValueError:
        print("Your last command couldn't be heard")
        command = myCommand()

    return command


def tars(command):
    errors = ["I don't know what you mean", "Excuse me?", "Can you repeat it please?"]
    "if statements for executing commands"

    if "welcome" in command:
         engine.say("HI ! welcome")
         engine.runAndWait()
         talk("HEY WELCOME")       
    elif "sad" in command:
         #engine.say("looking    dull    today")
         #engine.say("           what    happen    u  can   share with  me ,  ")
         #engine.say("i   am here to         help you    ")
         #engine.say( "CHEER UP  !! ITS YOUR DAY")
         #engine.runAndWait()
         mixer.music.load("sad.mp3")
         mixer.music.play()
         talk("CHEER UP  !! ITS YOUR DAY")
    elif "i am dinesh" in command:
        engine.say( "Hello! dinesh ")
        engine.say( "good to see you ")
        engine.say( "Hello! I am Eupheric MIRROR")
        talk(" I am E-MIRROR  How can I help you?")
        engine.runAndWait()

    elif "hello" in command:
        engine.say( "Hello! I am Eupheric MIRROR")
        engine.say( "How can I help you?")
        talk("Hello! I am E-MIRROR  How can I help you?")
        engine.runAndWait()
    elif "who are you" in command:
        talk("I am  E - MIRROR , your friend")
        time.sleep(1)
    else:
        error = random.choice(errors)
        talk(error)
        time.sleep(1)


talk(" MIRROR activated!")

while True:
    time.sleep(1)
    tars(myCommand())
