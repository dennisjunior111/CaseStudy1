# Example 5: Collecting searching result here
# Description: conduct tweets search and store the data in json file
# Author: Xuanyu Li
# Date: Jan, 29, 2016

from urllib import unquote
import authorize
import json

# rerieve the searching result from the given hot topic
# twitter_api: api used to access twitter
# q: the hot topic we want to choose
# count: # of a batch of searching results
"""
 [rerieve the searching result from the given hot topic]
 @param  {[object]} twitter_api [api used to access twitter]
 @param  {[str]} q           [the hot topic we want to choose]
 @param  {[int]} count       [number of a batch of searching results]
 @return {[dict]}             [searching results by the given criteria]
"""
def twitter_search(twitter_api, q, count):
    # See https://dev.twitter.com/docs/api/1.1/get/search/tweets
    search_results = twitter_api.search.tweets(q=q, count=count)
    statuses = search_results['statuses']

    # set the maximum searching results first [200, 100,0000]
    max_results = 500

    # Iterate through 5 more batches of results by following the cursor
    for _ in range(5):
        print "Length of statuses", len(statuses)
        try:
            next_results = search_results['search_metadata']['next_results']
        except KeyError, e: # No more results when next_results doesn't exist
            break
        # Create a dictionary from next_results, which has the following form:
        # ?max_id=313519052523986943&q=NCAA&include_entities=1
        kwargs = dict([ kv.split('=') for kv in unquote(next_results[1:]).split("&") ])

        search_results = twitter_api.search.tweets(**kwargs)
        statuses += search_results['statuses']

        if len(statuses) >= max_results:
            break

    return statuses

# save the specified data into json file
"""
/**
 * [save the retrieved searching result into json file]
 * @param  {[type]} filename [the name of the saved file]
 * @param  {[type]} data     [searching results]
 * @return {[type]}          [none]
 */
"""
def save_json(filename, data):
    with open(filename, 'w') as f:
        f.write(unicode(json.dumps(data, indent=1)))

twitter_api = authorize.oauth_login() # added line of code from authorize.py
# XXX: Set this variable to a trending topic,
# or anything else for that matter. The example query below
# was a trending topic when this content was being developed
# and is used throughout the remainder of this chapter.
q = 'WPI' #'#MentionSomeoneImportantForYou'
count = 100

data = twitter_search(twitter_api, q, count)
save_json("hot_topic.json", data)
