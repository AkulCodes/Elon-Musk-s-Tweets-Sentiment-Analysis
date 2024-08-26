import tweepy
import yfinance as yf
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt


# Twitter API credentials 
consumer_key = ""
consumer_secret = ""
access_token = "-"
access_token_secret = ""

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Fetch Elon Musk's tweets
tweets = api.user_timeline(screen_name='elonmusk', count=100, tweet_mode='extended')

tweet_data = []
for tweet in tweets:
    analysis = TextBlob(tweet.full_text)
    sentiment = analysis.sentiment.polarity
    tweet_data.append({'Date': tweet.created_at.date(), 'Tweet': tweet.full_text, 'Sentiment': sentiment})


tweet_df = pd.DataFrame(tweet_data)

stock_data = yf.download('TSLA', start='YYYY-MM-DD', end='YYYY-MM-DD')  # Set your desired date range

tweet_df_grouped = tweet_df.groupby('Date').mean()

merged_data = pd.merge(stock_data, tweet_df_grouped, how='inner', left_index=True, right_on='Date')

correlation = merged_data['Sentiment'].corr(merged_data['Close'])
print(f'Correlation between tweet sentiment and stock closing price: {correlation}')

plt.figure(figsize=(10, 5))
plt.plot(merged_data.index, merged_data['Close'], label='TSLA Closing Price')
plt.plot(merged_data.index, merged_data['Sentiment'], label='Tweet Sentiment', color='red')
plt.title('Tesla Stock Price vs. Elon Musk Tweet Sentiment')
plt.legend()
plt.show()
