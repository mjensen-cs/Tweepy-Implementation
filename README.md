# Tweepy Implementation
Final project for CS 6500 - AI

## Overview
* Implements Tweepy library with Twitter API to collect tweets containing keywords from 5 trending topics on Twitter.
* Sends tweets to Microsoft Cognitive Services Text Analytics
* Retrieves Sentiment Analysis
* Graphs Analysis
* Analyzes two different poems. One happy, one sad

### report Directory
contains latex information for final report

### texts Directory
contains texts that can be analyzed, including a full copy of Gulliver's
Travels by Johnothan Swift

### analyze.py
Main driver application

## What to do to run
#### Needed:
* Twitter Developer Account and associated keys
* Microsoft Cognitive Services Account and associated keys

#### To Do:
Create a config.py file with the following fields:

From Twitter:
* ACCESS_TOKEN
* ACCESS_SECRET
* CONSUMER_KEY
* CONSUMER_SECRET
* BEARER_TOKEN

From Microsoft:
* API_KEY
* API_ENDPOINT


## Helpful Resources:
docs.tweepy.org

https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/sentiment-opinion-mining/quickstart?pivots=programming-language-python
