import tweepy
from datetime import datetime
import schedule
import time
from os import environ
# from auth import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, BEARER_TOKEN

num2daystr = {
    0 : "Monday", 
    1 : "Tuesday", 
    2 : "Wednesday", 
    3 : "Thursday", 
    4 : "Friday", 
    5 : "Saturday", 
    6 : "Sunday"
}

def job(client):
    day = datetime.today().weekday()
    if day == 5 or day == 6:
        return
    elif day >= 0 and day <= 3:
        tweet = "It's only {}.".format(num2daystr[day])
    else:
        tweet = "It's finally Friday!"
    client.create_tweet(text=tweet)

if __name__ == "__main__":

    client = tweepy.Client(bearer_token=environ.get('BEARER_TOKEN'), 
    consumer_key=environ.get('API_KEY'), 
    consumer_secret=environ.get('API_SECRET'), 
    access_token=environ.get('ACCESS_TOKEN'), 
    access_token_secret=environ.get('ACCESS_TOKEN_SECRET'))

    schedule.every().dat.at("06:00").do(job, client)
    while True:
        schedule.run_pending()
        time.sleep(1)
