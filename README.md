# Elon-Musk-s-Tweets-Sentiment-Analysis

Created a Python script to use Elon Musk’s Tweets for sentiment analysis to predict the behavior of Tesla’s stock price.
To get Elon Musk’s Tweets, the Tweepy library accessed Twitter’s/X’s API and retrieved 1500 Tweets, then used TextBlob to analyze the sentiment of the Tweets. A polarity score of 0.23 was returned meaning the Tweets were slightly positive on average, with a subjectivity score of 0.35 meaning the Tweets were opinion based.
To find the effects of the Tweets on Tesla's stock price, the YFinance API was used to give Tesla’s changes in stock price 24 hours after the Tweet, and the Pandas library merged and organized the sentiment results. Then the data was graphically displayed to show correlation using Matplotlib. The correlation was approximately 0 since TextBlob struggles to interpret Musk’s Tweets accurately.
