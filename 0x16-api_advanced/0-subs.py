#!/usr/bin/python3
""" retrieves number of subscribers of subreddit """
import requests


def number_of_subscribers(subreddit):
    rURL = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    h = {"User-Agent": 'any agent'}

    data = requests.get(rURL, h, allow_redirects=False).json().get('data')
    if data is None:
        return 0
    return data.get('subscribers')