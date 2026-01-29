import pyttsx3
import speech_recognition as sr
import eel
import time
def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)   # fixed key
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        eel.DisplayMessage('Listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=10, phrase_time_limit=6)
    try:
        eel.DisplayMessage('Recognizing...')
        query = r.recognize_google(audio, language="en-in")
        eel.DisplayMessage(query)
        time.sleep(2)
        return query.lower()
    except Exception:
        return ""
@eel.expose
def allCommands(message=1):
    if message == 1:
        query = takecommand()
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)
    if not query:
        speak("I didn't catch that. Please try again.")
        eel.ShowHood()
        return
    try:
        if "open" in query:
            from engine.features import openCommand
            openCommand(query)
        elif "on youtube" in query or "in youtube" in query:
            from engine.features import playYouTube
            playYouTube(query)
        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact, whatsApp
            flag = ""
            contact_no, name = findContact(query)
            if contact_no != 0:
                if "send message" in query:
                    flag = 'message'
                    speak("What message should I send?")
                    query = takecommand()
                elif "phone call" in query:
                    flag = 'call'
                else:
                    flag = 'video call'
                whatsApp(contact_no, query, flag, name)
        else:
            from engine.features import chatBot
            chatBot(query)
    except Exception as ex:
        speak("Something went wrong")
        print(ex)
    eel.ShowHood()