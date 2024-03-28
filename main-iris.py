import pyttsx3
import wikipedia
import speech_recognition as sr
import webbrowser
import datetime
import sys
import smtplib
from OCR import OCR
from helpers import *
from youtube import youtube
from sys import platform
import os
import pytesseract

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

def say(text):
    engine.say(text)
    engine.runAndWait()


class Iris:
    def takeCommand(self):
        recognize = sr.Recognizer()
        with sr.Microphone() as source:
            print('Waiting for the command')
            recognize.adjust_for_ambient_noise(source)
            try:
                audio = recognize.listen(source, timeout=5)
                print('Processing...')
                query = recognize.recognize_google(audio, language='en-us')
                print(f'{query}\n')
                return query
            except sr.UnknownValueError:
                say("Sorry, I couldn't understand the audio. Please try again.")
            except sr.RequestError as e:
                say(f"Speech recognition request failed; {e}")
            except Exception as e:
                say(f"An unexpected error occurred: {e}")

    def wishMe(self) -> None:
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            say("Good Morning,I'm iris,How may I help you today?")
        elif hour >= 12 and hour < 18:
            say("Good Afternoon, I'm iris,What would you like to search?")
        else:
            say('Good Evening, I am Iris. Please tell me how can I help you?')

    def sendEmail(self, to, content) -> None:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('jesica20jes20@gmail.com', 'Boardtopper!')
        server.sendmail('jesica20jes20@gmail.com', to, content)
        server.close()

    def execute_query(self, query):

        if 'wikipedia' in query:
            say('Searching Wikipedia....')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=5)
            say('According to Wikipedia')
            print(results)
            say(results)

        elif 'youtube downloader' in query:
            exec(open('youtube_downloader.py').read())

        elif 'voice' in query:
            if 'male' in query:
                engine.setProperty('voice', voices[0].id)
                say("Hello, I have switched my voice. How is it?")


        elif 'email' in query:
            to = input("Enter the recipient's email address: ")
            content = input("Enter the email content: ")
            iris = Iris()
            iris.sendEmail(to, content)

        elif 'are you there' in query:
            say("Yes master, at your service")

        elif 'open youtube' in query:
            webbrowser.open('https://youtube.com')

        elif 'open amazon' in query:
            webbrowser.open('https://amazon.com')

        elif 'open google' in query:
            webbrowser.open('https://google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('https://stackoverflow.com')

        elif 'play music' in query:
            webbrowser.open('https://youtu.be/mJW57E7GpSo?feature=shared')

        elif 'search youtube' in query:
            say('What you want to search on Youtube?')
            youtube(takeCommand())

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f'Sir, the time is {strTime}')

        elif 'search' in query:
            say('What do you want to search for?')
            search = takeCommand()
            url = 'https://google.com/search?q=' + search
            webbrowser.open(
                url)
            say('Here is What I found for' + search)

        elif 'location' in query:
            say('What is the location?')
            location = takeCommand()
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.open(url)
            say('Here is the location ' + location)

        elif 'your name' in query:
            say('My name is Iris')

        elif 'who made you' in query:
            say('I was created by my master in 2021')

        elif 'shutdown' in query:
            if platform == "win32":
                os.system('shutdown /p /f')

        elif 'your friend' in query:
            say('My friends are Google assisstant alexa and siri')

        elif 'github' in query:
            webbrowser.open(
                'https://github.com/jesca20')

        elif 'note this' in query:
            say("what should i remember sir")
            rememberMessage = takeCommand()
            say("you said me to remember" + rememberMessage)
            remember = open('data.txt', 'w')
            remember.write(rememberMessage)
            remember.close()

        elif 'do you remember anything' in query:
            remember = open('data.txt', 'r')
            say("you said me to remember that" + remember.read())

        elif 'sleep' in query:
            sys.exit()

        elif 'dictionary' in query:
            say('What you want to search in your intelligent dictionary?')
            translate(takeCommand())

        elif 'news' in query:
                say('Opening bbc news...')
                webbrowser.open('https://www.bbc.com/news')
                say('You can now read the full news from this website.')

def wakeUpIris():
    bot_ = Iris()
    bot_.wishMe()
    while True:
        query = takeCommand().lower()
        bot_.execute_query(query)

if __name__ == '__main__':
    wakeUpIris()
