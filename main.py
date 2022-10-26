import tweepy
import os

from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv("auth.env")

    auth = tweepy.OAuthHandler(os.getenv("API_KEY"), os.getenv("API_KEY_SECRET"))
    auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))
    
    api = tweepy.API(auth)

    name = 'stable_bird'
    tweet_id = '1582123837432291329'

    replies=[]
    for tweet in tweepy.Cursor(api.search,q='to:'+name, result_type='recent', timeout=999999).items(1000):
        if hasattr(tweet, 'in_reply_to_status_id_str'):
            if (tweet.in_reply_to_status_id_str==tweet_id):
                replies.append(tweet)
    
    print(replies)