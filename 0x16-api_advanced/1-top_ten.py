#!/usr/bin/python3
"""
Write a function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit.
Requirements:
    Prototype: def top_ten(subreddit)
    If not a valid subreddit, print None.
    note: Invalid subreddits may return a redirect to search results.
        Ensure that you are not following redirects.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    """
    user_agent_str = ('Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0)'
                      'Gecko/20190101 Firefox/77.0')
    user_ag = {'User-Agent': user_agent_str}
    session = requests.Session()
    session.headers.update(user_ag)

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    request = session.get(url, headers=user_ag)
    if (request.status_code == 404):
        print(None)
        return
    posts = request.json().get('data').get('children')
    for post in posts[:10]:
        print(post.get('data').get('title'))
