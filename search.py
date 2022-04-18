from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import tweepy
import config
import numpy as np
import matplotlib.pyplot as plt


def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint,
        credential=ta_credential)
    return text_analytics_client


def sentiment_analysis(client, tweets):
    count = 0
    avg_sentiment = [0, 0, 0]

    response = client.analyze_sentiment(documents=tweets)

    for post in response:
        print("Document Sentiment: {}".format(post.sentiment))
        print("Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \n".format(
            post.confidence_scores.positive,
            post.confidence_scores.neutral,
            post.confidence_scores.negative,
        ))
        avg_sentiment[0] += post.confidence_scores.positive
        avg_sentiment[1] += post.confidence_scores.neutral
        avg_sentiment[2] += post.confidence_scores.negative
        count += 1

    avg_sentiment[0] = avg_sentiment[0] / count
    avg_sentiment[1] = avg_sentiment[1] / count
    avg_sentiment[2] = avg_sentiment[2] / count

    print("Average Feelings\nPositive:{0:.2f}; neutral={1:.2f}; negative={2:.2f}\n".format(
        avg_sentiment[0],
        avg_sentiment[1],
        avg_sentiment[2],
    ))

    return avg_sentiment


def book_sentiment(client, text):
    response = client.analyze_sentiment(documents=text)[0]
    print("Document Sentiment: {}".format(response.sentiment))
    print("Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \n".format(
        response.confidence_scores.positive,
        response.confidence_scores.neutral,
        response.confidence_scores.negative,
    ))


client = tweepy.Client(bearer_token=config.BEARER_TOKEN)
key = config.API_KEY
endpoint = config.API_ENDPOINT

doja = 'doja lang:en -is:retweet'  # coachella trending
suns = 'suns lang:en -is:retweet'  # suns win game 1 of playoffs
# people talking about tweets by creator
dilbert = 'dilbert lang:en -is:retweet'
clonex = 'clonex lang:en -is:retweet'  # trending for business
kpop = 'kpop lang:en -is:retweet'  # trending in entertainment

analyze_client = authenticate_client()

# doja
response = client.search_recent_tweets(query=doja, max_results=10)
tweets = []
for tweet in response.data:
    tweets.append(tweet.text)
doja_sentiments = sentiment_analysis(analyze_client, tweets)

# suns
response = client.search_recent_tweets(query=suns, max_results=10)
tweets = []
for tweet in response.data:
    tweets.append(tweet.text)
suns_sentiments = sentiment_analysis(analyze_client, tweets)

# dilbert
response = client.search_recent_tweets(query=dilbert, max_results=10)
tweets = []
for tweet in response.data:
    tweets.append(tweet.text)
dilbert_sentiments = sentiment_analysis(analyze_client, tweets)

# clonex
response = client.search_recent_tweets(query=clonex, max_results=10)
tweets = []
for tweet in response.data:
    tweets.append(tweet.text)
clonex_sentiments = sentiment_analysis(analyze_client, tweets)

# kpop
response = client.search_recent_tweets(query=kpop, max_results=10)
tweets = []
for tweet in response.data:
    tweets.append(tweet.text)
kpop_sentiments = sentiment_analysis(analyze_client, tweets)


# plotting
labels = ['Positive', 'Neutral', 'Negative']
width = 0.166
plt.xticks(np.arange(len(doja_sentiments)) + 2 * width, labels)

doja_pos = np.arange(len(doja_sentiments))
suns_pos = np.arange(len(suns_sentiments)) + width
dilbert_pos = np.arange(len(dilbert_sentiments)) + (width * 2)
clonex_pos = np.arange(len(clonex_sentiments)) + (width * 3)
kpop_pos = np.arange(len(kpop_sentiments)) + (width * 4)

plt.bar(doja_pos, doja_sentiments, width=width, label='Doja')
plt.bar(suns_pos, suns_sentiments, width=width, label='Suns')
plt.bar(dilbert_pos, dilbert_sentiments, width=width, label='Dilbert')
plt.bar(clonex_pos, clonex_sentiments, width=width, label='Clonex')
plt.bar(kpop_pos, kpop_sentiments, width=width, label='KPop')
plt.title('Trending On Twitter')
plt.legend()
plt.show()

# book
lines = []
with open('happy_poem.txt') as g:
    lines = (g.readlines())

book_sentiment(analyze_client, lines)

with open('sad_poem.txt') as g:
    lines = (g.readlines())

book_sentiment(analyze_client, lines)
