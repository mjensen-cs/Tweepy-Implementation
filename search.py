import tweepy
import config

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

query = '#POTUS lang:en -is:retweet'

response = client.search_recent_tweets(query=query, max_results=10)

# prints JSON
print(response.data)

# for tweet in response.data:
#   print(tweet.text + '\n')

# Todo:
#   * feed tweets into Microsoft AI
#   * save output in some sort of fashion
#   * use pandas to graph changes

# Notes:
#   * printing response.data prints JSON, this can be used to store the search_recent_tweets
#   * https://docs.microsoft.com/en-us/azure/synapse-analytics/machine-learning/tutorial-text-analytics-use-mmlspark

