import tweepy
import os

from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv("auth.env")

    auth = tweepy.OAuthHandler(os.getenv("API_KEY"), os.getenv("API_KEY_SECRET"))
    auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))
    
    api = tweepy.API(auth)

    api.update_status("Test tweet from Tweepy Python")