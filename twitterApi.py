import requests

TWITTER_URL = 'https://api.twitter.com/1.1/search/tweets.json'

AUTH_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAEaYvQAAAAAAhDVWgZfs4c5v3TZXluuWFMOIJGQ%3DbuQxA3m3dIbR94iXjwB3AYyyUJFrAh26eg80hgydXmeNZ45m89'
MAX_TWEETS = 100


class TwitterApi(object):
    def search(self, search_param):
        params = {
            'q': search_param,
            'count': MAX_TWEETS
        }
        headers = {
            'Authorization': 'Bearer ' + AUTH_TOKEN,
            'content-type': 'application/json'
        }
        return requests.get(TWITTER_URL, params=params, headers=headers)


twitter_api = TwitterApi()
