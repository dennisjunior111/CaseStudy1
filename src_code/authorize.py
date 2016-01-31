# authorizing an application using OAuth authentication - Example 1
import twitter

# XXX: Go to http://dev.twitter.com/apps/new to create an app and get values
# for these credentials, which you'll need to provide in place of these
# empty string values that are defined as placeholders.
# See https://dev.twitter.com/docs/auth/oauth for more information
# on Twitter's OAuth implementation.

# fill the parameters for login first
def oauth_login():
    CONSUMER_KEY = 'oCTWWczTJuoGpTMFJaQWv0HhP'
    CONSUMER_SECRET ='nabcbzCgt8nU3QbxkIsSXxx6LLQBMI4EMLuHuJDHuZ6xB5PZQ4'
    OAUTH_TOKEN = '4859210933-axKkVKHXpC1BQtQEFlHM3eD6znG6RF57GDKYnec'
    OAUTH_TOKEN_SECRET = '3eHQcVSoDwJtcZWIiSKnuKc4FOci2rN9j5XiUQ6m3tOwd'

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET)

    twitter_api = twitter.Twitter(auth=auth)

    # Nothing to see by displaying twitter_api except that it's now a
    # defined variable

    return twitter_api
