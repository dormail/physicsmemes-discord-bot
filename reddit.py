import requests
import json

def get_reddit_post():
    subreddit = 'physicsmemes'
    count = 1
    timeframe = 'day' #hour, day, week, month, year, all
    listing = 'random' # controversial, best, hot, new, random, rising, top

    def get_reddit(subreddit,count):
        try:
            base_url = f'https://www.reddit.com/r/{subreddit}/{listing}.json'
            request = requests.get(base_url, headers = {'User-agent': 'yourbot'}, params = {'count': count, 't': timeframe})
        except:
            print('An Error Occurred')
        return request.json()

    top_post = get_reddit(subreddit,count)

    if listing != 'random':
        url = top_post['data']['children'][0]['data']['url']
    else:
        url = top_post[0]['data']['children'][0]['data']['url']

    print(f'Sharing {url}')

    return url
