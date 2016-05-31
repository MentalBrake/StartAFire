import json
import sys

from twitterApi import twitter_api


class Tweet(object):
    def __init__(self, username, user_image_url, text, image_url):
        self.username = username.encode('ascii', 'ignore') if username else ''
        self.user_image = user_image_url
        self.text = text.encode('ascii', 'ignore') if text else ''
        self.image_url = image_url


args = sys.argv

search_terms = []
output_file = 'index.html'
if args[1] == '-ofile':
    output_file = args[2]
    search_term = args[3]
else:
    search_term = args[1]

results = twitter_api.search(search_term)

data = json.loads(results.content)

tweets = data['statuses']

tweets_with_images = []
for tweet in tweets:
    if tweet.get('entities'):
        if tweet['entities'].get('media'):
            for image in tweet['entities']['media']:
                tweets_with_images.append(Tweet(username=tweet['user']['name'],
                                                user_image_url=tweet['user']['profile_image_url'],
                                                text=tweet['text'],
                                                image_url=image.get('media_url')))

f = open(output_file, 'w')

message = """<html>
<head>
</head>
<body style='margin-left:30%;'>"""

for tweet in tweets_with_images:
    message += """<div style='
                display: flex;
                flex-direction:row;
               font-family:"Helvetica Neue";
               font-size: 12px;
               font-weight: bold;
               line-height: 16px;
               border-color: #eee #ddd #bbb;
               border-radius: 5px;
               border-style: solid;
               border-width: 1px;
               box-shadow: 0 1px 3px rgba(0, 0, 0, 0.15);
               margin: 10px 5px;
               padding: 16px;
               max-width: 468px;'>"""
    message += """<div style='padding-right:10px;'><img src="{0}" style='border:0;border-radius:5px;'/></div>""".format(
        tweet.user_image)
    message += """<div>"""
    message += "<div>{0}</div>".format(tweet.username)
    message += "<p style='font-size: 16px;font-weight: normal;line-height: 20px;'>'{0}'</p>".format(tweet.text)
    message += "<img src='{0}' style='width:100%; border:0; border-radius:5px;'>".format(tweet.image_url)
    message += "<br/>"
    message += """</div>"""
    message += "</div>"

message += """</body></html>"""

f.write(message)
f.close()
