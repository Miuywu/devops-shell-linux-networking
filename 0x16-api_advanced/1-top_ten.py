#!/usr/bin/python3
""" prints top ten hot posts of subreddit """
import requests


def top_ten(subreddit):
    rURL = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    h = {"User-Agent": 'any agent'}

    hot_data = requests.get(rURL, h, allow_redirects=False).json().get('data')
    if hot_data is None:
        print(None)
    else:
        for a in range(10):
            title = hot_data.get('children').get(str(a)).get('data')
            print(title.get('title'))
