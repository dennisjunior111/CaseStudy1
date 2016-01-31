import json
from collections import Counter
# load data from the saved json file
statuses = json.loads(open('hot_topic.json').read())

# The result of the list comprehension is a list with only one element that
# can be accessed by its index and set to the variable t
status_texts = [ status['text']
                 for status in statuses ]

screen_names = [ user_mention['screen_name']
                 for status in statuses
                     for user_mention in status['entities']['user_mentions'] ]

hashtags = [ hashtag['text']
             for status in statuses
                 for hashtag in status['entities']['hashtags'] ]

# Compute a collection of all words from all tweets
words = [ w
          for t in status_texts
              for w in t.split() ]

# Explore the first 5 items for each...

print json.dumps(status_texts[0:5], indent=1)
print json.dumps(screen_names[0:5], indent=1)
print json.dumps(hashtags[0:5], indent=1)
print json.dumps(words[0:5], indent=1)

# Creating a basic frequency distribution from the words in tweets
for item in [words, screen_names, hashtags]:
    c = Counter(item)
    print c.most_common()[:10] #TODO: change # of top 10
    print


c = Counter(words)
print type(c)
