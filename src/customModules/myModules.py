import datetime
import time
import requests
import json
from plyer import notification
from customModules.voice import aiVoice
import AppOpener
import random
import os

API_SECRET="0a2e1437d3e4a66a60f3ee9481c88ace"

def currentTime(scheduled):
    if(scheduled == False):
        now = datetime.datetime.now()
        formatted_time = now.strftime("%I:%M:%S %p")
        return formatted_time        
    while True:
        time.sleep(3600)
        now = datetime.datetime.now()
        formatted_time = now.strftime("%I:%M:%S %p")
        notification.notify(
                title = "1 hour has passed",
                message=f"You are 1 hour near your death, the time now is {formatted_time}" ,
                timeout=2
            )
        aiVoice("1 hour near your death")
        
def trendingNews(topic):
    aiVoice("Tell me directly the topic of news you want to know.")
    url = f'https://gnews.io/api/v4/search?q={topic}&apikey={API_SECRET}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["articles"][0]["title"]
    else:
        print(f"Error: {response.status_code}")

def writeProcesses(data):
    data = {
        "user_name": data
    }
    json_object = json.dumps(data)
    json_file_path = os.path.join(os.path.dirname(__file__), '..', 'data')
    with open(f"{json_file_path}/{data["user_name"]}.json", "w") as file:
        file.write(json_object)
        
def openApp(name):
    AppOpener.open(name)
    
def closeApp(appName):
    AppOpener.close(appName)