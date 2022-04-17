import tweepy
import credential_configuration
import pandas as pd
import pickle

#We are using the client service of the v2 api
client = tweepy.Client(bearer_token=credential_configuration.BEARER_TOKEN)

#Query for finding tweets that contain certain information
query = None

#Information that we need to extract from each tweet. See the structure of a tweet in the Twitter API Documentation
attributes = ["id",'author_id', 'created_at',"entities","conversation_id"]

"""
Input: number of tweets required, query, attributes
Output: list of tweets (tweet: object) with the attributes specified
"""
def get_tweets(number_required, query, attributes):
    tweet_list = []

    for tweet in tweepy.Paginator(client.search_recent_tweets, query=query,tweet_fields=attributes, max_results=10).flatten(limit=number_required):
        tweet_list.append(tweet)

    return tweet_list

"""
Input: list of tweets
Output: dataframe with each tweet as a row, and columns correspond to 
        the attributes of the tweet
"""
def organize_tweets_in_dataframe(tweet_list):
    dictionary = {}  # Dictionary used to construct Data Frame

    sample_tweet = tweet_list[0]
    for key in sample_tweet.keys():
        dictionary[key] = []

    for tweet in tweet_list:
        for key in sample_tweet.keys():
            list_of_keyvalues = dictionary[key] 
            list_of_keyvalues.append(tweet[key])

    df = pd.DataFrame(dictionary)
    #Data management
    df['created_at'] = df['created_at'].dt.tz_localize(None)
    first_column = df.pop("id")
    df.insert(0, 'id', first_column)

    return df
