# News reader
import requests
import json
from win32com.client import Dispatch


def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':

    url = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    news = requests.get(url).text
    news_dict = json.loads(news)

    art =news_dict["articles"]

    for article in art:
        speak(article["title"])
        speak("Moving to next news")
