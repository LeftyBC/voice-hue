#!/usr/bin/python

import pyaudio
import time

import speech_recognition as sr
r = sr.Recognizer()

keyword = "computer"

while True:
    # use the default microphone as the audio source
    with sr.Microphone() as source:
        # listen for the first phrase and extract it into audio data
        print("Listening...")
        audio = r.listen(source)

        try:
            # recognize speech using Google Speech Recognition
            speech = r.recognize(audio).lower()
            print("You said: %s " % speech)

            if speech[:len(keyword)] == keyword:
                print("This would have been a command, prefixed by '%s'" % keyword)
            time.sleep(3)
        except LookupError:
            # speech is unintelligible
            print("Could not understand audio")
