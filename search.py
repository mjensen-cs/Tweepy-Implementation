import tweepy
import config

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

query = '#POTUS lang:en -is:retweet'

response = client.search_recent_tweets(query=query, max_results=10)

for tweet in response.data:
    print(tweet.text + '\n')

# response.data is JSON

# Todo:
#   * save tweets in some sort of fashion
#   * feed tweets into Microsoft AI
#   * save output in some sort of fashion
#   * use pandas to graph changes
