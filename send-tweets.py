import twitter
import markov_chains
import os 

api = twitter.Api(
    consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
    consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
    access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
    access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

print api.VerifyCredentials()


def tweet(chains, last_words):
    # tweet_text = markov_chains.make_text(chains, last_words)
    # print tweet_text 
    user_input = "n"
    
    while user_input.lower() != "y":
        tweet_text = markov_chains.make_text(chains, last_words)
        print tweet_text
        user_input = raw_input("Would you like to tweet this? y/n: ")

    status = api.PostUpdate(tweet_text)
    print status.text

tweet(markov_chains.chains, markov_chains.last_words)