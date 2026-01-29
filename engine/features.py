from groq import Groq
from shlex import quote
import struct
import subprocess
import webbrowser as wb
from playsound import playsound
import eel
import os
import re
import pvporcupine
import time
import pyaudio
import pyautogui
from engine.command import *
from engine.command import speak
from engine.config import *
import sqlite3 as sql
import pywhatkit as kit
from engine.helper import extract_yt_term, remove_words
conn = sql.connect("dynamo.db")
cursor = conn.cursor()
#playing assistant sound
@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)
#opening a windows app / executing a '.exe' file
@eel.expose
def openCommand(query) :
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()
    app_name = query.strip()
    if app_name != "" :
        try :
            cursor.execute("SELECT Path FROM sys_commands WHERE Name IN (?)", (app_name,))
            results = cursor.fetchall()
            if len(results) != 0 :
                speak("Opening " + query)
                os.startfile(results[0][0])
            elif len(results) == 0 :
                cursor.execute("SELECT URL FROM web_commands WHERE Domain IN (?)", (app_name,))
                results = cursor.fetchall()
                if len(results) != 0 :
                    speak("Opening " + query)
                    wb.open(results[0][0])
                else :
                    speak("Opening " + query)
                    try :
                        os.system(f'start {query}')
                    except :
                        speak(query + " not found")
        except :
            speak("Something went wrong...")
    # if query != "" :
    #     speak("Opening "  + query)
    #     os.system("start " + query)
    # else :
    #     speak("Sorry! " + query + " not found!")
#playing the video on YouTube
def playYouTube(query) :
    search_term = extract_yt_term(query)
    speak("Playing " + search_term + " on YouTube")
    kit.playonyt(search_term)
#detecting hot word
def hotWord() :
    porcupine = None
    paud = None
    audio_stream = None
    try :
        porcupine = pvporcupine.create(keywords = ["jarvis", "alexa"])
        paud = pyaudio.PyAudio()
        audio_stream = paud.open(rate = porcupine.sample_rate, channels = 1, format = pyaudio.paInt16, input = True, frames_per_buffer = porcupine.frame_length)
        while True :
            keyword = audio_stream.read(porcupine.frame_length)
            keyword = struct.unpack_from("h"*porcupine.frame_length, keyword)
            keyword_index = porcupine.process(keyword)
            if keyword_index >= 0 :
                print("Hot word detected.")
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("y")
                time.sleep(2)
                autogui.keyUp("win")
    except :
        if porcupine is not None :
            porcupine.delete()
        if audio_stream is not None :
            audio_stream.close()
        if paud is not None :
            paud.terminate()
#finding contact
def findContact(query) :
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'whatsapp', 'video']
    query = remove_words(query, words_to_remove)
    try :
        query = query.strip().lower()
        cursor.execute("SELECT Mobile FROM Contacts WHERE LOWER(Name) LIKE ? OR LOWER(Name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        print(results[0][0])
        mobile_number_str = str(results[0][0])
        if not mobile_number_str.startswith('+91') :
            mobile_number_str = '+91' + mobile_number_str
        return mobile_number_str, query
    except :
        speak('does not exist in contacts')
        return 0, 0
def whatsApp(mobile_no, message, flag, name):
    # Status messages
    dynamo_message = {
        "message": f"Message sent successfully to {name}",
        "call": f"Calling {name}",
        "video": f"Video calling {name}"
    }.get(flag, f"Opening chat with {name}")
    # Clean number
    mobile_no = str(mobile_no).replace("+", "").replace(" ", "")
    encoded_message = quote(message if flag == "message" else "")
    # Open WhatsApp
    whatsapp_url = f"https://wa.me/{mobile_no}?text={encoded_message}"
    try:
        subprocess.run(f'start "" "{whatsapp_url}"', shell=True)
        # Wait for WhatsApp to load
        timeout = time.time() + 20
        while time.time() < timeout:
            try:
                window = gw.getWindowsWithTitle("WhatsApp")[0] # type: ignore
                window.activate()
                break
            except:
                time.sleep(1)
        time.sleep(2)  # small buffer
        # Perform action
        if flag == "message":
            pyautogui.press("enter")
        elif flag == "call":
            pyautogui.hotkey("ctrl", "shift", "c")
        elif flag == "video":
            pyautogui.hotkey("ctrl", "shift", "v")
    except Exception as e:
        dynamo_message = f"Failed to process WhatsApp action: {e}"
    speak(dynamo_message)
def chatBot(query):
    client = Groq(api_key = API_KEY)
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": query}],
        temperature=1,
        max_tokens=512,
        top_p=1,
        stream=True
    )
    response_text = ""
    for chunk in completion:
        delta = chunk.choices[0].delta
        text = getattr(delta, "content", None)  # safely get content
        if text:  # only if not None
            print(text, end="", flush=True)
            response_text += text
    # print(response_text)
    speak(response_text)
    # return response_text