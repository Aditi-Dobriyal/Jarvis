import pyttsx3 #pip install pyttsx3
import speech_recognition as sr
import os
import webbrowser
import openai
from config import apikey
import datetime
import random
import numpy as np

# import win32com.client
# speaker= win32com.client.Dispatch("SAPI.SpVoice")

# print("Enter: ")
# s=input()
# speaker.Speak(s)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        query=r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
# chatStr = ""
# # https://youtu.be/Z3ZAJoi4x6Q
# def chat(query):
#     global chatStr
#     print(chatStr)
#     openai.api_key = apikey
#     chatStr += f"Harry: {query}\n Jarvis: "
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt= chatStr,
#         temperature=0.7,
#         max_tokens=256,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#     )
#     # todo: Wrap this inside of a  try catch block
#     say(response["choices"][0]["text"])
#     chatStr += f"{response['choices'][0]['text']}\n"
#     return response["choices"][0]["text"]


# def ai(prompt):
#     openai.api_key = apikey
#     text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=prompt,
#         temperature=0.7,
#         max_tokens=256,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#     )
#     # todo: Wrap this inside of a  try catch block
#     # print(response["choices"][0]["text"])
#     text += response["choices"][0]["text"]
#     if not os.path.exists("Openai"):
#         os.mkdir("Openai")

#     # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
#     with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
#         f.write(text)

# def say(text):
#     os.system(f'say "{text}"')

# def takeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         # r.pause_threshold =  0.6
#         audio = r.listen(source)
#         try:
#             print("Recognizing...")
#             query = r.recognize_google(audio, language="en-in")
#             print(f"User said: {query}")
#             return query
#         except Exception as e:
#             return "Some Error Occurred. Sorry from Jarvis"

if __name__ == '__main__':
        while True:
    # if 1:
         query = takeCommand().lower()


    # print('Welcome to Jarvis A.I')
    # speak("Jarvis A.I")
    # while True:
    #     print("Listening...")
    #     query = takeCommand()
#         # todo: Add more sites
#         sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"],]
#         for site in sites:
#             if f"Open {site[0]}".lower() in query.lower():
#                 say(f"Opening {site[0]} sir...")
#                 webbrowser.open(site[1])
#         # todo: Add a feature to play a specific song
#         if "open music" in query:
#             musicPath = "/Users/harry/Downloads/downfall-21371.mp3"
#             os.system(f"open {musicPath}")

#         elif "the time" in query:
#             musicPath = "/Users/harry/Downloads/downfall-21371.mp3"
#             hour = datetime.datetime.now().strftime("%H")
#             min = datetime.datetime.now().strftime("%M")
#             say(f"Sir time is {hour} bajke {min} minutes")

#         elif "open facetime".lower() in query.lower():
#             os.system(f"open /System/Applications/FaceTime.app")

#         elif "open pass".lower() in query.lower():
#             os.system(f"open /Applications/Passky.app")

#         elif "Using artificial intelligence".lower() in query.lower():
#             ai(prompt=query)

#         elif "Jarvis Quit".lower() in query.lower():
#             exit()

#         elif "reset chat".lower() in query.lower():
#             chatStr = ""

#         else:
#             print("Chatting...")
#             chat(query)





        # say(query)