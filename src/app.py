from customModules.myModules import currentTime, trendingNews, writeProcesses, openApp, closeApp
from customModules.voice import aiVoice, userVoice
import multiprocessing
import os
import time
    
def main():
    assistant_name = "Sam"
    aiVoice(f"Hi, I am {assistant_name}! what is your name")
    user_name = userVoice()
    while True:
        if(type(user_name) == type(None)):
            aiVoice(f"Please let me know your name to find out if you are authorized to use {assistant_name}")
            file_path=f"./data/{user_name}.json"
            user_name = userVoice()
            if os.path.exists(file_path):
                print(f"The file at {file_path} exists.")
            else:
                print(f"The file at {file_path} does not exist.")
        else:
            aiVoice(f"Thank you for telling your name")
            break
    aiVoice(f"So how may I help you {user_name}")
    p1 = multiprocessing.Process(name='p1', target=currentTime, args=(False,))
    p2 = multiprocessing.Process(name='p2', target=writeProcesses, args=(user_name,))
    p1.start()
    p2.start()
                
    while True:
        user_response = userVoice()
        while not user_response == "Sam wake up" or user_response == "Sam I need to ask a question" or user_response == "Sam":
            time.sleep(1)
        aiVoice(f"what do you want to know")
        match "Sam open app":
            case "Sam what is the trending news":
                news_topic = userVoice()
                if(type(news_topic) == type(None)):
                    news_topic = userVoice()
                    aiVoice(f"Sorry I could not understand that please try again")
                    news_topic = userVoice()
                res = trendingNews(news_topic)
                aiVoice(f"Today's trending news is {res}")
                time.sleep(1)
                aiVoice(f"Wake me up if you need anything else")
                #working here
            case "Sam open app":
                openApp()
            case "Sam close app":
                closeApp()
            case "Sam what is the time":
                res = currentTime(False)
                aiVoice(f"The time is {res}")
                time.sleep(1)
                aiVoice(f"Wake me up if you need anything else")
            case user_command if user_command == "Sam Exit" or user_command == "Sam go to sleep":
                aiVoice(f"Thanks for using {assistant_name}")
                break
            case _:
                aiVoice("I'm sorry, I didn't understand what you said please try again.")
        
if __name__ == "__main__":
    main()