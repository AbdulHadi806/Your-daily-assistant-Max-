from customModules.myModules import currentTime, trendingNews, writeProcesses, openApp, closeApp
from customModules.voice import aiVoice, userVoice
import multiprocessing
import asyncio
import time

async def main():
    assistant_name = "Sam"
    aiVoice(f"Hi, I am {assistant_name}! what is your name")
    user_name = await userVoice()
    while True:
        if(type(user_name) == type(None)):
            aiVoice(f"Please let me know your name to find out if you are authorized to use {assistant_name}")
            user_name = await userVoice()
        else:
            aiVoice(f"Thank you for telling your name")
            break
    aiVoice(f"I can help you. Ask me {user_name}")
    p1 = multiprocessing.Process(name='p1', target=currentTime, args=(False,))
    p2 = multiprocessing.Process(name='p2', target=writeProcesses, args=(user_name,))
    p1.start()
    p2.start()
    while True:
        print("loop running again")
        user_response = await userVoice()
        aiVoice(f"what do you want to know")
        if(user_response == "news"):
            aiVoice(f"Need to know the topic of trending news")
            print('test')
            news_topic = await userVoice()
            if(type(news_topic) == type(None)):
                news_topic = await userVoice()
                aiVoice(f"Sorry I could not understand that please try again")
                news_topic = await userVoice()
            res = trendingNews(news_topic)
            aiVoice(f"Today's trending news is {res}")
            time.sleep(1)
            aiVoice(f"Wake me up if you need anything else")
        elif(user_response == "open app"):
            aiVoice("What app do you want to open")
            appName = await userVoice()
            openApp(appName)
        elif(user_response == "close app"):
            aiVoice("Sure, what is the app name")
            appName = userVoice()
            closeApp()
        elif(user_response == "what is the time"):
            res = currentTime(False)
            aiVoice(f"The time is {res}")
            time.sleep(1)
            aiVoice(f"Wake me up if you need anything else")
        elif(user_response == "exit" or user_response == "go to sleep") :
            aiVoice(f"Thanks for using {assistant_name}")
            break
        else:
            aiVoice("I'm sorry, I didn't understand what you said please try again.")
        
if __name__ == "__main__":
    asyncio.run(main())